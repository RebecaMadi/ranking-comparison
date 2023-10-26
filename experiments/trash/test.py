import matplotlib.pyplot as plt
import sys

x = [] #quantidade
y = [] #tamanho

x2 = []
y2 = []

body_sizes = []

def readFile():
    with open("data/body_sizes.txt", "r") as bs:
        lines = (bs.readlines())
        for line in lines:
            body_sizes.append(int(line))

def repeat(list, value):
    cont = 0
    for i in list:
        if i == value:
            cont += 1
    return cont

def format_bytes(value):
    cont = 0
    while value > 1024:
        value = value/1024.00
        cont += 1
    
    if cont == 0: return str(value) + " bytes"
    elif cont == 1: return str(value) + " kb"
    elif cont == 2: return str(value) + " Mb"
    elif cont == 3: return str(value) + " Gb"
    elif cont == 4: return str(value) + " Tb"
    else: return str(value) + " Out"


def defineXY():
    body_sizes.sort()
    for i in body_sizes:
        if i not in y:
            k = format_bytes(i)
            y.append(k)
            x.append(repeat(body_sizes, i))
    
def defineXY_2(q):
    q.sort()
    for i in q:
        if i not in y2:
            k = i/1024
            y2.append(k)
            x.append(repeat(body_sizes, i))

def total_memory():
    memoria_total = 0
    for i in body_sizes:
        memoria_total += i
    return memoria_total

def less_than(size):
    cont = 0
    for i in body_sizes:
        if i <= size:
            cont += 1
    return cont

def less_than_size(size):
    cont = 0
    for i in body_sizes:
        if i <= size:
            cont += i
    return cont

def more_than_size(size):
    cont = 0
    for i in body_sizes:
        if i > size:
            cont += i
    return cont

def more_than(size):
    cont = 0
    for i in body_sizes:
        if i > size:
            cont += 1
    return cont

#readFile()
#defineXY()

def plot_graphicTQ():
    readFile()
    defineXY()
    plt.plot(x, y)
    plt.ylabel('Eixo Tamanho')
    plt.xlabel('Eixo Quantidade')
    plt.title('Gráfico de quantidade X tamanho')
    plt.show()

def plot_graphicTQ_2():
    readFile()
    y = ["100 bytes", "500 bytes", "1kb", "10kb", "100kb", "500kb", "1Mb", "10Mb"]
    y2 = [100, 500, 1024, 10240, 102400, 512000, 1048576, 10485760]
    for i in range(8):
        x.append(less_than(y2[i]))
    i = 7
    while i>0:
         x[i] = x[i] - x[i-1]
         i = i -1

    plt.plot(y, x)
    plt.xlabel('Eixo Tamanho')
    plt.ylabel('Eixo Quantidade')
    plt.title('Gráfico de quantidade X tamanho')
    plt.show()

def plot_graphicsP(memoria_total):
    y = ["100 bytes", "500 bytes", "1kb", "10kb", "100kb", "500kb", "1Mb", "10Mb"]
    y2 = [100, 500, 1024, 10240, 102400, 512000, 1048576, 10485760]
    for i in range(8):
        x2.append(less_than_size(y2[i]))
    #x2.append(more_than_size(y2[7]))
    i = 7
    while i>0:
         x2[i] = x2[i] - x2[i-1]
         i = i -1
    for i in range(len(x2)):
        x2[i] = (x2[i]/memoria_total)*100

    print(memoria_total)
    print(x2)
    plt.plot(y, x2)
    plt.xlabel('Eixo Tamanho')
    plt.ylabel('Eixo Porcentagem em relação a memória total')
    plt.title('Gráfico de tamanho X porcentagem')
    plt.show()


def plot_graphics():
    #plot_graphicTQ_2()
    #readFile()
    #memoria_total = total_memory()
    #plot_graphicsP(memoria_total)
    p = "nao sei aaaa"
    print(p.encode('utf-8'))
    s = len(p.encode('utf-8'))
    s2 = sys.getsizeof(p)
    if s < 5:
        t = p
    else:
        t = p[0:5]

    print(p)
    print(s)
    print(s2)
    print(t)
    test_string = "geekforgeeks"
    print("The original string : " + str(test_string)) 
    res = sys.getsizeof(test_string) 
      
    print("The length of string in bytes : " + str(res))

plot_graphics()
    
