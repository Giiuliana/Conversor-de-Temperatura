
tipo= input('Digite o tipo de temperatura que voce quer converter: Celsius, Kelvin, Fahrenheit:  ')
tipo2= input('digite para qual temperatura você quer converter:')
temp= float(input('Qual a temperatura a ser convertida?'))
if tipo == 'celsius' and tipo2 =='fahrenheit':
    f= temp*1.8+32
    print('A temperatura de {}°C convertida para Fahrenheit fica {}°F'.format(temp,f))
elif tipo == 'celsius' and tipo2=='kelvin':
    k=temp*1.8+32
    print('A temperatura de {}°C convertida para Kelvin fica {}°K'.format(temp, k))
elif tipo == 'fahrenheit' and tipo2=='celsius':
    fc= (temp-32)*5/9
    print('A temperatura de {}°F convertida para Celsius fica {}°C'. format(temp, fc))
elif tipo== 'fahrenheit' and tipo2=='kelvin':
    fk= temp-32*5/9+273
    print('A temperatura de {}°F convertida para Kelvin fica {}°K'.format(temp, fk))
elif tipo== 'kelvin' and tipo2=='fahrenheit':
    kf= temp-273*1.8+32
    print('A temperatura de {}°K convertida para Fahrenheit fica {}°F'.format(temp, kf))
elif tipo==  'kelvin' and tipo2== 'celsius':
    kc= temp-273
    print('A temperatura de {}°K convertida para Celsius fica {}°C'.format(temp, kc))

else:
    print('Erro de sintaxe, digite o tipo de temperatura novamente')
return tipo









    












