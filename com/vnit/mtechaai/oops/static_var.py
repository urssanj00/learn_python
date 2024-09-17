class test:
    x = 50

t = test()
print(t.x)
t.x = t.x +50
print(t.x)

z = test()
print(z.x)

test.x = 150

print(t.x)
print(z.x)
