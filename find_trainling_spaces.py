import os

directory_list = list()

for root, dirs, files in os.walk("/datto/array1/owncloud/dd-itcl.dattodrive.com/data/", topdown=True):
    for name in dirs:
        directory_list.append(os.path.join(root, name))

print directory_list