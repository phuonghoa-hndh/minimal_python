# Convert CSV Annotations to Paddle-OCR-compatible format

This program allows you to convert annotations stored in CSV files into a Paddle-OCR-compatible format.

## Usage

1. **Install Python:** 
    - Ensure you have Python installed on your computer. If not, you can download Python from the [official Python website](https://www.python.org/downloads/).

2. **Install Dependencies:**
    - Run the following command to install the required dependencies:
        ```
        pip install pandas
        ```

3. **Run the Program:**
    - Open a command prompt or terminal window.
    - Navigate to the directory containing the source code of the program.
    - Run the program using the following command:
        ```
        python convert.py /path/to/folder
        ```
    - Replace `/path/to/folder` with the path to the folder containing the CSV annotation files you want to convert.

4. **Output:**
    - After the program finishes running, the Label.txt file will be created in the directory containing the CSV annotation files. This Label.txt file will contain the information converted from the CSV files.

## Requirements

- Python 3.x
- pandas library

## Additional Information

Only for [ID_CARD_LABEL Computer Vision Project](https://universe.roboflow.com/vo-duc-duy/id_card_label).
License:
Can be used freely for commercial use
Credit text: Creative Commons ID_CARD_LABEL dataset by Vo Duc Duy is licensed under CC by 4.0.


