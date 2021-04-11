from zipfile import ZipFile
import os, shutil

directory = os.getcwd()

print('This will zip all of the files in each subdirectory of ' + directory + ' into their own zip file')
booknames = []
bookdirs = []
for root, dirs, files in os.walk(directory):
    if root == directory:
        tot_dirs = len(dirs)
        tot_files = len(files)
        for i, name in enumerate(dirs):
            bookname = name
            booknames.append(bookname)
            bookdir = os.path.join(root, name)
            bookdirs.append(bookdir)

for i, bookdir in enumerate(bookdirs):
    bookname = booknames[i]
    for j, (root, dirs, files) in enumerate(os.walk(bookname)):
        if j==0:
            with ZipFile('{0}.zip'.format(os.path.join(directory, bookname)), 'w') as zip:
                print('\tNow zipping book ' + str(i + 1) + ' of ' + str(tot_dirs) + ': ' + bookname)
                # print(zip.filename)
                for file in files:
                    if file.endswith(('.mp3', '.m4b', '.aa', '.aax', '.m4a', '.aac', '.m4p', '.ogg', '.wma', '.flac',
                                      '.alac', '.wav', 'm3u', '.py')):
                        # print('\t\t',os.path.join(directory,root,file))
                        test = os.path.join(directory, root, file)
                        zip.write(test, os.path.basename(test))
    shutil.rmtree(bookdir)
