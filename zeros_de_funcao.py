#############################
#   Métodos Computacionais  #
#   Caio Eduardo Meirelles  #
#   201611310015            #
#############################

#escreve a funcao e sua derivada em um arquivo a se importar posteriormente
def write_method_func(this_function,this_derivada):
    f = open("funcao.py","w+")
    f.write('''
def funcao(x):
    return ''')
    for i in this_function:
        f.write(i)
    f.write('\n')
    f.write('''
def derivada(x):
    return ''')
    f.write(this_derivada)
    f.write('\n')
    return

#le a funcao, transforma em codigo python e a deriva
def export_func(operands,operators):
    aux = []
    for i in operands:
        if 'x' in i:
            if '^' in i:
                a = ("x**"+i[-1:])
                aux.append(a)
            else:
                aux2 = i.split('x')
                b = (aux2[0]+"*x")
                aux.append(b)
        else:
            aux.append(i)

    interpreted_function = []
    for i in range(len(operators)):
        interpreted_function.append(aux[i])
        interpreted_function.append(operators[i])
    interpreted_function.append(aux[len(aux)-1])
    write_method_func(interpreted_function,"teste")
    return

#separa a entrada em tokens
def write_func(func):
    symbols = []
    for i in func:
        if i == '+':
            symbols += '+'
        elif i == '-':
            symbols += '-'
    func = func.split('+')
    aux = []
    for i in func:
        aux += i.split('-')
    export_func(aux,symbols)
    return

#tira o "f(x)=" da entrada e deixa só a funcao a se interpretar
def interpret_function(f_de_x):
    aux = f_de_x.split('=')
    func = aux[1]
    write_func(func[:-1])
    return

#guarda a precisao
def interpret_precision(precision):
    aux = precision.split('=')
    return int(aux[1][:-1])

#guarda o intervalo inicial
def interpret_interval(interval):
    aux = interval.split('=')
    aux2 = aux[1].split(',')
    
    a = float(aux2[0])
    b = float(aux2[1])
    return a,b

#implementa a bisseccao
def bisseccao(a,b,precision):
    return

#implementa a posicao falsa
def pos_falsa(a,b,precision):
    return

#implementa o ponto fixo
def ponto_fixo(a,b,precision):
    return

#implementa newton-raphson
def newton_raphson(a,b,precision):
    return

#implementa o metodo da secante
def secante(a,b,precision):
    return



input = open('input.txt','r')

interpret_function(input.readline())
precisao = interpret_precision(input.readline())
a0,b0 = interpret_interval(input.readline())

input.close()

print(precision)
print(a,b)

