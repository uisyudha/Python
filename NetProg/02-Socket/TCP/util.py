import struct


def sendall_termination(conn, data):
    data = data + "\r\n"
    conn.send(data)


def recvall_termination(conn):
    alldata = ''
    while "\r\n" not in alldata:
        data_terima = conn.recv(10)
        alldata = alldata + data_terima

    alldata = alldata.replace("\r\n", "")
    return alldata


def sendall_number(conn, data):
    msg_len = len(data)
    msg_len_pack = struct.pack(">I", msg_len)
    # Prepend msg len ke data
    data = msg_len_pack + data
    # kirim
    conn.send(data)


def recvall_number(conn):
    msg_len_raw = conn.recv(4)
    msg_len = struct.unpack(">I", msg_len_raw)[0]

    # Baca sampai habis
    alldata = ''

    while len(alldata) < msg_len:
        alldata = alldata + conn.recv(10)
    return alldata
