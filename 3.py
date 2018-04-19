fo = open('helloworld.txt','w')
for i in range(10):
    fo.write("This is line %d\r\n" %(i+1))
fo.close()
fo =open('helloworld.txt','a+')
for i in range(2):
    fo.write("Appended line %d\r\n" %(i+1))
fo.close()
print (".....input what you want search.....") 
temp = input("Search you want: ")
#guess = int(temp)
def check():
        datafile = open('helloworld.txt','r')
        for line in datafile:
            if temp in line:
                return True
        return False
if check():
    print ("true")
else:
    print ("false")
