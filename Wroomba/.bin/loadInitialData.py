import json
import pygame as pg

if __name__ == "__main__":
    data = {
        "initialDisplayDimensions": (1200, 700),
        "initialBackgroundDimensions": (1200, 700),
        "initialRoombaDimensions": (75, 75),
        "initialRoombaPosition": (100, 100),
        "roombaInitialAngle": 0,
        "initialTitle": "Wroomba",
        "initialFlag": pg.RESIZABLE,
        "initialFPS": 60
    }

    with open('initialData.json', 'w') as f:
        json.dump(data, f)

    f.close()
