import socket 
# client.py

# Như mình đã nói ở trên thì chúng ta không truyền tham số vào vẫn ok
s = socket.socket()
s.connect(("localhost", 4000)) 


# Nhập vào tên file 
filename = input("Enter a filename")

# Gửi tên file cho server
s.send(filename.encode())

# 1024 là số bytes mà client có thể nhận được trong 1 lần
# Phần tin nhắn đầu tiên
content = s.recv(1024)

print(content.decode())

s.close()