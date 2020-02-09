### testing out module

import numpy as np
import PIL
from keras.preprocessing import image
import pickle
import keras.models as models
import scipy

### load galaxy datadata
def get_image_names(input_image, n):
	encoder = models.load_model('encoder.h5')
	encoder.compile(loss = 'binary_crossentropy', optimizer = 'adam')


	with open('encoded_data.dat', 'rb') as f:
		dd = pickle.load(f)

	img_width, img_height = 228, 228
	ypixels_force, xpixels_force = 200, 200
	#img = image.load_img('tornado-upload-master/galaxy_test_image.png', target_size=(img_width, img_height))
	img = image.load_img(input_image, target_size=(xpixels_force, ypixels_force))
	#img_resized = np.array(Image.fromarray(arr).resize())
	x = image.img_to_array(img)
	x = x.astype("float32") / 255.0
	x = x.flatten()
	x = np.expand_dims(x, axis=0)


	z_q = encoder.predict(x)

	### compare vector to all in data set (with distances) d = sqrt(sum((z_i-z_m)**2)))

	length = np.shape(dd)[0]
	distances = np.zeros(length)

	for i in range(0, length):
		row = dd[i]
		diff = (row - z_q)**2
		sum_dist = np.sum(diff)
		dist = np.sqrt(sum_dist)
		distances[i] = dist

	### return top 5 matches (minimum distance)

	#n = 5
	indices = distances.argsort()[:n]
	#print(np.array(distances)[indices.astype(int)])

	### get filenames from encodefiles.txt (by index)

	filenames = 'encoded_files.txt'
	with open(filenames) as f:
  		line_list = f.readlines()

	filename_match = np.array(line_list)[indices.astype(int)]


	extensions = []
	for filename in filename_match:
		filename0 = filename.strip('\n')
		filename1 = filename0.split('/')
		filename2 = filename1[-1]
		extensions.append(filename2)


	return extensions












