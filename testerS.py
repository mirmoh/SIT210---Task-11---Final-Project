import serial
import time
import requests

if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.flush()
    
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            
            if (line == "pump on for 1 second"):
                print("low mositure, turning on the water pump for 1 second!")
                
                #webhook request
                r = requests.post('https://maker.ifttt.com/trigger/pump_on/with/key/c-6jBnvfEBtQXRccm8izTl')
                print ("Message sent!")
                
            elif (line == "unadvised, pump off"):
                print ("Water pump off")
                