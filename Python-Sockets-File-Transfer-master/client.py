import socket
import time

# Initialize Socket Instance
sock = socket.socket()
sock.settimeout(30)  # 30 second timeout
print ("Socket created successfully.")

# Defining port and host
port = 8800
host = 'localhost'

try:
    # Connect socket to the host and port
    sock.connect((host, port))
    print('Connection Established.')
    
    # Send a greeting to the server
    sock.send('A message from the client'.encode())
    print('Message sent to server')

    # Write File in binary
    file = open('client-file.txt', 'wb')
    bytes_received = 0
    start_time = time.time()  # Start timing the transfer

    # Keep receiving data from the server
    line = sock.recv(1024)

    while(line):
        file.write(line)
        bytes_received += len(line)
        # Simple progress indicator
        if bytes_received % 1024 == 0:  # Show progress every 1KB
            print(f"Received {bytes_received} bytes...")
        line = sock.recv(1024)

    file.close()
    transfer_time = time.time() - start_time
    speed = bytes_received / transfer_time if transfer_time > 0 else 0
    print(f'File has been received successfully. Total bytes: {bytes_received}')
    print(f'Transfer speed: {speed:.2f} bytes/second')

except Exception as e:
    print(f"Client error: {e}")
finally:
    sock.close()
    print('Connection Closed.')
