nombre = input("ingresa tu nombre: ")
apellido = input("ingresa tu apellido: ")
edad = input("cual es tu edad: ")
correo_electronico_o_Gmail = input("indique su correo electronico: ")

edad = int(edad)

print("-hola, " , apellido, nombre)
print("-tienes " , edad, " años")
print("-tu dirección de correo electrónico es: " , correo_electronico_o_Gmail)

if edad < 18:
    print("error: necesitas ser mayor de edad para continuar")

if edad > 110:
    print("error: edad no valida")

if nombre == "" or apellido == "" or edad == "" or correo_electronico_o_Gmail == "":
    print("Error: se requiere que todos los campos sean completados")
