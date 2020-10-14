from time import sleep
from sense_emu import SenseHat
from PIL import Image, ImageDraw
import time
from datetime import datetime
import os

#Create object to get data from the SenseHAT Emulator
hat = SenseHat()

sleep(5)
hat.clear()

#Get the current date and time to use as filenaame
fname = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
path = os.path.join('/home/pi/Desktop/'+str(fname)+'.txt')



while True:
    
    data = []

    #Getting magnetometer readings
    mag = hat.get_compass_raw()
    mag_data = []
    mag_data.append(round(mag["x"],2))
    mag_data.append(round(mag["y"],2))
    mag_data.append(round(mag["z"],2))
    

    #Getting accelerometer readings
    acc = hat.get_accelerometer_raw()
    acc_data = []
    acc_data.append(round(acc["x"],3))
    acc_data.append(round(acc["y"],3))
    acc_data.append(round(acc["z"],3))

    #Getting gyroscope reading
    gyro = hat.get_orientation()
    gyro_data = []
    gyro_data.append(round(gyro["pitch"],2))
    gyro_data.append(round(gyro["yaw"],2))
    gyro_data.append(round(gyro["roll"],2))
    
    data.append(mag_data)
    data.append(acc_data)
    data.append(gyro_data)
    
    #Write acquired data to file
    with open(path,'a') as file:
        file.write(str(data)+"\n")
    
    #Read data every 0.5 seconds
    sleep(0.5) 