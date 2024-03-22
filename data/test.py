import json
import csv
import sys
import pandas as pd

# from PIL import Image, ImageFont, ImageDraw, ImageEnhance
#
#
# source_img = Image.open("/home/teko/Downloads/ID_CARD_LABEL.v1i.retinanet/train/00cddf83-c1eb-4fc3-a1ed-68c2d6cae965_jpg.rf.9e4fb563f3f2c1183fa7bf05ad7b291f.jpg")
#
# draw = ImageDraw.Draw(source_img)
# draw.polygon([(0, 0), (499, 0), (499, 299), (0, 299)], fill= None, outline=(255, 255, 0))
#
# source_img.save("ouput.jpg", "JPEG")
data = pd.read_csv("/home/teko/PycharmProjects/OCR_idcards/data/anno.csv", header = None, names=["filename", "xmin", "ymin", "xmax", "ymax", "type"])

print(data)



# result = {}
#
# for line in data:
#     parts = line.split(",")
#     filename = parts[0]
#     coordinates = [int(x) for x in parts[1:5]]
#     type_ = parts[5]
#
#     if filename not in result:
#         result[filename] = []
#
#     result[filename].append({"coordinates": coordinates, "type": type_})
#
# print(result)








