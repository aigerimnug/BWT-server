import socket
import sys

def send_message_to_server(message):
    try:
        s = socket.socket()
        host = socket.gethostname()
        port = 12345

        s.connect((host, port))
        s.sendall(message)

        response = s.recv(1024)
        print("Server response:", response.decode('utf-8'))

    except Exception as e:
        print("Error:", e)

    finally:
        s.close()

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("No message to server provided on the command line; ending program.")
    else:
        print("If you want to inversely convert from Burrows-Wheeler Transform (BWT) of DNA sequences to original DNA sequence, please start you message with 'BWT: ' (e.g 'BWT:GTC$GACTAGA') ")
        message = ' '.join(sys.argv[1:]) + '\0'
        print("Sending message to server:", message)
        send_message_to_server(message.encode('utf-8'))
