import os, glob

directories_traversed = []

def delete_all(root,extension):
    traverse(root,directories_traversed,extension)
    
def get_directories(root):
    return [os.path.abspath(f) for f in glob.glob(root+"/*") if os.path.isdir(f)]

def traverse(directory,directories_traversed,extension):
    directory = os.path.abspath(directory)
    if not directory in directories_traversed:
        delete(directory,extension)
        directories_traversed.append(directory)
        directories = get_directories(directory)
        for folder in directories:
            traverse(folder,directories_traversed,extension)
            
def delete(directory,extension):
    print directory
    filelist = glob.glob(directory+"/*"+extension)
    print filelist
    for f in filelist:
        f = os.path.abspath(f)
        print "deleting",f
        os.remove(f)
     
