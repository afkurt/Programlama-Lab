"""
Created on Sat Apr 20 16:50:46 2020
@author: Ahmet Furkan Kurt 170401002

https://github.com/afkurt/Programlama-Lab/blob/master/ODEV%203

"""


from sympy import Symbol,pprint
import sympy as sym
import sympy.plotting as syp
import matplotlib.pyplot as plt

x = Symbol('x')# x istenilen olasılık adedi
lamda=Symbol('lambda')#lamda sürecin verilen ortalama değeri

part_1= ((lamda**x)*sym.exp(-lamda))
part_2=sym.factorial(x)

olasilik = part_1/part_2#Olasıllığın hesaplandığı formül.
pprint(olasilik)

syp.plot(olasilik.subs({lamda:5}),(x,0,10),title="Poisson Distribution")
plt.show() # Sympy sayesinde çizilen grafik

x_value=[]
y_value=[]
for value in range(12):
    y=olasilik.subs({lamda:5,x:value}).evalf()
    y_value.append(y)#Listeye alma işlemi
    x_value.append(value)
plt.plot(x_value,y_value)
plt.show()#Matplotlib yöntemiyle çıktı veren grafik:
