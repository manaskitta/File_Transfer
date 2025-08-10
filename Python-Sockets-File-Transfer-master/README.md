# Python Socket File Transfer Project

A Python socket programming project that demonstrates client-server file transfer over TCP/IP. This project showcases basic networking concepts with simple error handling and performance monitoring.

## 🚀 Features

- **TCP Socket Communication** - Reliable data transfer between client and server
- **File Transfer** - Binary file transfer with progress tracking
- **Error Handling** - Graceful error recovery and connection management
- **Performance Monitoring** - Transfer speed and progress indicators
- **Timeout Protection** - Prevents hanging on slow connections
- **Graceful Shutdown** - Proper cleanup on server termination

## 📋 Prerequisites

- Python 3.6 or higher
- Basic understanding of networking concepts

## 🛠️ Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/manaskitta/python-socket-file-transfer.git
cd python-socket-file-transfer
```

### 2. Verify Python Installation
```bash
python --version
# or
python3 --version
```

### 3. Check Project Files
```bash
ls
# Should show: client.py, server.py, server-file.txt, README.md
```

## 🚀 How to Run

### Step 1: Start the Server
Open a terminal/command prompt and run:
```bash
python server.py
```
**Expected Output:**
```
Socket created successfully.
Server bound to port 8800
Socket is listening...
```

### Step 2: Start the Client
Open **another** terminal/command prompt and run:
```bash
python client.py
```
**Expected Output:**
```
Socket created successfully.
Connection Established.
Message sent to server
Received 1024 bytes...
File has been received successfully. Total bytes: 67
Transfer speed: 134.00 bytes/second
Connection Closed.
```

### Step 3: Check Results
- **Server terminal** will show transfer completion and speed
- **Client terminal** will show file received successfully
- **New file** `client-file.txt` will be created in the project directory

## 🔧 Configuration

### Server Settings (in `server.py`)
```python
HOST = ''           # Empty string = accept connections from any IP
PORT = 8800        # Port number for the server
CHUNK_SIZE = 1024  # Size of data chunks to send
CLOSE_AFTER_ONE_CLIENT = True  # Server closes after one client
```

### Client Settings (in `client.py`)
```python
HOST = 'localhost'  # Server IP address
PORT = 8800        # Server port number
```

## 📚 Key Networking Terminologies

### **Socket Programming**
- **Socket**: An endpoint for network communication between two machines
- **TCP (Transmission Control Protocol)**: Reliable, ordered data delivery protocol
- **Port**: Virtual endpoint for specific services (like port 8800 for our file transfer)

### **Client-Server Architecture**
- **Server**: Listens for incoming connections and serves data
- **Client**: Initiates connection and requests data from server
- **Binding**: Server associates socket with specific IP and port
- **Listening**: Server waits for client connections
- **Accepting**: Server establishes connection with client

### **File Transfer Concepts**
- **Binary Mode**: Files transferred as raw bytes (`'rb'`, `'wb'`)
- **Chunked Transfer**: Data sent/received in smaller pieces (1024 bytes)
- **Progress Tracking**: Monitoring bytes transferred in real-time
- **Timeout**: Maximum time to wait for data before giving up

### **Error Handling**
- **Connection Refused**: Client can't connect to server
- **File Not Found**: Server file doesn't exist
- **Socket Timeout**: Connection takes too long
- **Graceful Shutdown**: Proper cleanup when stopping server

## 🏗️ Project Structure

```
python-socket-file-transfer/
├── server.py          # TCP server implementation
├── client.py          # TCP client implementation
├── server-file.txt    # Sample file to transfer
├── client-file.txt    # Received file (created after transfer)
├── README.md          # This file
└── .gitignore         # Git ignore file
```

## 🔍 How It Works

### **Server Process:**
1. **Initialize** socket and bind to port 8800
2. **Listen** for incoming client connections
3. **Accept** client connection when available
4. **Receive** greeting message from client
5. **Read** `server-file.txt` in binary mode
6. **Send** file data in 1024-byte chunks
7. **Track** progress and calculate transfer speed
8. **Close** client connection and optionally exit

### **Client Process:**
1. **Initialize** socket and connect to server
2. **Send** greeting message to server
3. **Create** `client-file.txt` for receiving data
4. **Receive** file data in 1024-byte chunks
5. **Write** received data to file
6. **Track** progress and calculate transfer speed
7. **Close** file and socket connection

## 🐛 Troubleshooting

### **Common Issues:**

**"Connection refused" error:**
- Make sure server is running first
- Check if port 8800 is available
- Verify firewall settings

**"File not found" error:**
- Ensure `server-file.txt` exists in project directory
- Check file permissions

**Transfer hangs:**
- Server has 30-second timeout protection
- Client has 30-second timeout protection
- Use Ctrl+C to stop server gracefully

### **Port Already in Use:**
```bash
# Windows
netstat -ano | findstr :8800
taskkill /PID <PID> /F

# Linux/Mac
lsof -i :8800
kill -9 <PID>
```

## 🎯 Learning Objectives

This project demonstrates:
- **Network Programming** fundamentals
- **Socket API** usage in Python
- **Client-Server** communication patterns
- **File I/O** operations
- **Error Handling** in network applications
- **Performance Monitoring** basics

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- Python Socket Programming documentation
- TCP/IP networking fundamentals
- File transfer protocols and best practices

---

**Happy Coding! 🚀**

*For questions or issues, please open a GitHub issue.*
