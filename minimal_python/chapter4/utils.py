# def str_to_int(string):
#     return int(string)

# def str_to_int(string):
#     string = string.replace(',', '.')
#     return int(float(string))
def str_to_int(string):
    if ',' in string and '.' in string:
        string = string.split('.')[0]
        string = string.replace(',', '')
        return int(string)
    string = string.replace(',', '.')
    return int(float(string))