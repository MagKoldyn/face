from remember import remember
from training import getImagesAndLabels
from interpretator import interpretator, cam, recognizer, cascadePath, faceCascade, font, id, names, minW, minH
import cv2
import numpy as np


remember()

path = "face"
recognizer = cv2.face.LBPHFaceRecognizer_create()
detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

getImagesAndLabels(path)

print ("\n [INFO] Training faces. It will take a few seconds. Wait ...")
faces,ids = getImagesAndLabels(path)
recognizer.train(faces, np.array(ids))

recognizer.write('trainer/trainer.yml')

interpretator(cam, recognizer, cascadePath, faceCascade, font, id, names, minW, minH)

