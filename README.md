# 🔧 ¿Como Usarlo?

<p align="center">
     CMD
</p>

```py
pip install socket
```

<p align="center">
     ARCHIVO
</p>

```py
import socket #importe en el archivo
```
# 💻 Código
[ip-hostname](https://github.com/Pandaxyz-xd/ip-hostname/edit/main/ip-hostname.py)
```py
import socket

hostname = socket.gethostname () #Hostname = Nombre de PC
ip = socket.gethostbyname (hostname) #IP = Dirección ip

print("(Dirección IP) = " + ip) #Muestra la dirección ip
print("(Nombre de tu Dispositivo) = " + hostname) #Muestra el nombre del pc
```
# 📸 Resultado
![Resultado](https://i.imgur.com/ynrjiRF.png)
