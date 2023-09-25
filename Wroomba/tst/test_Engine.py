from lib import Engine as eng
from lib import ImageAnalyzer as imgan

from tkinter.filedialog import askopenfilename
import copy
import matplotlib.pyplot as plt


def showImg(image, title=""):
    plt.imshow(image)
    plt.gray()
    plt.xticks([])
    plt.yticks([])
    plt.title(title)
    plt.show()


def draw16Plots(plotsList, collisionList):
    fig, ax = plt.subplots(4, 4)

    iterator = 0
    for i in range(4):
        for j in range(4):
            if iterator < len(plotsList):
                ax[i, j].imshow(plotsList[iterator], cmap='gray')
                ax[i, j].set_xticks([])
                ax[i, j].set_yticks([])
                ax[i, j].set_title(collisionList[iterator])

                iterator += 1
    plt.show()


if __name__ == "__main__":
    analyzer = imgan.ImageAnalyzer()
    engine = eng.Engine()

    analyzer.path = askopenfilename()
    analyzer.loadImage()
    analyzer.binarizeImage()

    engine.bitMap = analyzer.bitMap
    engine.setRoomba(x=100, y=200, angle=0, radius=25)
    engine.setMask(engine.roomba.radius)

    bitMapWithMaskCopy = copy.deepcopy(engine.bitMap)

    # Test showing of mask according to roomba`s position

    # set both ranges accordingly to the background image you are testing
    xRoombaPositions = [i for i in range(100, 990, 10)]
    yRoombaPositions = [i for i in range(500, 800, 100)]

    counter = 0
    plotList = []
    collisionList = []

    for y in yRoombaPositions:
        for x in xRoombaPositions:
            engine.roomba.x = x
            engine.roomba.y = y

            bitMapWithMaskCopy = copy.deepcopy(engine.bitMap)

            # print(f'en.roomba.x = {engine.roomba.x}, en.roomba.y = {engine.roomba.y}')

            for (xOff, yOff) in engine.mask:
                bitMapWithMaskCopy[engine.roomba.y + yOff, engine.roomba.x + xOff] = 1

            collision = engine.willCollisionOccur(roombaPositionShift=engine.roomba.getPos())
            # showImg(bitMapWithMaskCopy, f"({x}, {y}), collision = {collision}")

            # maskScope = bitMapWithMaskCopy[engine.roomba.y - engine.roomba.radius : engine.roomba.y + engine.roomba.radius + 1,
            #                                engine.roomba.x - engine.roomba.radius : engine.roomba.x + engine.roomba.radius + 1]

            if counter == 16:
                draw16Plots(plotList, collisionList)

                counter = 0
                plotList = []
                collisionList = []
            else:
                counter += 1
                plotList.append(bitMapWithMaskCopy)
                collisionList.append(f'{engine.roomba.x},{engine.roomba.y}:{collision}')

