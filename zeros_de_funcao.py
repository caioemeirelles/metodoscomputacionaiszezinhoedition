#############################
#   Métodos Computacionais  #
#   Caio Eduardo Meirelles  #
#   201611310015            #
#############################


########## METODOS PRE PROCESSAMENTO E LIDAR COM ENTRADA #######################

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
    for i in this_derivada:
        f.write(i)
    f.write('\n')
    return

#le a funcao, transforma em codigo python e a deriva
def export_func(operands,operators):
    aux = []
    aux_deriv = []
    coef = []
    exp = []
    for i in operands:
        if 'x' in i:
            if '^' in i:
                coef.append(i.split("x^")[0])
                exp.append(i.split("x^")[1])

                if coef[len(coef)-1] == "":
                    a = ("x**"+exp[len(coef)-1])
                    b = (exp[len(coef)-1]+"*x**("+exp[len(coef)-1]+"-1)")
                else:
                    a = (coef[len(coef)-1]+"*x**"+exp[len(coef)-1])
                    b = (exp[len(coef)-1]+"*"+coef[len(coef)-1]+"*x**("+exp[len(coef)-1]+"-1)")
                aux.append(a)
                aux_deriv.append(b)

            else:
                aux2 = i.split('x')
                b = (aux2[0]+"*x")
                aux.append(b)
                aux_deriv.append(aux2[0])
        else:
            aux.append(i)
            aux_deriv.append("")

    interpreted_function = []
    interpreted_deriv = []
    for i in range(len(operators)):
        interpreted_function.append(aux[i])
        interpreted_function.append(operators[i])

        interpreted_deriv.append(aux_deriv[i])
        if not aux_deriv[i+1] == "":
            interpreted_deriv.append(operators[i])

    interpreted_function.append(aux[len(aux)-1])
    interpreted_deriv.append(aux_deriv[len(aux_deriv)-1])
    write_method_func(interpreted_function,interpreted_deriv)
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

################ FIM METODOS PRE PROCESSAMENTO E LIDAR COM ENTRADA ###############

############ EXECUTA PRE PROCESSAMENTO #####################
input = open('input.txt','r')

interpret_function(input.readline())
precisao = interpret_precision(input.readline())
a0,b0 = interpret_interval(input.readline())

input.close()

import funcao as fun
############ FIM EXECUTA PRE PROCESSAMENTO ################


############## IMPLEMENTA MÉTODOS NUMERICOS #################
#implementa a bisseccao
def erro_bisseccao(a,b,fx):
    return min(abs(a+b)/2,abs(fx))

def bisseccao(a,b,precision):
    fa = fun.funcao(a)
    fb = fun.funcao(b)
    x = (a+b)/2.
    fx = fun.funcao(x)
    xizes = [x]
    fxizes = [fx]
    prec = 10**(-precision)
    iteracoes = 0
    erro = erro_bisseccao(a,b,fx)
    while erro > prec or iteracoes > 1000:
        iteracoes += 1
        if fx == 0:
            erro = 0
            return xizes,fxizes,x,fx,erro,iteracoes
        elif fx*fa < 0:
            b = x
            x = (a+b)/2
            fx = fun.funcao(x)
        else:
            a = x
            x = (a+b)/2
            fx = fun.funcao(x)
        xizes.append(x)
        fxizes.append(fx)
        erro = erro_bisseccao(a,b,fx)

    return xizes,fxizes,x,fx,erro,iteracoes

#implementa a posicao falsa
def erro_pos_falsa(a,b,fx):
    return min(abs(a-b),abs(fx))

def pos_falsa(a,b,precision):
    fa = fun.funcao(a)
    fb = fun.funcao(b)
    x = (a*fb - b*fa)/(fb - fa)
    fx = fun.funcao(x)
    xizes = [x]
    fxizes = [fx]
    prec = 10**(-precision)
    iteracoes = 0
    erro = erro_pos_falsa(a,b,fx)

    while erro > prec and iteracoes < 1000:
        iteracoes += 1
        if fx == 0:
            erro = 0
            return xizes,fxizes,x,fx,erro,iteracoes
        elif fx*fa < 0:
            b = x
            x = (a*fb - b*fa)/(fb - fa)
            fx = fun.funcao(x)
        else:
            a = x
            x = (a*fb - b*fa)/(fb - fa)
            fx = fun.funcao(x)
        xizes.append(x)
        fxizes.append(fx)
        erro = erro_pos_falsa(a,b,fx)

    return xizes,fxizes,x,fx,erro,iteracoes

