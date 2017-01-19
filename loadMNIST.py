import numpy as np
def LoadMNIST(filename):
    '''Written by GSY'''
    with open(filename, 'rb') as f:
        header = bytearray(f.read(4)) #read the header bytes
        datatype = 'int32'  
        typecode = header[2] # read the type byte
        if(typecode==8):
            datatype = '>u1';
        elif(typecode == 12):
            datatype = '>f4'
        elif(typecode == 14):
            datatype = '>f8'    
        print datatype
        
        size = np.fromfile(f, '>i4', header[3]) #read the dimensions of the array  
        dshape = ()
        count = 1
        for d in range(0,len(size)):
            count *= size[d]
            dshape += (size[d], )        
        print dshape
        data = np.fromfile(f, datatype, count) #read the array data
        return data.reshape(dshape)   