import face_recognition
import cv2
import numpy as np
import requests
import json
from PIL import Image

# Definir URL da API
url = 'http://25.94.11.255:8000/photos/'

# Request para obter nomes e imagens dos usuários cadastrados
response = requests.get(url)
response_json = json.loads(response.text)

# Transformar o JSON em list de nomes e imagens
names = list(map(lambda obj: obj['name'], response_json))
imagesUrl = list(map(lambda obj: obj['image'], response_json))
images = list(map(lambda url: Image.open(requests.get(url, stream=True).raw), imagesUrl))

# Transformar array de imagens PIL para numpy array
numpy_images = list(map(lambda image: np.array(image), images))

# Referência da câmera utilizada
video_capture = cv2.VideoCapture(0)

# Listas de codificação da face e de nomes correspondentes
known_face_encodings = list(map(lambda image: face_recognition.face_encodings(image)[0], numpy_images))
known_face_names = names

# Inicializa variáveis que serão utilizadas
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

while True:
    # Captura o frame do video
    ret, frame = video_capture.read()

    # Reduz o frame do vídeo para um quarto do tamanho original (para questões de otimização)
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # Converte a imagem de BGR (utilizado pelo OpenCV) para RGB (utilizado pela biblioteca face_recognition)
    rgb_small_frame = small_frame[:, :, ::-1]

    # Processar quadro alternados para economizat tempo
    if process_this_frame:
        # Localizar face e codificações de faces no frame do vídeo atual
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            # Verifica se o rosto encontrado é igual a um dos rostos pré existentes
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Desconhecido"

            # Utiliza o rosto mais parecido
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]

            face_names.append(name)

    process_this_frame = not process_this_frame


    # Mostra os resultados
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Escala o rosto para o tamanho original (antes estava em 1/4 do tamanho)
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Define a cor de acordo com o reconhecimento
        color = (0, 0, 255) if name == "Desconhecido" else (0, 255, 0)
        
        # Desenha um quadrado no rosto da pessoa
        cv2.rectangle(frame, (left, top), (right, bottom), color, 2)

        # Escreve um texto (nome) abaixo no rosto
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), color, cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    # Mostra o resultado
    cv2.imshow('Video', frame)

    # (Opcional) Apertar 'q' no teclado para sair
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Abre a webcam
video_capture.release()
cv2.destroyAllWindows()
