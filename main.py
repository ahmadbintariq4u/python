# from skimage.metrics import structural_similarity as ssim
# import argparse
# import cv2


# # 3. Load the two input images
# imageA = cv2.imread('assets/image1.jpg')
# imageB = cv2.imread('assets/image3.jpg')

# imageA=cv2.resize(imageA,(500,500))
# imageB=cv2.resize(imageB,(500,500))

# # 4. Convert the images to grayscale
# grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
# grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)

# # 5. Compute the Structural Similarity Index (SSIM) between the two
# #    images, ensuring that the difference image is returned
# #(score, diff) = compare_ssim(grayA, grayB, full=True)
# (score, diff) = ssim(grayA, grayB, full=True)
# diff = (diff * 255).astype("uint8")

# # 6. You can print only the score if you want
# print("SSIM: {}".format(score))


import tensorflow as tf

my_tensor = tf.constant([[1.0, 2.0], [3.0, 4.0]])
my_variable = tf.Variable(my_tensor)

# Variables can be all kinds of types, just like tensors
bool_variable = tf.Variable([False, False, False, True])
complex_variable = tf.Variable([5 + 4j, 6 + 1j])
print("Shape: ", my_variable.shape)
print("DType: ", my_variable.dtype)
print("As NumPy: ", my_variable.numpy())