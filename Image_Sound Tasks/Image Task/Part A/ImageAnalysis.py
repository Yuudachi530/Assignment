from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

img = Image.open('Kenshi Yonezu.jpg')

bit_1 = img.convert('1')
bit_8 = img.convert('P')
bit_24 = img.convert('RGB')
bit_32 = img.convert('RGBA')

plt.figure('Kenshi Yonezu')
plt.subplot(2,2,1)
plt.imshow(bit_1), plt.title('bit-1'), plt.axis('off')
plt.subplot(2,2,2)
plt.imshow(bit_8), plt.title('bit-8'), plt.axis('off')
plt.subplot(2,2,3)
plt.imshow(bit_24), plt.title('bit-24'), plt.axis('off')
plt.subplot(2,2,4)
plt.imshow(bit_32), plt.title('bit-32'), plt.axis('off')

plt.savefig('Kenshi Yonezu.png', dpi = 700)
plt.show()



#plt.imshow(bit_1), plt.axis('off')
#bit_8 = img.convert('L'), plt.title('8-bits')
#plt.imshow(bit_8), plt.axis('off')
#bit_24 = img.convert('RGB'), plt.title('24-bits')
#plt.imshow(bit_24), plt.axis('off')
#bit_32 = img.convert('RGBA'), plt.title('32-bits')
#plt.imshow(bit_32), plt.axis('off')