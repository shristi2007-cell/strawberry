import matplotlib.pyplot as plt
x=[1,2,3,4,5,6,7,8,9,10]
y=[1,1,2,3,5,8,13,21,34,55]   #fibonacci
ye=[2,4,6,8,10,12,14,16,18,20]
yo=[1,3,5,7,9,11,13,15,17,19]
yp=[2,3,5,7,11,13,17,19,23,29]

plt.plot(x,y,color='r',label='fibonacci')
plt.plot(x,ye,color='b',label='even')
plt.plot(x,yo,color='y',label='odd',)
plt.plot(x,yp,color='black',label='prime')
plt.legend()
plt.show()