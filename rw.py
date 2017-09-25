import gzip
with gzip.open('t10k-images-idx3-ubyte.gz','rb') as f:
    file_content = f.read(4)
    print(file_content)