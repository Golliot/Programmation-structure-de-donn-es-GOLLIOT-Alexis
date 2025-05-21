import struct as st

def extract_data():
    res = []
    f = open("the_wall.wav", 'rb')
    data = f.read()
    chunk_size = 4 #on parcourt data 4 par 4
    nb_channel = 2
    nb_bytes_in_data = st.unpack('I', data[40:44])[0]
    for i in range(nb_bytes_in_data//4):
        res.append(st.unpack_from('hh', data, 44+4*i))
    return res

def create_wav():
    f = open('new.wav', 'wb')
    
    size = 10786332
    riff = st.pack("<4sI4s", b'RIFF', size, b'WAVE')
    fmt = st.pack('<4sIHHIIHH', b'fmt ', 16, 1, 2, 44100 , 176400, 4, 16)
    
    #create header
    data_header = st.pack('<4sI', b'data', 10786296)
    f.write(riff)
    f.write(fmt)
    f.write(data_header)

    #create data
    unpacked_data = extract_data()
    data = b''.join(st.pack('<hh', unpacked_data[i][0], unpacked_data[i][1]) for i in range(len(unpacked_data)))
    f.write(data)
    
    

create_wav()
f=open("new.wav", 'rb')
data = f.read()
print(data[0:44])



    