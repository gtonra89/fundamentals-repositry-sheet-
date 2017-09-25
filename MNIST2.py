import gzip
def read_images(filename):
    f= gzip.open(filename,'rb')
    magic = f.read(4) #read num 4 bytes long from file
    magic = int.from_bytes(magic, 'big') #convert integer int to 32bits
    print("magic is :",magic) # print

    noimg = f.read(4) #read how many labels in a file
    noimg = int.from_bytes(noimg, 'big')
    print("images are : ",noimg)

    norow = f.read(4) #read how many labels in a file
    norow = int.from_bytes(norow, 'big')
    print("rows are : ",norow)

    nocol = f.read(4) #read how many labels in a file
    nocol = int.from_bytes(nocol, 'big')
    print("cols are : ",nocol)

    images = []
    for i in range(noimg):
     row = []   
    for r in range(norow):
       col = []
    for c in range(nocol):
        col.append(int.from_bytes(f.read(2)),'big')
    row.append(col)
    images.append(row)
    
    return images

train_images = read_images('C:/data/t10k-images-idx3-ubyte.gz')
test_images = read_images('C:/data/t10k-images-idx3-ubyte.gz')