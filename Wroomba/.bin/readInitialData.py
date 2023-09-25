import json
import pygame as pg

if __name__ == "__main__":
    with open('initialData.json', 'r') as f:
        data = json.load(f)

    f.close()
    print(data)
    print(type(data["initialFPS"]))
    print(type(data["initialDisplayDimensions"]))
