import cv2
import pickle

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

finded = False
nombre = ""
while not finded:
  ret, marco = web_cam.read()
  grises = cv2.cvtColor(marco, cv2.COLOR_BGR2GRAY)    
  rostros = faceCascade.detectMultiScale(grises, 1.5, 5)

  for (x, y, w, h) in rostros:
    roi_gray = grises[y:y+h, x:x+w]
    roi_color = marco[y:y+h, x:x+w]

    id_, conf = reconocimiento.predict(roi_gray)
    if conf >= 4  and conf < 85:
      font = cv2.FONT_HERSHEY_SIMPLEX            

      nombre = etiquetas[id_]
      

      if conf > 50:
        nombre = "Desconocido"
      

      color = (255,255,255)
      grosor = 2
      cv2.putText(marco, nombre, (x,y), font, 1, color, grosor, cv2.LINE_AA)

      # img_item = "my-image.png"
      # cv2.imwrite(img_item, roi_gray)
      
      cv2.rectangle(marco, (x, y), (x+w, y+h), (0, 255, 0), 2)

      rasgos = smileCascade.detectMultiScale(roi_gray)
      for(ex,ey,ew,eh) in rasgos:
        cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)
      finded = True

  marco_display = cv2.resize(marco, (1200, 650), interpolation = cv2.INTER_CUBIC)
  cv2.imshow('Detectando Rostros', marco_display)

  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

print(f'Bienvenido {nombre}')

web_cam.release()
cv2.destroyAllWindows()