import json
import pygame as pg
from tkinter.filedialog import askopenfilename

if __name__ == "__main__":
    # with open(askopenfilename()) as f:
    #     data = json.load(f)

    data = {
    "initialDispBackDimensions" : (1200, 700),
    "initialRoombaDimensions" : (75, 75),
    "initialRoombaPosition" : (100, 100),
    "roombaInitialAngle" : 0,
    "initialTitle" : "Wroomba",
    "initialFlag" : pg.RESIZABLE,
    "initialFPS" : 60
    }
    with open('data.json', 'w') as f:
        json.dump(data, f)
    f.close()

    print(data)
