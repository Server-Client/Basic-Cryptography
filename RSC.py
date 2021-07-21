x = input('Type String Here: ')
y = input('Character to Replace & Character to Replace with (ex: e,r): ')
z = y.strip().replace(',', '')
print(z)
a,b = z
print(x.replace(a, b))
