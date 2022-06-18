# this project is a test of system of inventaries

print("Hola mundo!")
print("Inventario")
articulo = input("Ingresa el producto a buscar en la lista de inventario: ")
inventario = {"Huevos":30,"Leche":40,"Avena":50,"Chocolate":{"Chocolate blanco":10,"Chocolate negro":20,},"Braunis":50,"mani dulce":20,"atun":100,"sardinas":75,}

'''Al crear la variable 'num_inv', le estoy asignando que con 'get' busque dentro del diccionario 'inventario'
si existe el articulo ingresado dende el imput y si existe lo asigne dentro de la variable 'num_inv' y si no
existe dicho articulo, asigne el valor cero a la variable'''

num_inv= inventario.get(articulo,0)
print(f"{articulo}: {num_inv}")

# Create by Jhosua Rengel

print("Porcentage of discount to client frequent")
client = input("Name of client:")
porcentage = {"Luis Jimenez":20,"Fernanda Arevalo":50,"Alejandra Velazques":70,}
discount= porcentage.get(client,"Client not is frequent")
print(f"{client} : {discount}")