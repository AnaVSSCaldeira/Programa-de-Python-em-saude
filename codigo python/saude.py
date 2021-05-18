def verificacod(C,LISTAC):
    erro=1
    if len(LISTAC)>0:
        while erro>0:
            erro=0
            for i in range(0,len(LISTAC)):
                if (C<1 or C>1000) or C==LISTAC[i]:
                    print('\nCodigos ja inseridos:',LISTAC,)
                    C=int(input('Codigo invalido tente um numero entre 1 e 1000 e diferente dos ja colocados: '))
                    erro+=1
    else:
        while C<1 or C>1000:
            C=int(input('Codigo invalido tente um numero entre 1 e 1000: '))
    
    print('Codigo validado, pode prosseguir')
    return C

def taxadoencas(x,y,z,EX,EY,EZ):#verificando a taxa e se esta doente ou nao
    while x<0 or x>100:
        x=int(input('Taxa da doenca X digitada invalidada, digite um numero entre 1 e 100: '))
        if x<30 or x>50:
            EX=1
            print(EX)
        else:
            EX=0    
    while y<-10 or y>10:
        y=int(input('Taxa da doenca Y digitada invalidada, digite um numero entre -10 e 10: '))
        if y<3 or y>7:
            EY=1    
        else:
            EY=0 
    while z<5000 or z>10000:
        z=int(input('Taxa da doenca Z digitada invalidada, digite um numero entre 5000 e 10000: '))
        if z<6500 or z>8000:
            EZ=1    
        else:
            EZ=0
    if x<30 or x>50:
        EX=1
    else:
        EX=0  
    if y<3 or y>7:
         EY=1    
    else:
        EY=0
    if z<6500 or z>8000:
        EZ=1    
    else:
        EZ=0

    if EX+EY+EZ==1:
        return 'Pouco grave'
    elif EX+EY+EZ==2:
        return 'Grave'
    elif EX+EY+EZ==3:
        return 'Muito grave'
    else:
        return 'Saudavel'

continuar='s' #se o paciente quer continuar ou não
pacientes=[] #lista de nomes dos pacientes
codigos=[] #lista dos codigos dos pacientes
estado=[] #estado do paciente, pode ser pouco grave, grave, muito grave ou saudavel
i=0 #posicao do paciente
contMG,contG,contPG,contS=0,0,0,0
pessoas=0 #quantidade de pessoas

while continuar=='s':
    estadoX,estadoY,estadoZ=0,0,0 #flag->1:tem doenca/0:nao tem doenca
    contdoenca=0
    pessoas+=1
    nome=input('Digite seu nome: ')
    pacientes.append(nome) #nome da pessoa

    cod=int(input('Agora digite seu codigo(entre 1 e 1000): '))
    cod=verificacod(cod,codigos) #verifica o codigo
    codigos.append(cod) #coloca o codigo dela

    X=int(input('Digite a taxa da doenca X(entre 0 e 100): '))
    Y=int(input('Digite a taxa da doenca Y(entre -10 e 10): '))
    Z=int(input('Digite a taxa da doenca Z(entre 5000 e 10000): '))
    estado.append(taxadoencas(X,Y,Z,estadoX,estadoY,estadoZ))#taxa das doencas e analise da situacao do paciente
    if estado[i]=='Saudavel':
        contS+=1
    elif estado[i]=="Pouco grave":
        contPG+=1
    elif estado[i]=='Grave':
        contG+=1
    elif estado[i]=="Muito grave":
        contMG+=1
    i+=1
    continuar=input('Deseja continuar? (s/n): ')

print('\n\nLista de pacientes:')
for i in range(0,pessoas): #mostra os pacientes
    print('Paciente:',pacientes[i],'\nCodigo:',codigos[i],'\nSituação:',estado[i])
    print('(',i+1,'/',pessoas,')\n')

print('\nRelatorio Final:') #Mostrando numero de pessoas em relacao a condicao
print('Pessoas com estado MUITO GRAVE:',contMG)
print('Pessoas com estado GRAVE:',contG)
print('Pessoas com estado POUCO GRAVE:',contPG)
print('Pessoas com estado SAUDAVEL:',contS)
print('\nPacientes MUITO GRAVES:')
for i in range(0,pessoas):
    if estado[i]=="Muito grave":
        print('Paciente:',pacientes[i],'\nCodigo:',codigos[i],)
print('\nPacientes GRAVES:')
for i in range(0,pessoas):
    if estado[i]=='Grave':
        print('Paciente:',pacientes[i],'\nCodigo:',codigos[i],)
print('\nPacientes POUCO GRAVES:')
for i in range(0,pessoas):
    if estado[i]=="Pouco grave":
        print('Paciente:',pacientes[i],'\nCodigo:',codigos[i],)
print('\nPacientes SAUDAVEIS:')
for i in range(0,pessoas):
    if estado[i]=='Saudavel':
        print('Paciente:',pacientes[i],'\nCodigo:',codigos[i],)