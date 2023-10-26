import matplotlib.pyplot as plt

x = [] #quantidade
y = [] #tamanho

body_sizes = []

def readFile():
    with open("data/bs_babs.txt", "r") as bs:
        lines = (bs.readlines())
        for line in lines:
            body_sizes.append(int(line))

def less_than(size):
    cont = 0
    for i in body_sizes:
        if i <= size:
            cont += 1
    return cont

def graphic():
    readFile()
    y = ["100 bytes", "500 bytes", "1kb", "10kb", "100kb", "500kb", "1Mb"]
    y2 = [100, 500, 1024, 10240, 102400, 512000, 1048576]
    for i in range(7):
        x.append(less_than(y2[i]))
    
    plt.plot(y, x)
    plt.xlabel('Tamanho')
    plt.ylabel('Quantidade')
    plt.title('Gráfico de quantidade X tamanho')
    plt.show()

graphic()