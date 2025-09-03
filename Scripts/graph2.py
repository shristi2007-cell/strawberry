import matplotlib.pyplot as plt

x=[1,2,3,4,5]
y=[2,4,6,8,10]

plt.plot(x,y, marker='o',color='r', label='Even numbers plot')

plt.xlabel('Numbers')
plt.ylabel('Even numbers')
plt.title('even numbers plot')
plt.legend()
plt.show()
