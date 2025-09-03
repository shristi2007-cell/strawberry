import matplotlib.pyplot as plt

x=['Sun','Mon','Tue','Wed','Thu', 'Fri', 'Sat']
y=[3,2,1,3,2,3,2]


plt.plot(x,y, marker='o',linestyle='--',color='b',label='Kati thaal Bhaat?')

plt.xlabel('Days')
plt.ylabel('Thaal Bhaat')
plt.title('Harek din kati thaal Bhaat?')
plt.legend()
plt.show()

