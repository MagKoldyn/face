import cv2
import os
def remember():
    cap = cv2.VideoCapture(0)
    cap.set(3, 640)
    cap.set(4, 480)

    face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    face_id = input("Enter your id: ")

    print('Смотри в камеру')
    count = 0
    while True:
        ret, img = cap.read()
        img = cv2.flip(img, 1)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
            count += 1
            cv2.imwrite("face/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h, x:x+w])
            cv2.imshow('image', img)
        if cv2.waitKey(100) & 0xFF == ord('q'):
            print('Done')
            break
        elif count >= 30:
            print('Done')
            break
    cap.release()
    cv2.destroyAllWindows()

# while True:
#     success, img = cap.read()
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     faces = face.detectMultiScale(gray, 1.1, 4)
#
#     for (x, y, w, h) in faces:
#         cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
#
#     cv2.imshow('img', img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break