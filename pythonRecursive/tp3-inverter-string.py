def inverter_string(string):
    if len(string) == 0:
        return ""
    return string[-1] + inverter_string(string[:-1])

string = "recursao"
print(inverter_string(string))
