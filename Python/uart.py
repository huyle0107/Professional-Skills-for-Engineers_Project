print("Hello Sensors")
import serial.tools.list_ports
import time

def getPort():
    ports = serial.tools.list_ports.comports()
    N = len(ports)
    commPort = "None"
    for i in range(0, N):
        port = ports[i]
        strPort = str(port)
        if "ST" in strPort:
            splitPort = strPort.split(" ")
            commPort = (splitPort[0])
    return "COM7"

portName = getPort()
if portName != "None":
    ser = serial.Serial(port=portName, baudrate=115200)
    print(ser)

mess = ""

def processData(client, data):
    data = data.replace("!", "")
    data = data.replace("#", "")
    splitData = data.split(":")
    print(splitData)
    if splitData[1] == "T":
        if int(splitData[2]) >= 30:
            client.publish("v12", "100")
            client.publish("v1", splitData[2])
        elif int(splitData[2]) <= 25:
            client.publish("v1", splitData[2])
            client.publish("v12", "0")
        else:
            client.publish("v1", splitData[2])
    if splitData[1] == "H":
        client.publish("v2", splitData[2])
    if splitData[1] == "L":
        client.publish("v3", splitData[2])
    if splitData[1] == "B":
        client.publish("v10", splitData[2])
    if splitData[1] == "C":
        client.publish("v11", splitData[2])
    if splitData[1] == "F":
        client.publish("v12", splitData[2])

def readSerial(client):
    bytesToRead = ser.inWaiting()
    if (bytesToRead > 0):
        global mess
        mess = mess + ser.read(bytesToRead).decode("UTF-8")
        while ("#" in mess) and ("!" in mess):
            start = mess.find("!")
            end = mess.find("#")
            processData(client, mess[start:end + 1])
            if (end == len(mess)):
                mess = ""
            else:
                mess = mess[end+1:]

def WriteSerial(data):
    ser.write(str(data)).encoder('utf-8')
