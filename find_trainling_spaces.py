import os
import glob

#for root, dirs, files in os.walk("/datto/array1/owncloud/dd-itcl.dattodrive.com/data/", topdown=True):
#    if "* " in root:
#        print(root)



space_list = glob.glob('/datto/array1/owncloud/dd-itcl.dattodrive.com/data/* ')

for i in space_list:
    print i

    