# !/usr/bin/env python3
# Program name:          car_wrapper.py
# Author(s):                 Zack Steck
#Date:                          03/05/2018

''' Works with car_builder, will handle both painting and wrapping a car '''

import time
from PIL import Image

print("This program only works with cars taht already exist. It cannot create new cars for you. ")
print("If you do not already have a car, please use 'car_builder' to create one and then come back. ")

def stockPicGenerator(car_name):
    car_file_name = car_name + ".jpeg"
    car_image = Image.open(car_file_name)

    rgb_car_image = car_image.convert("RGB")

    #r, g, b = rgb_car_image.getpixel((100, 100))

    #print(r, g, b)

    pixeldata = car_image.load()

    car_image.show()

    print("Perparing the car for paint/wrap", end="")
    for i in range(5):
        time.sleep(0.5)
        print(".", end="")
    print("")
    
    
    for x in range(car_image.size[0]):
        for y in range(car_image.size[1]):
            r, g, b = rgb_car_image.getpixel((x, y))
            if r > 4 and r < 100:
                if g > 19 and g < 125:
                    if b > 70 and b < 232:
                        pixeldata[x, y] = (0, 255, 0, 255)
                

    car_image.save("stock.png")

    car_image.show()

def getCar():
    car_model = input("What model car do you want to work on? ")
    car_name = input("What's the name of the car you want to work on? ")

    #car_file = open(car_name, "r")

    modded = input("Does your car have any visual mods? ")
    if "y" in modded.lower():
        modded = True
    else:
        modded = False

    print("Generating an image of the stock car", end="")
    for i in range(5):
        time.sleep(0.5)
        print(".", end="")
    print("")
    stockPicGenerator(car_name)
    
    if modded:
        print("Applying visual mods to the car", end="")
        for i in range(5):
            time.sleep(0.5)
            print(".", end="")
        print("")
        print("Visual mods applied! ")
        
    
def paintCar():
    #temp
    print("", end="")
    
def wrapCar():
    #temp
    print("", end="")
    
def showCar():
    #temp
    print("", end="")
