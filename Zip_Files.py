from zipfile import ZipFile
import os, shutil
import argh
from tqdm import tqdm

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

    for i, bookdir in enumerate(bookdirs): # tqdm(, desc=f"Processing books in {directory}", total=len(bookdirs) ):
        bookname = booknames[i]
        for j, (root, dirs, files) in enumerate(os.walk(os.path.join(directory, bookname))):
            if j==0:
                with ZipFile('{0}.zip'.format(os.path.join(directory, bookname)), 'w') as zip:
                    for file in tqdm(files, desc=f"    Book {str(i + 1)} of {str(tot_dirs)} {bookname}", total = len(files)):
                        if file.endswith(('.mp3', '.m4b', '.aa', '.aax', '.m4a', '.aac', '.m4p', '.ogg', '.wma', '.flac',
                                        '.alac', '.wav', 'm3u', '.py')):
                            test = os.path.join(directory, root, file)
                            zip.write(test, os.path.join(bookname,file))
        shutil.rmtree(bookdir)

if __name__ == "__main__":
    argh.dispatch_command(main)
