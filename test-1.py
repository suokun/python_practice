__author__ = 'suokun'

# to use Image .etc, you should install pillow or PIL first
from PIL import Image, ImageDraw, ImageFont

sourceFileName = "./Wechat.png"
wechat = Image.open(sourceFileName)
drawWechat = ImageDraw.Draw(wechat)

xSize, ySize = wechat.size
fontSize = min(xSize, ySize) // 5

myFont = ImageFont.truetype("/Library/Fonts/Monaco for Powerline.otf", fontSize)

drawWechat.text([0.8 * xSize, 0.2 * ySize - fontSize],\
    "5", fill = (255, 0, 0), font = myFont)
del drawWechat

wechat.show()

# Reference:
# https://github.com/Show-Me-the-Code/python/blob/master/LiamHuang/0000/solution.py
