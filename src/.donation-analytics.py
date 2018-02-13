
import os
# base_path = "Desktop"
filename = "itcont.txt"

path_to_file = os.path.join(filename)
#path_to_file = os.path.join(base_path, filename)
testdata = open(path_to_file , 'r')

print(testdata.read())