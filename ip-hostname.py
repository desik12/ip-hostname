import socket

hostname = socket.gethostname () #Hostname = Nombre de PC
ip = socket.gethostbyname (hostname) #IP = Dirección ip

print("(Dirección IP) = " + ip) #Muestra la dirección ip
print("(Nombre de tu Dispositivo) = " + hostname) #Muestra el nombre del pc
