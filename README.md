# Facial Recognition

Repositório destinado ao projeto SmartDoor do grupo 9 da disciplina de  Projeto Integrador 2 da UnB-FGA (2020/2).

Este projeto utiliza a biblioteca [face_recognition](https://github.com/ageitgey/face_recognition) para realizar o reconhecimento facial na Raspberry Pi.

## Exemplo de Funcionamento

O gif abaixo demonstra o funcionamento do reconhecimento facial (atuando em um Raspberry Pi):

![exemplo2](./images/exemplo.gif)

## Instalação (Raspberry Pi 4+)

1. Instale as seguintes dependências (uma de cada vez):

```
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install build-essential
sudo apt-get install cmake
sudo apt-get install gfortran
sudo apt-get install git
sudo apt-get install wget
sudo apt-get install curl
sudo apt-get install graphicsmagick
sudo apt-get install libgraphicsmagick1-dev
sudo apt-get install libatlas-base-dev
sudo apt-get install libavcodec-dev
sudo apt-get install libavformat-dev
sudo apt-get install libboost-all-dev
sudo apt-get install libgtk2.0-dev
sudo apt-get install libjpeg-dev
sudo apt-get install liblapack-dev
sudo apt-get install libswscale-dev
sudo apt-get install pkg-config
sudo apt-get install python3-dev
sudo apt-get install python3-numpy
sudo apt-get install python3-pip
sudo apt-get install zip
sudo apt-get clean
```

2. Instale as dependências:

```
sudo apt-get install python3-picamera
sudo pip3 install --upgrade picamera[array]
```

3. Aumente o SWAP FILE:

```
sudo nano /etc/dphys-swapfile
```

Change `CONF_SWAPSIZE=100` to `CONF_SWAPSIZE=1024` and save / exit nano

4. Clone e instale a biblioteca `dlib`:

```
mkdir -p dlib
git clone -b 'v19.6' --single-branch https://github.com davisking/dlib.git dlib/
cd ./dlib
sudo apt-get install cmake
mkdir build; cd build; cmake .. ; cmake --build 
```

Instale `dlib` com o `pip3`:

```
pip3 install dlib
```

5. Diminua o SWAP FILE:

```
sudo nano /etc/dphys-swapfile
```

Change `CONF_SWAPSIZE=1024` to `CONF_SWAPSIZE=100` and save / exit nano

6. Instalar biblioteca de suporte ao `dlib`:

```
pip3 install numpy
pip3 install scikit-image
sudo apt-get install python3-scipy
sudo apt-get install libatlas-base-dev
sudo apt-get install libjasper-dev
sudo apt-get install libqtgui4
sudo apt-get install python3-pyqt5
sudo apt install libqt4-test
pip3 install opencv-python==3.4.6.27
pip3 install face_recognition 
```

7. Clone este repositório e rode o script `facial_recognition.py`:

```
python3 facial_recognition.py
```

## Créditos
* [face_recognition](https://github.com/ageitgey/face_recognition)
* [sbuildsio](https://smartbuilds.io/installing-face-recognition-library-on-raspberry-pi-4/)
* [EbenKouao](https://www.youtube.com/watch?v=6nY-V_WG7oI&ab_channel=EbenKouao)
* [OpenCV](https://opencv.org/)