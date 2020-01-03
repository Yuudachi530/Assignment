Picture = {}
for i in range(8):
    for j in range(8):
        Picture[i, j] = 60

def Lighten():
    for i in range(8):
        for j in range(8):
            Picture[i, j] = Picture[i, j] * 1.1
            if Picture[i, j] >= 255:
                Picture[i, j] = 255
                print('burnt out')
            else:
                Picture[i, j] = int(Picture[i, j])

Lighten()
print(Picture)
