print("---------------------------------------")
print("---------REBOTE DE PELOTA--------------")
print("---------------------------------------")

#INPUT
H = int(input("Ingrese el numero de rebotes: "))

#PROCESS
Q = H/5
N = 0

while H>Q:
    H = H*0.9
    N = N+1
    
#OUTPUT  
print("Rebotes que hizo la pelota: " + str(N))






