import os

def gen_file(imagepath_list, extension_list):

	os.remove('current_images.html')

	f = open('current_images.html','w') #move to after loop?
	
	message_full = ['<html>', "<head>", '<meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>', "<title>image results</title>", "</head>", "<body>"]

	message_end = ['</body>', '</html>']

	for i in range(len(imagepath_list)):
		if i == 0:
			message_current_1 = "<p> {} {} </p>".format('input image: ', extension_list[i])
		else:
			message_current_1 = "<p> {} {} </p>".format( 'match ' + str(i) + ': ', extension_list[i])
		message_current_2 = '<img src="{}" height="300" width="300"/>'.format(imagepath_list[i])
		message_full.append(message_current_1)
		message_full.append(message_current_2)

	message_full.append(message_end[0])
	message_full.append(message_end[1])

	for element in message_full:
		f.write(element)
		f.write('\n')

	f.close()

