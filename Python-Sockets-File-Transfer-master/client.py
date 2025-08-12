import socket
import os
import sys
import time

SERVER_IP = "127.0.0.1"  # Change to your server's IP
PORT = 8800

def download_file(sock):
    file_list = sock.recv(4096).decode()
    if file_list == "NO_FILES":
        print("[CLIENT] No files available.")
        return
    print("\nAvailable files:\n" + file_list)

    filename = input("Enter file name to download: ").strip()
    sock.send(filename.encode())

    status = sock.recv(1024).decode()
    if status != "FILE_OK":
        print("[CLIENT] File not found on server.")
        return

    with open(filename, "wb") as f:
        bytes_received = 0
        start_time = time.time()
        while True:
            data = sock.recv(1024)
            if not data:
                break
            f.write(data)
            bytes_received += len(data)
        elapsed = time.time() - start_time
    print(f"[CLIENT] Downloaded {filename} ({bytes_received} bytes) in {elapsed:.2f}s.")

def upload_file(sock):
    local_file = input("Enter local file path to upload: ").strip()
    if not os.path.exists(local_file):
        print("[CLIENT] File not found.")
        return

    sock.recv(1024)  # Expect SEND_FILENAME
    filename = os.path.basename(local_file)
    sock.send(filename.encode())

    sock.recv(1024)  # Expect SEND_FILE
    with open(local_file, "rb") as f:
        bytes_sent = 0
        start_time = time.time()
        while chunk := f.read(1024):
            sock.send(chunk)
            bytes_sent += len(chunk)
        elapsed = time.time() - start_time
    print(f"[CLIENT] Uploaded {filename} ({bytes_sent} bytes) in {elapsed:.2f}s.")

def main():
    try:
        with socket.socket() as sock:
            sock.connect((SERVER_IP, PORT))

            msg = sock.recv(1024).decode()
            if msg.startswith("DENIED"):
                print(msg)
                return

            if msg == "PASSWORD:":
                password = input("Enter password: ").strip()
                sock.send(password.encode())

            auth_response = sock.recv(1024).decode()
            if auth_response != "AUTH_OK":
                print(auth_response)
                return

            menu = sock.recv(1024).decode()
            choice = input(menu).strip()
            sock.send(choice.encode())

            if choice == "1":
                download_file(sock)
            elif choice == "2":
                upload_file(sock)
            else:
                print("[CLIENT] Invalid choice.")

    except Exception as e:
        print(f"[CLIENT] Error: {e}")

if __name__ == "__main__":
    main()
