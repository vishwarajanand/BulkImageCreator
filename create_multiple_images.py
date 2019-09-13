import os
from PIL import Image, ImageDraw, ImageFont

# create 10x10=100 images
TotalImageRows = 10
TotalImageColumns = 10

# create images of resolution width x height
# keep atleast 400x400
Width = 700
Height = 700

def getStringifiedNumber(x):
    switcher = {
    1: str(x)+"st",
    2: str(x) + "nd",
        3: str(x) + "rd",
        0: str(x) + "th",
    }
    switcher_selector = abs(x)% 10
    if switcher_selector > 3:
        switcher_selector = 0
    return switcher.get(switcher_selector)


def getImageName(i,j):
    return getStringifiedNumber(i) + " image of " + getStringifiedNumber(j) + " product."


def createImage(name):
    # create Image object with default size
    image = Image.new('RGB', (Width, Height), color='red')

    # or create Image object with default image in cwd
    # image = Image.open('default.png')

    # initialize the drawing context with the image object as background
    draw = ImageDraw.Draw(image)

    # create font object with the font file and specify desired size
    font = ImageFont.truetype('Roboto-Bold.ttf', size=45)

    # starting position of the message
    (x, y) = (50, 50)
    message = "Demo Image"
    color = 'rgb(0, 0, 0)'  # black color

    # draw the message on the background
    draw.text((x, y), message, fill=color, font=font)
    (x, y) = (150, 150)
    color = 'rgb(255, 255, 255)'  # white color
    draw.text((x, y), name, fill=color, font=font)

    # save the edited image
    image.save(name + '.png')


print("Creating " + str(TotalImageRows * TotalImageColumns) + " images.");
for i in range(1, TotalImageRows + 1):
    for j in range(1, TotalImageColumns + 1):
        image_name = getImageName(i,j)
        createImage(image_name)
        print("Created image number: " + image_name)


print("Images are located at: " + os.getcwd())
print("You may upload them on GitHub to get hosted internet URLs.")
