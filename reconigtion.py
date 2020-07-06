import sys
sys.path.insert(0, 'dao/')
sys.path.insert(0, 'utils/')
sys.path.insert(0, 'entities/')
sys.path.insert(0, 'database/')
sys.path.insert(0, 'services/')

import cv2
import pickle
import utils

faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

eyeCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
smileCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')

reconocimiento = cv2.face.LBPHFaceRecognizer_create()
reconocimiento.read("training.yml")

etiquetas = {"nombre_persona" : 1 }
with open("labels.pickle",'rb') as f:
  pre_etiquetas = pickle.load(f)
  etiquetas = { v:k for k,v in pre_etiquetas.items()}

web_cam = cv2.VideoCapture(0)

dni = ''
previous_dni = ''
while True:
  ret, marco = web_cam.read()
  grises = cv2.cvtColor(marco, cv2.COLOR_BGR2GRAY)    
  rostros = faceCascade.detectMultiScale(grises, 1.5, 5)
  finded = False
  for (x, y, w, h) in rostros:
    roi_gray = grises[y:y+h, x:x+w]
    roi_color = marco[y:y+h, x:x+w]

    id_, conf = reconocimiento.predict(roi_gray)
    if conf <= 50:
      font = cv2.FONT_HERSHEY_SIMPLEX            

      dni = etiquetas[id_]
      finded = True

      color = (255,255,255)
      grosor = 2
      cv2.putText(marco, dni, (x,y), font, 1, color, grosor, cv2.LINE_AA)

      cv2.rectangle(marco, (x, y), (x+w, y+h), (0, 255, 0), 2)

      rasgos = smileCascade.detectMultiScale(roi_gray)
      for(ex,ey,ew,eh) in rasgos:
        cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)

  marco_display = cv2.resize(marco, (1200, 650), interpolation = cv2.INTER_CUBIC)
  cv2.imshow('Detectando Rostros', marco_display)

  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

  if (finded) and  (previous_dni != dni):
    previous_dni = dni
    utils.markAttendance(dni)

web_cam.release()
cv2.destroyAllWindows()