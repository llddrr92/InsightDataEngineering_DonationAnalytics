
import os

abs_dir = os.path.dirname(__file__)

rel_in_path = "../input/itcont.txt"
path_to_in_file = os.path.join(abs_dir, rel_in_path)

rel_out_path = "../output/repeat_donors.txt"
path_to_out_file = os.path.join(abs_dir, rel_out_path)


#cwd = os.getcwd()
# # base_path = "Desktop"
#filename = "../input/itcont.txt"
#path_to_file = os.path.join(filename)
#path_to_file = os.path.join(cwd, filename)

# testdata = open(path_to_file , 'r')


data_matrix = []

with open(path_to_in_file) as f:
    for line in f:
        
        line_split = line.split('|',50)
        CMTE_ID = line_split[0]
        NAME = line_split[7]
        ZIP_CODE = line_split[10]
        TRANSACTION_DT = line_split[13]
        TRANSACTION_AMT = line_split[14]
        OTHER_ID = line_split[15]
        
        # Delete entity contribution
        if (OTHER_ID):
            continue
        
        data_line = [CMTE_ID, NAME, ZIP_CODE, TRANSACTION_DT, TRANSACTION_AMT, OTHER_ID]
        
        
        data_matrix.append(data_line)
        
        print data_line

print("\n")
print data_matrix

# print data_matrix[0][2]
        



# Process sequentially for repeated donors





out_file = open(path_to_out_file, 'w') 

for data_line in data_matrix:
    data_line_text = data_line[0] + '|' + data_line[1] + '|' + data_line[2] + '|' + data_line[3] + '|' + data_line[4] + '|' + data_line[5] + '\n'
    out_file.write(data_line_text) 

out_file.close() 
