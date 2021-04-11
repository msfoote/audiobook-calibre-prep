from zipfile import ZipFile,is_zipfile
import os


directory = os.getcwd()

print('This will unzip all of the files in each subdirectory of ' + directory + ' into their own directory')
for root, dirs, files in os.walk(directory):
	# print('\n--------------------------\n',root)
	# print(dirs)
	# print(files)
	for i,name in enumerate(files):
		filename = os.path.join(root, name)
		if is_zipfile(filename):
			print('\tExtracting ZIP:\t',name)
			# print(filename)
			# os.mkdir(os.path.splitext(name)[0])
			with ZipFile(filename,'r') as zip:
				zip.extractall(root)
			os.remove(filename)
		elif filename.endswith(('.mp3','.m4b','.aa','.aax','.m4a','.aac','.m4p','.ogg','.wma','.flac','.alac','.wav','m3u','.py')):
			pass
		else:
			os.remove(filename)