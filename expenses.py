
expenses = [10.50, 8, 5, 15, 20, 5, 3]

sum = 0

for x in expenses:
    sum = sum + x

#print ("Your expenses are " + str(sum))
print ("Your expenses are $", sum) # esta forma es la misma q la de arriba pero sin tener que comvertir sum a string

print ("Your expenses are $", sum, sep = '') # esta es la forma de especificar el separador, en este caso eliminamos el espacio que es el separador por defecto

