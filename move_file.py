import os
import shutil

from_dir = "C:/Users/Rohit/Downloads/"
to_dir = "C:/Users/Rohit/OneDrive/Documents/"

list_of_files = os.listdir(from_dir)

print(list_of_files)
#move all documents from downloads to pictures
for file in list_of_files:
    name,ext = os.path.splitext(file)
    print(name)
    print(ext)
    if ext == ' ':
        continue
    if ext in ['.txt','.pdf','.doc','.docx']:
        path1 = from_dir + '/' + file
        path2 = to_dir + '/' + 'documents'
        path3 = to_dir + '/' + 'documents' + '/' + file
        print('path1', path1)
        print('path3', path3)
    
    #check if folder or path exists before moving
    #else make a new folder or directory then move
        if os.path.exists(path2):
            print('moving ' + file + '... ')
            shutil.move(path1, path3)
        else :
            os.makedirs(path2)
            print('moving ' + file + '... ')
            shutil.move(path1, path3)