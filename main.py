from distutils.dir_util import copy_tree

# copy subdirectory example


import os.path


def diff(list1, list2):
    list_difference = [item for item in list1 if item not in list2]
    return list_difference


def foo():
    print("New dive introduced")


def ham():
    print("Drive disconnected")


dl = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
drives = ['%s:' % d for d in dl if os.path.exists('%s:' % d)]
print(drives)
while True:
    uncheckeddrives = ['%s:' % d for d in dl if os.path.exists('%s:' % d)]
    x = diff(uncheckeddrives, drives)
    if x:
        from_directory = x[0]+"\\"
        to_directory = "D:\copy"
        copy_tree(from_directory, to_directory)
        
        print("New drives:     " + str(x))
        print(from_directory)
        foo()
    x = diff(drives, uncheckeddrives)
    if x:
        print("Removed drives: " + str(x))
        ham()
    drives = ['%s:' % d for d in dl if os.path.exists('%s:' % d)]
