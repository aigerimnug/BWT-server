import socket
import time

def generate_bwt(dna):
    dna = dna + '$'

    rotations = [dna[i:] + dna[:i] for i in range(len(dna))]

    rotations.sort()

    bwt_result = ''.join(rotation[-1] for rotation in rotations)

    return bwt_result

def inverse_bwt(bwt):
    table = [""] * len(bwt)

    
    for i in range(len(bwt)):
        table = sorted(bwt[i] + table[i] for i in range(len(bwt)))

    
    original_text = [row for row in table if row.endswith('$')][0]

    return original_text[:-1] 

End = b'\0'

def recv_end(conn):
    total_data=[]; data=''
    while True:
        data=conn.recv(1024)
        if End in data:
            total_data.append(data[:data.find(End)])
            break
        total_data.append(data)
    return b''.join(total_data)

def handle_connection(conn):
    data = recv_end(conn)
    data = data.decode('utf-8')
    print('Received request:', data)

    time.sleep(5)

    if data.startswith('BWT:'):
        bwt_sequence = data[len('BWT:'):]
        original_dna = inverse_bwt(bwt_sequence)
        conn.sendall(original_dna.encode('utf-8'))
    else:
        bwt_sequence = generate_bwt(data)
        conn.sendall(bwt_sequence.encode('utf-8'))

    conn.close()

def start_server():
    s = socket.socket()
    host = socket.gethostname()
    port = 12345
    s.bind((host, port))

    s.listen(5)

    while True:
        conn, addr = s.accept()
        print('Got connection from', addr)
        handle_connection(conn)

if __name__ == "__main__":
    start_server()

