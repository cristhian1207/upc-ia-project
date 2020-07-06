
import sys
sys.path.insert(0, 'dao/')
sys.path.insert(0, 'utils/')
sys.path.insert(0, 'entities/')
sys.path.insert(0, 'database/')
sys.path.insert(0, 'services/')

import cv2
import os
import utils

dni = utils.createUser()

if not os.path.exists('./images'):
  os.makedirs('./images')
if not os.path.exists(f'./images/{dni}'):
  os.makedirs(f'./images/{dni}')

web_cam = cv2.VideoCapture(0)
faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

count = 0

while 1:
  _, image_window = web_cam.read()

  grays = cv2.cvtColor(image_window, cv2.COLOR_BGR2GRAY)
  face = faceCascade.detectMultiScale(grays, 1.5, 5)

  for (x, y, w, h) in face:
    cv2.rectangle(image_window, (x,y), (x+w, y+h), (255,0,0), 4)
    count += 1

    cv2.imwrite(f'images/{dni}/{dni}_{count}.jpg', grays[y:y+h, x:x+w])
    cv2.imshow("Creando Dataset", image_window)

  if cv2.waitKey(1) & 0xFF == ord('q'):
    break
  elif count >= 400:
    break

web_cam.release()
cv2.destroyAllWindows()