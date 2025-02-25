# import socket
# #server.py

# host = "localhost"
# port = 4000
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.bind((host, port))

# s.listen(2)
# print("Server listening on port", port)

# c, addr = s.accept()
# print("Connect from", str(addr))

# # Nhận tên file do client gửi tới 
# filename = c.recv(1024)

# try:
#     f = open(filename, 'rb')
#     content = f.read()

#     # Gửi dữ liêụ trong file cho client 
#     c.send(content)
#     f.close()
# except FileExistsError:
#     c.send("File not found")
# except FileNotFoundError:
#     c.send("File not found 2")
# c.close()


import socket

# Cấu hình server
host = "localhost"
port = 4000

# Tạo socket server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(2)  # Cho phép tối đa 2 kết nối chờ trong hàng đợi
print(f"Server đang lắng nghe tại {host}:{port}")

# Vòng lặp chính để server chạy liên tục
while True:
    print("Đang chờ kết nối từ client...")
    c, addr = s.accept()  # Chấp nhận kết nối từ client
    print(f"Kết nối từ {addr}")

    try:
        # Nhận tên file từ client
        filename = c.recv(1024).decode()  # Giải mã bytes thành string
        print(f"Client yêu cầu file: {filename}")

        # Mở và đọc file
        with open(filename, 'rb') as f:  # Dùng 'with' để tự động đóng file
            content = f.read()
            c.send(content)  # Gửi nội dung file cho client
            print(f"Đã gửi nội dung của {filename} cho client.")

    except FileNotFoundError:
        error_msg = "File not found"
        c.send(error_msg.encode())  # Gửi thông báo lỗi nếu file không tồn tại
        print(f"Không tìm thấy file: {filename}")
    except Exception as e:
        error_msg = f"Lỗi: {str(e)}"
        c.send(error_msg.encode())  # Xử lý lỗi bất ngờ khác
        print(f"Lỗi xảy ra: {e}")

    finally:
        c.close()  # Đóng kết nối với client hiện tại
        print(f"Đã đóng kết nối với {addr}")

# s.close() không cần thiết vì server chạy vô hạn