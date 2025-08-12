Here’s an updated **concise** README that adds your **file upload from client to server** feature without making the file bloated:

---

# Python Socket File Transfer Project

A Python socket programming project demonstrating **client-server file transfers** over TCP/IP.
Now supports **cross-system transfers**, **multiple file selection**, and **client-to-server uploads**.

---

## 🚀 Features

* **TCP Socket Communication** – Reliable transfers over LAN/VPN
* **Cross-System Support** – Client can connect from another machine
* **Multiple File Selection** – Download files from server’s list
* **Client File Upload** – Client can send files to the server’s `server_files/` folder
* **Binary Transfer** – Works for any file type
* **Progress & Speed Tracking**
* **Error Handling** & Timeout Protection
* **Whitelist + Password Authentication** (optional)

---

## 📋 Prerequisites

* Python **3.6+**
* Server & client on same network (or via VPN)

---

## 🛠 Setup

**1️⃣ Clone Repo**

```bash
git clone https://github.com/manaskitta/python-socket-file-transfer.git
cd python-socket-file-transfer
```

**2️⃣ Prepare Folders**

* Put downloadable files in `server_files/`
* For uploads, server will store incoming files in the same folder

---

## 🚦 Usage

**Start Server**

```bash
python server.py
```

**Start Client**

```bash
python client.py
```

**Client Menu Example**

```
Enter password: mylocalpass

Select an option:
1. Download file
2. Upload file
Choice: 2
Enter local file path to upload: C:\path\to\file.txt
[CLIENT] Upload complete.
```

---

## 🔧 Config

**In `server.py`:**

```python
HOST = ''                # Accept from any IP
PORT = 8800
SERVER_FILES_DIR = 'server_files'
```

**In `client.py`:**

```python
HOST = '192.168.x.x'     # Server LAN IP
PORT = 8800
```

---

## 📚 How It Works

**Server**

1. Starts socket, binds to HOST\:PORT
2. Lists files in `server_files/`
3. Accepts client connection & authenticates
4. Sends file list for downloads or receives file uploads
5. Saves uploaded files to `server_files/`

**Client**

1. Connects to server
2. Authenticates
3. Chooses **Download** or **Upload**
4. Transfers file in binary chunks with progress tracking

---

## 🐛 Troubleshooting

* **Connection refused** → Start server first & check firewall
* **File not found on upload** → Use correct absolute path without quotes in PowerShell
* **Port in use** → Change port or free it

---

## 📝 License

MIT License – see LICENSE for details.

---