

with open('D:\Class_IIMS_Year1\Python\Script\file_reading','r') as f:
    line1=f.readline()
    line2=f.readline()
    print(line2)
    print(line1)

#for reading 100 lines you have to print 100 times 

#alt
with open('D:\Class_IIMS_Year1\Python\Script\file_reading','r') as f:
    for x in f:
        print(x)

with open('D:\Class_IIMS_Year1\Python\Script\file_reading','r') as f:
    lines=f.readlines()
    print(lines)

with open('D:\Class_IIMS_Year1\Python\Script\file_reading','a') as f:
    lines=f.writelines()
    print(lines)