from zipfile import ZipFile
import os, shutil
import argh
from tqdm import tqdm, trange

# TODO Make sure that if the zip files are already there the program skips the book or stops
def main(directory=None):
    # TODO Test to make sure this works when no argument is given
    if directory is None:
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
                    # TODO Implement progress bars using TQDM.  Refer to https://www.youtube.com/watch?v=eILeIEE3C8c&t=311s
                    print('\tNow zipping book ' + str(i + 1) + ' of ' + str(tot_dirs) + ': ' + bookname)
                    # print(zip.filename)
                    for file in files:
                        if file.endswith(('.mp3', '.m4b', '.aa', '.aax', '.m4a', '.aac', '.m4p', '.ogg', '.wma', '.flac',
                                        '.alac', '.wav', 'm3u', '.py')):
                            # print('\t\t',os.path.join(directory,root,file))
                            test = os.path.join(directory, root, file)
                            zip.write(test, os.path.basename(test))
        shutil.rmtree(bookdir)

if __name__ == "__main__":
    argh.dispatch_command(main)
