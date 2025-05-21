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

def question2():
    with open('question2.wav', 'wb') as f:
    
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
        data = b''.join(st.pack('<hh', unpacked_data[i][0], 
                                unpacked_data[i][1]) for i in range(len(unpacked_data)))
        f.write(data)
    

def question3():
    with open('question3.wav', 'wb') as f:

        size = 5393184
        
        #create header
        riff = st.pack("<4sI4s", b'RIFF', size, b'WAVE')
        fmt = st.pack('<4sIHHIIHH', b'fmt ', 16, 1, 2, 44100 , 176400, 4, 16)
        data_header = st.pack('<4sI', b'data', 10786296//2)

        f.write(riff)
        f.write(fmt)
        f.write(data_header)

        #create data
        unpacked_data = extract_data()
        data = b''.join(st.pack('<hh', unpacked_data[2*i][0],
                                unpacked_data[2*i][1]) for i in range(len(unpacked_data)//2))
        f.write(data)

def question4():
    with open('question4.wav', 'wb') as f:
        size = 21572628
        riff = st.pack("<4sI4s", b'RIFF', size, b'WAVE')
        fmt = st.pack('<4sIHHIIHH', b'fmt ', 16, 1, 2, 44100 , 176400, 4, 16)
        data_header = st.pack('<4sI', b'data', 10786296*2)
        f.write(riff)
        f.write(fmt)
        f.write(data_header)

        unpacked_data = extract_data()
        samples = []
        for i in range(len(unpacked_data)-1):
            samples.append(st.pack('<hh', unpacked_data[i][0], unpacked_data[i][1]))
            samples.append(st.pack('<hh',
                            (unpacked_data[i][0] + unpacked_data[i+1][0])//2,
                            (unpacked_data[i][1] + unpacked_data[i+1][1])//2))
        samples.append(st.pack('<hh', unpacked_data[-1][0], unpacked_data[-1][1]))
        data = b''.join(samples)
        f.write(data)
    
def question5(phi: float):
    with open('question5.wav', 'wb') as f:
    
        size = 10786332
        riff = st.pack("<4sI4s", b'RIFF', size, b'WAVE')
        fmt = st.pack('<4sIHHIIHH', b'fmt ', 16, 1, 2, int(phi*44100) , 176400, 4, 16)
        
        #create header
        data_header = st.pack('<4sI', b'data', 10786296)
        f.write(riff)
        f.write(fmt)
        f.write(data_header)

        #create data
        unpacked_data = extract_data()
        data = b''.join(st.pack('<hh', unpacked_data[i][0], 
                                unpacked_data[i][1]) for i in range(len(unpacked_data)))
        f.write(data)
        
    

    
if __name__ == '__main__':
    question2()
    question3() #le son est accéléré *2
    question4() #le son est ralenti *2
    question5(1.33)