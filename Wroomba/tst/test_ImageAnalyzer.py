from lib import ImageAnalyzer as imgan
from tkinter.filedialog import askopenfilename

import cv2
import matplotlib.pyplot as plt


if __name__ == "__main__":
    path = askopenfilename()

    # Show original image
    image = cv2.imread(path)
    plt.imshow(image)
    plt.xticks([])
    plt.yticks([])
    plt.title("Original")
    plt.show()

    # Analyzer has to be created, and then manually call image binarize
    analyzer = imgan.ImageAnalyzer()

    # analyzer.path = path  # Manually assign path

    # analyzer.loadImage(imagePath=path)  # Parse path while loading image

    analyzer.binarizeImage(imagePath=path)  # Binarize image from provided path

    # Compare binarized image
    plt.imshow(analyzer.bitMap)
    plt.xticks([])
    plt.yticks([])
    plt.gray()
    plt.title("Binarized image")
    plt.show()
