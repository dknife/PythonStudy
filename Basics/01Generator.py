import matplotlib.pyplot as plt
import math

def sinValue(max) :
       angle = 0
       while angle < max:
              angle+= 0.01
              yield math.sin(angle)

def cosValue(max):
       angle = 0
       while angle < max:
              angle += 0.01
              yield math.acos(math.fabs(angle)/7.28)

fList = []

fList = list(sinValue(6.28))
plt.plot(fList)
fList = list(cosValue(6.28))
plt.plot(fList)
plt.show()
