import socket
import os
import time
import signal
import sys

# =======================
# CONFIGURATION
# =======================
HOST = "0.0.0.0"
PORT = 8800
FILES_DIR = "server_files"
CLIENTS_FILE = "allowed_clients.txt"
CLOSE_AFTER_ONE_CLIENT = False

# =======================
# LOAD ALLOWED CLIENTS
# =======================
def load_allowed_clients(filepath):
    allowed = {}
    if os.path.exists(filepath):
        with open(filepath, "r") as f:
            for line in f:
                parts = line.strip().split()
                if len(parts) >= 2:
                    ip, pwd = parts[0], parts[1]
                    allowed[ip] = pwd
    return allowed

ALLOWED_CLIENTS = load_allowed_clients(CLIENTS_FILE)

# Ensure server_files exists
os.makedirs(FILES_DIR, exist_ok=True)

# =======================
# SHUTDOWN HANDLER
# =======================
def signal_handler(sig, frame):
    print("\n[SERVER] Shutting down gracefully...")
    sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

# =======================
# FILE TRANSFER HELPERS
# =======================
def send_file(con, filename):
    """Send a file to the client."""
    file_path = os.path.join(FILES_DIR, filename)
    if not os.path.exists(file_path):
        con.send("FILE_NOT_FOUND".encode())
        return

    con.send("FILE_OK".encode())
    with open(file_path, "rb") as f:
        bytes_sent = 0
        start_time = time.time()
        while chunk := f.read(1024):
            con.send(chunk)
            bytes_sent += len(chunk)
        elapsed = time.time() - start_time
    print(f"[SERVER] Sent {filename} ({bytes_sent} bytes) in {elapsed:.2f}s.")

def receive_file(con, filename):
    """Receive a file from the client."""
    file_path = os.path.join(FILES_DIR, filename)
    with open(file_path, "wb") as f:
        bytes_received = 0
        start_time = time.time()
        while True:
            data = con.recv(1024)
            if not data:
                break
            f.write(data)
            bytes_received += len(data)
        elapsed = time.time() - start_time
    print(f"[SERVER] Received {filename} ({bytes_received} bytes) in {elapsed:.2f}s.")

# =======================
# CLIENT HANDLER
# =======================
def handle_client(con, addr):
    client_ip = addr[0]
    print(f"[SERVER] Connection from {client_ip}:{addr[1]}")

    # Whitelist check
    if client_ip not in ALLOWED_CLIENTS:
        con.send("DENIED: IP not allowed.".encode())
        print(f"[SERVER] Denied connection from {client_ip}")
        return

    # Ask for password
    con.send("PASSWORD:".encode())
    password = con.recv(1024).decode().strip()
    if password != ALLOWED_CLIENTS[client_ip]:
        con.send("DENIED: Wrong password.".encode())
        print(f"[SERVER] Wrong password from {client_ip}")
        return

    con.send("AUTH_OK".encode())
    print(f"[SERVER] {client_ip} authenticated.")

    # Send menu
    menu = "\nSelect an option:\n1. Download file\n2. Upload file\nChoice: "
    con.send(menu.encode())
    choice = con.recv(1024).decode().strip()

    if choice == "1":
        # Send file list
        files = os.listdir(FILES_DIR)
        if not files:
            con.send("NO_FILES".encode())
            return
        con.send("\n".join(files).encode())

        requested_file = con.recv(1024).decode().strip()
        send_file(con, requested_file)

    elif choice == "2":
        con.send("SEND_FILENAME".encode())
        filename = con.recv(1024).decode().strip()
        con.send("SEND_FILE".encode())
        receive_file(con, filename)

# =======================
# MAIN SERVER LOOP
# =======================
def main():
    with socket.socket() as sock:
        sock.bind((HOST, PORT))
        sock.listen(5)
        print(f"[SERVER] Listening on {HOST}:{PORT}")

        while True:
            try:
                con, addr = sock.accept()
                with con:
                    handle_client(con, addr)
            except Exception as e:
                print(f"[SERVER] Error: {e}")

            if CLOSE_AFTER_ONE_CLIENT:
                break

if __name__ == "__main__":
    main()
