import os

for root, dirs, files in os.walk("/datto/array1/owncloud/dd-itcl.dattodrive.com/data/", topdown=True):
    for name in files, dirs:
        print(os.path.join(root, name))