
#lambda è un metodo veloce di definire funzione e parametri in una sola riga
animali = ['cani', 'gatti', 'scoiattoli', 'alci']

add10 = lambda a: a + 10  #somma 10 al parametro passato a lambda
f = lambda animale: animale.capitalize() #rende maiuscolo il primo carattere della stringa passata a lambda

mymean = lambda a,b:  (a+b)/2



print(f(animali[0]))
print(add10(4))
print (mymean(3,7))
