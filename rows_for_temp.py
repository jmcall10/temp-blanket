import cv2
import numpy as np
import pandas as pd



# Create a black image
black_box = np.zeros((1200, 1440, 3), np.uint8)
cv2.imwrite("black_box.jpg", black_box)
img = cv2.imread('black_box.jpg')

df = pd.read_csv('charlotte_fixed_rgb.csv')

print(df)
y = 0
option = 'B'
for row in df.itertuples():
    if 1 == 1:
    #if row.Index > 87:
        print(row)
        hot_str = str(row.hot_rgb_value).replace(" ", "").split(',')
        print(hot_str)
        r = hot_str[0]
        g = hot_str[1]
        b = hot_str[2]
        cold_str = str(row.cold_rgb_value).replace(" ", "").split(',')
        r2 = cold_str[0]
        g2 = cold_str[1]
        b2 = cold_str[2]
        daylight_pixels_across = int(row.sunset_pixels_across) - int(row.sunrise_pixels_across)
        if option == 'A':
            while(daylight_pixels_across % 3 != 0):
                daylight_pixels_across = daylight_pixels_across - 1
            stitches = daylight_pixels_across / 3

            cv2.rectangle(img, (0, y * 8), (int(daylight_pixels_across), (y * 8 + 8)), (int(b),int(g),int(r)), thickness=-1)
            cv2.rectangle(img, (int(daylight_pixels_across), y * 8), (1440, y * 8 + 8), (int(b2),int(g2),int(r2)), thickness=-1)
            # text = "stitch count: " + str(stitches) + ", yarn color: " + ("yarn color")
            # font = cv2.FONT_HERSHEY_SIMPLEX
            # #text2 = "yarn color: " + str(stitches)

            # # Define the position of the text
            # org = (50,500 + (y * 30))

            # # Define the font scale and color
            # fontScale = .5
            # color = (255, 255, 255)
            # cv2.putText(img, text, org, font, fontScale, color, 2)
        
            
        if option == 'B':
            average_str = str(row.average_rgb_value).replace(" ", "").split(',')
            r3 = average_str[0]
            g3 = average_str[1]
            b3 = average_str[2]
            cv2.rectangle(img, (0, y * 8), (int(row.sunrise_pixels_across), (y * 8 + 8)), (int(b),int(g),int(r)), thickness=-1)
            cv2.rectangle(img, (int(row.sunrise_pixels_across), y * 8), (int(row.sunset_pixels_across), (y * 8 + 8)), (int(b3),int(g3),int(r3)), thickness=-1)
            cv2.rectangle(img, (int(row.sunset_pixels_across), y * 8), (1440, y * 8 + 8), (int(b2),int(g2),int(r2)), thickness=-1)
        
# Add the text to the image
        y = y + 1

cv2.imwrite("tangle.jpg", img)
cv2.imshow("Black Box", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
#cv2.rectangle(img, (0, start), (start5, start2), (start3, 100, start4), thickness=-1)
    
    