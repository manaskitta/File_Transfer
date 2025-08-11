# Python Socket File Transfer Project

A Python socket programming project that demonstrates client-server file transfer over TCP/IP.  
This project now supports **cross-system file transfers** and **multiple file selection from the client side**.

---

## 🚀 Features

- **TCP Socket Communication** – Reliable data transfer between client and server across networks
- **Cross-System Support** – Client can connect from another machine on the same LAN or via VPN
- **Multiple File Selection** – Client can request a file from a list maintained by the server
- **Binary File Transfer** – Supports any file type with progress tracking
- **Error Handling** – Graceful recovery from network and file errors
- **Performance Monitoring** – Shows transfer speed and progress indicators
- **Timeout Protection** – Prevents hanging on slow/no connections
- **Graceful Shutdown** – Proper resource cleanup on server exit

---

## 📋 Prerequisites

- Python **3.6** or higher  
- Basic understanding of networking concepts  
- For cross-system transfer: client and server should be on the same network or connected via VPN

---

## 🛠️ Installation & Setup

### 1️⃣ Clone the Repository
```
git clone https://github.com/manaskitta/python-socket-file-transfer.git
cd python-socket-file-transfer
```

### 2️⃣ Verify Python Installation
```
python --version
# or
python3 --version
```

### 3️⃣ Prepare Server Files
Place any files you want to make available for download inside the `server_files/` folder.

---

## 🚀 How to Run

### **Step 1: Start the Server**
On the **server machine**:
```
python server.py
```
**Example Output:**
```
Socket created successfully.
Server bound to port 8800
Socket is listening...
Available files:
  1. file1.txt
  2. image.png
  3. document.pdf
```

> 💡 For cross-system communication, use the server’s LAN IP (found via `ipconfig` or `ifconfig`).

---

### **Step 2: Start the Client**
On the **client machine** (same or different machine in the network):
```
python client.py
```

**Client Output Example:**
```
Available files on server:
1. file1.txt
2. image.png
3. document.pdf
Enter the number of the file you want to download: 2
Connected to server at 192.168.1.10:8800
Requesting 'image.png'...
File received successfully. Total bytes: 102400
Transfer speed: 25600.00 bytes/sec
```

---

### **Step 3: Verify Download**
The requested file will be saved in the client’s working directory.

---

## 🔧 Configuration

### **Server Settings** (`server.py`)
```
HOST = ''                   # Empty = accept connections from any IP (cross-system)
PORT = 8800                 # Port to listen on
CHUNK_SIZE = 1024           # Data chunk size
SERVER_FILES_DIR = 'server_files'  # Directory containing available files
```

### **Client Settings** (`client.py`)
```
HOST = '192.168.x.x'        # Server machine's LAN IP
PORT = 8800
```

**Find the Server LAN IP:**
- **Windows:** `ipconfig` and look for `IPv4 Address`
- **Linux/Mac:** `ifconfig` or `ip addr`

---

## 📚 How It Works

### **Server Flow**
1. Initializes socket and binds to `HOST:PORT`
2. Lists all files in `server_files/`
3. Sends file list to the client upon connection
4. Receives file selection from the client
5. Streams the file in binary chunks, tracking progress
6. Closes the connection

### **Client Flow**
1. Connects to the server using IP and port
2. Receives available file list
3. Sends selected file choice to the server
4. Receives the file and writes it locally
5. Displays transfer progress and speed
6. Closes the socket

---

## 🐛 Troubleshooting

**Connection Refused**
- Ensure server is running first
- For cross-system, use the server’s LAN IP, not `localhost`
- Check firewall on the server machine and allow port 8800

**File Not Found**
- File must be present in `server_files/` directory

**Port Already in Use**
```
# Windows
netstat -ano | findstr :8800
taskkill /PID  /F

# Linux/Mac
lsof -i :8800
kill -9 
```

---

## 🎯 Learning Objectives

This project demonstrates:
- **Socket Programming** in Python
- **Client-Server Communication** patterns
- **Binary File Transfer** with chunked sending
- **Progress & Speed Tracking**
- **Error Handling** in networked applications

---

## 🤝 Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add some AmazingFeature'`)
4. Push branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 License
This project is available under the **MIT License** – see [LICENSE](LICENSE) for details.

---

**Now supports cross-system transfers + multiple file selection 🚀**
```

***
