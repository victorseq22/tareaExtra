list = [1,2,3,4,5]
print ("El resultaod es :",sum(list))

print ()

def multiplicador (numeros):
    producto = 1

    for n in numeros:
        producto *= n

    return producto

list = [1,2,3,4,5]
print(type(list))
print("El resultaod es :", multiplicador(list)) 
