from PIL import Image

def main():
    car_name = input("Car name? ")
    car_file_name = car_name + ".jpeg"
    car_image = Image.open(car_file_name)

    rgb_car_image = car_image.convert("RGB")

    #r, g, b = rgb_car_image.getpixel((100, 100))

    #print(r, g, b)

    pixeldata = car_image.load()

    for x in range(car_image.size[0]):
        for y in range(car_image.size[1]):
            r, g, b = rgb_car_image.getpixel((x, y))
            if r > 4 and r < 100:
                if g > 19 and g < 125:
                    if b > 70 and b < 232:
                        pixeldata[x, y] = (0, 255, 0, 255)
                

    car_image.save("tester.png")

    car_image.show()


while 1 != 2:
    main()
