const socket = new WebSocket("ws://localhost:8765");

socket.addEventListener('open', () => {
    socket.send('Browser client connected')
})

socket.addEventListener('message', sock => {
    console.log(`Received: ${sock.data}`);
})
