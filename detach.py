import cv2
import os
import glob

methods = [
    cv2.CHAIN_APPROX_SIMPLE,
    cv2.CHAIN_APPROX_NONE,
    cv2.CHAIN_APPROX_TC89_KCOS,
    cv2.CHAIN_APPROX_TC89_L1
]

modes = [
    cv2.RETR_CCOMP,
    cv2.RETR_EXTERNAL,
    #cv2.RETR_FLOODFILL,
    cv2.RETR_LIST,
    cv2.RETR_TREE
]

files = glob.glob('set_final/*')
for file in files:
    image = cv2.imread(file)
    image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    # black and white
    _, image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV)

    # find contours of each character
    x=0
    for mode in modes:
        y=0
        for method in methods:
            _, image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV)
            contours, _ = cv2.findContours(image, mode, method)
            test = cv2.drawContours(image, contours, -1, (0,255,0), 3)
            cv2.imwrite(f"characters/{x}_{y}.png",test)
            y += 1
        x += 1
    

    continue

    characters_region = []

    # find character contours
    for contour in contours:
        (x, y, width, height) = cv2.boundingRect(contour)
        area = cv2.contourArea(contour)
        print ("area: " + str(area))
        if area > 115:
            characters_region.append((x, y, width, height))
    
    if len(characters_region) != 5:
        print (len(characters_region))
        continue

    #print character
    final_image = cv2.merge([image]*3)
    
    i=0
    for rectangle in characters_region:
        x, y, width, height = rectangle
        character_image = image[y-2:y+height+2, x-2:x+width+2]
        file_name = os.path.basename(file).replace(".png",f"char{i}.png")
        cv2.imwrite(f"characters/{file_name}",character_image)
        cv2.rectangle(final_image, (x-2, y-2), (x+width+2, y+height+2), (0, 255, 0), )
        i += 1
        
    cv2.imwrite(f"identfied/{os.path.basename(file)}", final_image)