f = open('coordenadas.txt', 'r')
x,y = zip(*[l.split(', ') for l in f]) #Aqui ele lê em string
f.close()

#Remove amostras anteriores à posição 24
x = x[24:]
y = y[24:]

x0 = float(x[0])

x = [float(xi)-x0 for xi in x] #subtrai o tempo de todas as amostras pelo tempo da primeira
y = [int(yi[:-3])-353 for yi in y] #Subtrai a posição pela posição de repouso do pêndulo


f = open('coordenadasAjustado.txt', 'w')
for xi, yi in zip(x,y):
    f.write(str(xi)+' '+str(yi)+'\n')
f.close()
