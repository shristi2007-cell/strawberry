import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[2,3,5,7,11]
xo=[1,3,5,8,10]
ye=[4,6,8,10,12]

plt.plot(x,y,marker='o',color='b',label='prime numbers plot')
plt.plot(xo,ye,marker='o',color='r',label='numbers plot')
plt.xlabel('numbers')
plt.ylabel('Prime numbers')
plt.legend()
plt.show()
