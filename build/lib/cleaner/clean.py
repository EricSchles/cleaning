import os, glob

directories_traversed = []

def delete_all(root,extension):
    traverse(root,directories_traversed,extension)
    
def get_directories(root):
    return [os.path.abspath(f) for f in glob.glob(root+"/*") if os.path.isdir(f)]

def traverse(directory,directories_traversed,extension):
    directory = os.path.abspath(directory)
    if not directory in directories_traversed:
        directories = delete(directory,extension)
        directories_traversed.append(directory)
        for folder in directories:
            return traverse(folder,directories_traversed,extension)
            
def delete(directory,extension):
    os.chdir(directory)
    filelist = glob.glob("*"+extension)
    for f in filelist:
        os.remove(f)
    directories = [os.path.abspath(f) for f in glob.glob("*") if os.path.isdir(f)]
    os.chdir("..")
    return directories
    
