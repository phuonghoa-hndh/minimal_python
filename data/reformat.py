import json
import csv
import sys
from PIL import ImageDraw, Image

data =[]
result = {}
with (open("/home/teko/PycharmProjects/OCR_idcards/data/anno.csv", "r", encoding="utf-8") as file):
    csv_read = csv.reader(file, delimiter=',')
    for row in csv_read:
        data.append(row)
        file_name = row[0]
        row[5] = row[5].split(',')

        #label mapping
        replacement = {
            "barcode": "barcode",
            "cccd_front": "cccd_front",
            "cmnd_front": "cmnd_front",
            "dob": "dob_value",
            "exp_date": "expire_date_value",
            "face": "face",
            "id": "id_value",
            "name": "name_value",
            "national": "nationality_value",
            "place": "current_place_value",
            "place_orig": "place_origin_value",
            "sex": "sex_value"
        }
        row[5] = [replacement.get(item,item) for item in row[5]]
        key = row[5]

        # convert x, y, width, height into this type - "points": [[359.0, 163.0], [751.0, 163.0], [751.0, 194.0], [359.0, 194.0]]
        # idea: [x, y] [x+w, y] [x+w, y+h] [x, y+h]
        first_element = [int(row[1]), int(row[2])]
        second_element = [int(row[1]) + int(row[3]), int(row[2])]
        third_element = [int(row[1]) + int(row[3]), int(row[2]) + int(row[4])]
        forth_element = [int(row[1]), int(row[2]) + int(row[4])]

        #concat dictionaries
        transcription = {"transcription":""}
        points = {"points": [first_element, second_element, third_element, forth_element]}
        difficult = {"difficult": "false"}
        key_cls = {"key_cls": key}

        dict_list = [transcription, points, difficult, key_cls]
        # for d in dict_list:
        #     result.update(d)


        # result[file_name].append({"transcription":"", "points": [first_element, second_element, third_element, forth_element], "difficult": "false", "key_cls": key})

        print(data)


# with open("data.json", "w") as json_file:
#     json.dump(result, json_file)







