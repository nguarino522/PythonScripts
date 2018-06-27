import os

for root, dirs, files in os.walk("/datto/array1/owncloud/dd-itcl.dattodrive.com/data/", topdown=True):
    if root == "* ":
        print(root)