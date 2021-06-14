
from PIL import Image
import numpy as np
import utils
import cv2 

img = np.array((Image.open('test.jpg')))  

img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)[:, :, np.newaxis] 
h, w, c = img.shape 

img_tmp = img.copy() 
    
noise_g = np.random.normal(0, 80, (h, w, c))
noise_p = np.random.poisson(30, (h, w, c))

size = h * w * c 
all_coords = [i for i in range(size)]
samples_0 = np.random.choice(all_coords, int(size * 0.1))
samples_1 = np.random.choice(all_coords, int(size * 0.1))

noisy_img = (noise_g + img_tmp + noise_p ).clip(0, 255).reshape(-1)
noisy_img[samples_0] = 0
noisy_img[samples_1] = 255

noisy_img = noisy_img.reshape((h, w, c))
    
    

    
noisy_img = noisy_img.astype(np.uint8)



# print(utils.psnr(noisy_img, img))

# noisy_img = (noisy_img * 255.0).astype(np.uint8)
noisy_img = np.repeat(noisy_img, 3, axis=2)
Image.fromarray(noisy_img).save('noisy.jpg')



