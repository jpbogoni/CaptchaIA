import cv2
import os
import glob
from PIL import Image

def imagehandler(path_origin, path_finish='set_final'):
    files = glob.glob(f"{path_origin}/*")
    for file in files:
        image = cv2.imread(file)
        #transform image to grayscale
        image_gray = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)

        #apply cv2.THRESH_TRUNC or cv2.THRESH_OTSU
        _, image_new = cv2.threshold(image_gray, 127, 255, cv2.THRESH_TRUNC or cv2.THRESH_OTSU)
        cv2.imwrite(f"{path_finish}/aplicado.png", image_new)


        image = Image.open(f"{path_finish}/aplicado.png")
        image = image.convert("P")
        image2 = Image.new("P", image.size, 255)
        
        #set pixel black
        for x in range(image.size[1]):
            for y in range(image.size[0]):
                pixel = image.getpixel((y, x))
                if pixel < 115:
                    image2.putpixel((y, x),0)

        #save converted image
        image2.save(f"{path_finish}/{os.path.basename(file)}")
        #glob.delete(f"{path_finish}/aplicado.png")

imagehandler("set","set_final")