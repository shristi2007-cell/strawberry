#immutable data types

s='hello'
#s[1]=H #(yesari change garna payinna type error hunxa)
#instead you can write:
s= 'H'+ s[1:5]
print(s)


#also you can replace with:

x='hello world'
print(x.replace('world','python')) #output: hello python 
