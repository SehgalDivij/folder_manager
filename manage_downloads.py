import glob, os, shutil
from os import walk

# Folder to be managed.
DIRECTORY_TO_MANAGE = 'C:\\Users\\catch\\Downloads'

# Destination folders for each extension
DIRS = {
	'Documents': ('txt', 'doc', 'docx', 'pdf', 'ppt', 'pptx', 'pps', 'xlsx', 'xls'),
	'Music': ('mp3', 'wav'),
	'Video': ('flv', 'mp4', 'avi', '3gp', 'mkv'),
	'Programs': ('exe', 'msi', 'bat', 'py', 'whl', 'pyc'),
	'Compressed': ('zip', 'rar', 'tar', 'gz', 'cab', 'xz'),
	'XMLFiles': ('xml'),
	'Photos': ('jpg', 'gif', 'jpeg', 'png', 'JPG', 'JPEG', 'GIF', 'PNG'),
	'Web': ('htm', 'js', 'html', 'css'),
	'Jars': ('jar',),
	'ISO Images': ('iso',),
	'Logs': ('log',),
	'Linux Repos': ('repo',),
	'Random': ('cfg', 'json', 'csv', 'in', 'tgn')
}

def pre_manage():
	print('%s Management Starts' % DIRECTORY_TO_MANAGE)

def ensure_directories_exist():
	"""
	This function removes recursively all empty folders present within the directory
	and creates all folders mentioned in the DIRS dictionary above
	"""
	# Removing all empty folders in Downloads directory
	for (dirpath, dirnames, filenames) in walk(DIRECTORY_TO_MANAGE):
		for dir_name in dirnames:
			cur_path = '%s\\%s' % (dirpath, dir_name)
			os.chdir(cur_path)
			if not os.listdir(cur_path):
				print('%s is empty. Removing..' % dir_name)
				os.rmdir(dir_name)
	# Change to Downloads Folder
	os.chdir(DIRECTORY_TO_MANAGE)
	# Creating Missing Folders
	for folder_name in list(DIRS.keys()):
		if not os.path.exists(folder_name):
			print('folder %s does not exist. Creating..' % folder_name)
			os.makedirs(folder_name)

def transfer_files():
	dir_level = 0
	for (dirpath, dirnames, filenames) in walk(DIRECTORY_TO_MANAGE):
		for file in filenames:
			"""
			Break after first level tree is travered, as nested folder and files are not be touched.
			Removing this break might cause havoc in your Downloads Folder, depending on contents of nested folders.
			In case you choose to remove this break statement, do it at your own risk.
			I shall not be held responsible for whatever happens thereafter.
			"""
			dest_folder = ''
			if file.endswith(DIRS['Documents']):
				dest_folder = 'Documents'
			elif file.endswith(DIRS['Music']):
				dest_folder = 'Music'
			elif file.endswith(DIRS['Video']):
				dest_folder = 'Video'
			elif file.endswith(DIRS['Programs']):
				dest_folder = 'Programs'
			elif file.endswith(DIRS['Compressed']):
				dest_folder = 'Compressed'
			elif file.endswith(DIRS['XMLFiles']):
				dest_folder = 'XMLFiles'
			elif file.endswith(DIRS['Photos']):
				dest_folder = 'Photos'
			elif file.endswith(DIRS['Web']):
				dest_folder = 'Web'
			elif file.endswith(DIRS['Random']):
				dest_folder = 'Random'
			elif file.endswith(DIRS['Jars']):
				dest_folder = 'Jars'
			elif file.endswith(DIRS['Logs']):
				dest_folder = 'Logs'
			elif file.endswith(DIRS['ISO Images']):
				dest_folder = 'ISO Images'
			elif file.endswith(DIRS['Linux Repos']):
				dest_folder = 'Linux Repos'
			elif file.endswith(''):
				dest_folder = 'Random'
			cur_src = '%s' % file
			destination = '%s\\%s\\%s' % (DIRECTORY_TO_MANAGE, dest_folder, file)
			print('Moving %s to %s' % (cur_src, destination))
			shutil.move(cur_src, destination)
		# this is the break I was talking about.
		break

def post_manage():
	print('%s managed. Enjoy your day! :)' % DIRECTORY_TO_MANAGE)

pre_manage()
ensure_directories_exist()
transfer_files()
post_manage()