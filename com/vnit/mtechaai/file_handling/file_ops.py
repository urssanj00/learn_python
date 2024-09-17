f = open('new.txt', 'r')

a = f.read()

print (a)

f = open('new.txt', 'w')
f.write('pyhon is important for interviews')
f.close()

f = open('new.txt', 'r')
a = f.read()
print (a)

f = open('new.txt', 'a')
f.write('\npyhon is important for data science')
f.close()

f = open('new.txt', 'r')
a = f.read()
print (a)