#implementa o ponto fixo #TODO
def ponto_fixo(a,b,precision):
    x = (a+b)/2.
    fx = fun.funcao(x)
    xizes = [x]
    fxizes = [fx]
    prec = 10**(-precision)
    iteracoes = 0
    erro = erro_bisseccao(a,b,fx)
    return xizes,fxizes,x,fx,erro,iteracoes

#implementa newton-raphson
def erro_newton(x,x1,fx):
    return min(abs((x1-x)/x1),abs(fx))

def newton_raphson(x,precision):
    fx = fun.funcao(x)
    flx = fun.derivada(x)
    x1 = x - fx/flx
    xizes = [x]
    fxizes = [fx]
    prec = 10**(-precision)
    iteracoes = 0
    erro = erro_newton(x,x1,fx)

    while erro > prec and iteracoes < 1000:
        iteracoes += 1
        x = x1
        fx = fun.funcao(x)
        flx = fun.derivada(x)
        x1 = x - fx/flx
        xizes.append(x)
        fxizes.append(fx)
        erro = erro_newton(x,x1,fx)

    return xizes,fxizes,x,fx,erro,iteracoes

#implementa o metodo da secante
def erro_secante(x,x1,fx):
    return min( abs(x1-x), abs(fx) )

def secante(a,b,precision):
    x = a
    x1 = b
    fx = fun.funcao(x)
    fx1 = fun.funcao(x1)
    x2 = ( (x*fx1 - x1*fx)/(fx1 - fx) )
    xizes = [x,x1]
    fxizes = [fx,fx1]
    iteracoes = 0
    prec = 10**(-precision)
    erro = erro_secante(x,x1,fx)

    while erro > prec and iteracoes < 1000:
        iteracoes += 1
        x = x1
        x1 = x2
        fx = fun.funcao(x)
        fx1 = fun.funcao(x1)
        x2 = ( (x*fx1 - x1*fx)/(fx1 - fx) )
        xizes.append(x1)
        fxizes.append(fx1)
        erro = erro_secante(x,x1,fx1)

    return xizes,fxizes,x,fx,erro,iteracoes

########## FIM IMPLEMENTA METODOS NUMERICOS #################################


############## IMPLEMENTA SAIDA FORMATADA #########################
def saida(f,out1,out2,out3,out4,out5,out6):
    f.write('<x>=')
    for i in range(len(out1)):
        f.write(str(out1[i]))
        if i < len(out1)-1:
            f.write(',')
    f.write('''
<fx>=''')
    for i in range(len(out2)):
        f.write(str(out2[i]))
        if i < len(out2)-1:
            f.write(',')
    f.write('''
x=''')
    f.write(str(aux3))
    f.write('''
f(x)=''')
    f.write(str(aux4))
    f.write('''
errx=''')
    f.write(str(aux5))
    f.write('''
iter=''')
    f.write(str(aux6))

    return

########## FIM IMPLEMENTA SAÍDA FORMATADA ###################

f = open("output.txt","w+")

#executa bisseccao
aux1,aux2,aux3,aux4,aux5,aux6 = (bisseccao(a0,b0,precisao))
f.write('''Metodo da Bisseccao:
''')
saida(f,aux1,aux2,aux3,aux4,aux5,aux6)
f.write('''

''')

#executa posicao falsa
aux1,aux2,aux3,aux4,aux5,aux6 = (pos_falsa(a0,b0,precisao))
f.write('''Metodo da Posicao Falsa:
''')
saida(f,aux1,aux2,aux3,aux4,aux5,aux6)
f.write('''

''')

#executa ponto fixo
aux1,aux2,aux3,aux4,aux5,aux6 = (newton_raphson((a0+b0)/2,precisao)) ##o método de Newton-Raphson é um caso particular do pto fixo
f.write('''Metodo do Ponto Fixo:
''')
saida(f,aux1,aux2,aux3,aux4,aux5,aux6)
f.write('''

''')

#executa newton-raphson
aux1,aux2,aux3,aux4,aux5,aux6 = (newton_raphson((a0+b0)/2,precisao))
f.write('''Metodo de Newton-Raphson:
''')
saida(f,aux1,aux2,aux3,aux4,aux5,aux6)
f.write('''

''')

#executa secante
aux1,aux2,aux3,aux4,aux5,aux6 = (secante(a0,b0,precisao))
f.write('''Metodo da Secante:
''')
saida(f,aux1,aux2,aux3,aux4,aux5,aux6)


f.close()