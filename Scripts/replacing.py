#value='####HELLO#WORLD####' to output:'Hello World'


s= '####HELLO#WORLD####'

s= s.strip('#')
s=s.upper()
s = s.split('#')        #removed (bich ko # removed)
s=" ".join(',')          #',' removed and joined
print(s.title())      # made a title (output='Hello World)

