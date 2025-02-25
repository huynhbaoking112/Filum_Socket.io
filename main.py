from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse

app = FastAPI()

# Trang HTML đơn giản để test WebSocket
html = """
<!DOCTYPE html>
<html>
    <head>
        <title>WebSocket Test</title>
    </head>
    <body>
        <h1>WebSocket Test với FastAPI</h1>
        <input type="text" id="messageInput" placeholder="Nhập tin nhắn...">
        <button onclick="sendMessage()">Gửi</button>
        <ul id="messages"></ul>
        <script>
            var ws = new WebSocket("ws://localhost:8000/ws");
            ws.onmessage = function(event) {
                var messages = document.getElementById('messages');
                var message = document.createElement('li');
                message.textContent = event.data;
                messages.appendChild(message);
            };
            function sendMessage() {
                var input = document.getElementById("messageInput");
                ws.send(input.value);
                input.value = '';
            }
        </script>
    </body>
</html>
"""

@app.get("/")
async def get():
    return HTMLResponse(html)

# Endpoint WebSocket
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()  # Chấp nhận kết nối từ client
    try:
        while True:
            data = await websocket.receive_text()  # Nhận tin nhắn từ client
            await websocket.send_text(f"Tin nhắn từ bạn: {data}")  # Gửi lại tin nhắn
    except WebSocketDisconnect:
        print("Client đã ngắt kết nối!")
    finally:
        await websocket.close()  # Đảm bảo đóng kết nối khi xong