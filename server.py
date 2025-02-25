import socket
#server.py

host = "localhost"
port = 4000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))

s.listen(2)
print("Server listening on port", port)

c, addr = s.accept()
print("Connect from", str(addr))

# Nhận tên file do client gửi tới 
filename = c.recv(1024)

try:
    f = open(filename, 'rb')
    content = f.read()

    # Gửi dữ liêụ trong file cho client 
    c.send(content)
    f.close()
except FileExistsError:
    c.send("File not found")
except FileNotFoundError:
    c.send("File not found 2")
c.close()