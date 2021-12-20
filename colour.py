import cv2
import pandas as pd
image_path = r'colour_image.jpg'
image = cv2.imread(image_path)

#global variables
clicked = False
r = g = b = x_pos = y_pos = 0

# reading csv file using pandas
index = ["colour", "colour_name", "hex", "R", "G", "B"]
csv = pd.read_csv('colors.csv', names=index, header=None)

#calulating the most maching clolour
def get_colour_name(R, G, B):
    minimum = 10000
    for i in range(len(csv)):
        d = abs(R - int(csv.loc[i, "R"])) + abs(G - int(csv.loc[i, "G"])) + abs(B - int(csv.loc[i, "B"]))
        if d <= minimum:
            minimum = d
            cname = csv.loc[i, "colour_name"]
    return cname

# function for the x and y coordinates of the places where there is double click
def draw_function(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global b, g, r, x_pos, y_pos, clicked
        clicked = True
        x_pos = x
        y_pos = y
        b, g, r = image[y, x]
        b = int(b)
        g = int(g)
        r = int(r)

cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_function)

while True:
    cv2.imshow("image", image)
    if clicked:

        cv2.rectangle(image, (20, 20), (750, 60), (b, g, r), -1)
        text = get_colour_name(r, g, b) + ' R=' + str(r) + ' G=' + str(g) + ' B=' + str(b)
        cv2.putText(image, text, (50, 50), 2, 0.8, (255, 255, 255), 2, cv2.LINE_AA)
        if r + g + b >= 600:
            cv2.putText(image, text, (50, 50), 2, 0.8, (0, 0, 0), 2, cv2.LINE_AA)
        clicked = False
    
    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()