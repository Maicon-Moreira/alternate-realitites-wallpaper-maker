import cv2
from cv2 import dnn_superres
import cv2
import numpy as np

# sr = dnn_superres.DnnSuperResImpl_create()
# path = "FSRCNN_x2.pb"
# sr.readModel(path)
# sr.setModel("fsrcnn", 2)


def extractImages(path_in, path_out):
    count = 0
    vidcap = cv2.VideoCapture(path_in)
    success, image = vidcap.read()
    success = True
    while success:
        vidcap.set(cv2.CAP_PROP_POS_MSEC, (count * 1000))
        success, image = vidcap.read()

        vertical_margin = 270
        image = image[vertical_margin:-vertical_margin]

        # image = sr.upsample(image)

        cv2.imwrite(
            path_out + "\\frame%d.png" % count,
            image,
        )
        print("Read a new frame: ", count)
        count = count + 1


if __name__ == "__main__":
    path_in = "video.mkv"
    path_out = "frames/"

    extractImages(path_in, path_out)
