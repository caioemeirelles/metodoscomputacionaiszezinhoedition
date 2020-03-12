#############################
#   Métodos Computacionais  #
#   Caio Eduardo Meirelles  #
#   201611310015            #
#############################

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

def interpret_function(f_de_x):
    aux = f_de_x.split('=')
    func = aux[1]
    write_func(func[:-1])
    return

def interpret_precision(precision):
    aux = precision.split('=')
    return int(aux[1][:-1])

def interpret_interval(interval):
    aux = interval.split('=')
    aux2 = aux[1].split(',')
    
    a = float(aux2[0])
    b = float(aux2[1])
    return a,b

def bisseccao(a,b,precision):
    return

def pos_falsa(a,b,precision):
    return

def ponto_fixo(a,b,precision):
    return

def newton_raphson(a,b,precision):
    return

def secante(a,b,precision):
    return



input = open('input.txt','r')

interpret_function(input.readline())
precisao = interpret_precision(input.readline())
a0,b0 = interpret_interval(input.readline())

input.close()

print(precision)
print(a,b)

