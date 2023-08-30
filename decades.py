age = int(input("How old are you?\n"))

# decades = int(age/10)
decades = age // 10 # doble slash es lo mismo que indicar que sólo quieres la parte entera de la división

years = age % 10 # devuelve el módulo de la división, el resto.

print("You are " + str(decades) + " decades and " + str(years) + " years old.")
