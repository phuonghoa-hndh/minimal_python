import argparse
import json
import csv
import pandas as pd

def main(folder_path):
    data = pd.read_csv(f"{folder_path}/_annotations.csv", header=None, names=["filename", "x_min", "y_min", "width", "height", "type"])

    results = {}
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

    for row in data.itertuples():
        if row.filename not in results:
            results[row.filename] = []
        results[row.filename].append(
            {
                "transcription": "",
                "key_cls": replacement[row.type],
                "points": [[row.x_min, row.y_min], [row.x_min + row.width, row.y_min], [row.x_min + row.width, row.y_min + row.height], [row.x_min, row.y_min + row.height]],
                "difficult": False
            }
        )

    with open(f"{folder_path}/Label.txt", "w") as f:
        for k, v in results.items():
            f.write(f"{k}\t{json.dumps(v)}\n")

    print("Done!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert folder containing CSV annotations to Label.txt file ")
    parser.add_argument("folder_path", help="Saved folder path") #Path to the folder containing CSV annotations and where the Label.txt file will be saved

    args = parser.parse_args()
    main(args.folder_path)
