import sys
import numpy as np
import cv2
import matplotlib.pyplot as plt

cap = cv2.VideoCapture("video/pendulo.mp4")

listaCoordenadas = []

if not cap.isOpened():
    sys.exit()
while(cap.isOpened()):
    ret, frame = cap.read()
    fps = cap.get(cv2.CAP_PROP_FPS)
    if ret is False:
        break

    #Transforma a imagem em cinza
    frameGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #Borra a imagem pra remover pequenos defeitos
    frameBlur = cv2.GaussianBlur(frameGray, (9,9), 5)

    #Pega as circunferencias do frame e coloca numa lista
    circulos = cv2.HoughCircles(frameBlur,cv2.HOUGH_GRADIENT, 2,400,param1=100,param2=50,minRadius=10,maxRadius=800)
    #cv2.imshow("Cinza", frameGray)
    if circulos is not None:
        circulos = np.round(circulos[0, :]).astype("int")
        for (x,y,r) in circulos:
            if r!=0:
                #Adiciona a coordenada na lista e imprime
                listaCoordenadas.append([float(cap.get(cv2.CAP_PROP_POS_MSEC)/1000), float(x)])
                print (listaCoordenadas[-1])

                #Plotar ponto
                #plt.scatter(float(cap.get(cv2.CAP_PROP_POS_MSEC)), float(x), color='blue')
                #plt.pause(0.01)

                #Desenha onde foi encontrado
                cv2.circle(frame, (x,y), r, (0,255,0), 4)
                cv2.rectangle(frame, (x-3,y-3), (x+3,y+3), (0, 0,255), 1)

                cv2.imshow("IDENTIFICACAO DE PENDULO", frame)
                #input()
    #Fecha a aplicação com uma tecla
    if cv2.waitKey(int(20)) & 0xFF == ord('q'):
        break

#Cria o gráfico
fig = plt.figure()
fig.canvas.set_window_title('Grafico do Pendulo')
plt.title('Gráfico Pêndulo Físico')
plt.ylabel('Posição (pixel)')
plt.xlabel('Tempo(s)')

listaCoordenadas = np.array(listaCoordenadas)
plt.plot(listaCoordenadas[:,0], listaCoordenadas[:,1], "bo", markersize=3)
plt.show()

cap.release()
cv2.destroyAllWindows()
