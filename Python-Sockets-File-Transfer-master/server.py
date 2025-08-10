import socket
import os
import time
import signal

# Initialize Socket Instance
sock = socket.socket()
sock.settimeout(30)  # 30 second timeout
print ("Socket created successfully.")

# Graceful shutdown handler
def signal_handler(sig, frame):
    print("\nShutting down server gracefully...")
    sock.close()
    exit(0)
signal.signal(signal.SIGINT, signal_handler)

# Defining port and host
port = 8800
host = ''

# Set to True if you want server to close after one client
CLOSE_AFTER_ONE_CLIENT = True

try:
    # binding to the host and port
    sock.bind((host, port))
    print(f"Server bound to port {port}")

    # Accepts up to 5 connections
    sock.listen(5) 
    print('Socket is listening...')

    while True:
        try:
            # Establish connection with the clients.
            con, addr = sock.accept()
            print(f'Connected with client at {addr[0]}:{addr[1]}')

            # Get data from the client
            data = con.recv(1024)
            if data:
                print(f"Client message: {data.decode()}")
            else:
                print("Client disconnected before sending message")
                con.close()
                continue
            
            # Check if file exists
            if not os.path.exists('server-file.txt'):
                print("Error: server-file.txt not found!")
                con.close()
                continue
                
            # Read File in binary
            file = open('server-file.txt', 'rb')
            line = file.read(1024)
            bytes_sent = 0
            start_time = time.time()  # Start timing the transfer
            
            # Keep sending data to the client
            while(line):
                con.send(line)
                bytes_sent += len(line)
                # Simple progress indicator
                if bytes_sent % 1024 == 0:  # Show progress every 1KB
                    print(f"Sent {bytes_sent} bytes...")
                line = file.read(1024)
            
            file.close()
            transfer_time = time.time() - start_time
            speed = bytes_sent / transfer_time if transfer_time > 0 else 0
            print(f'File has been transferred successfully. Total bytes sent: {bytes_sent}')
            print(f'Transfer speed: {speed:.2f} bytes/second')

        except Exception as e:
            print(f"Error handling client: {e}")
        finally:
            con.close()
            
        # Optional: Close server after one client
        if CLOSE_AFTER_ONE_CLIENT:
            print("Server will close after handling one client.")
            break

except Exception as e:
    print(f"Server error: {e}")
finally:
    sock.close()
    print("Server socket closed.")
