import hashlib

def create_md5_list(input_path, output_path):
	with open(input_path)  as file:
	    with open(output_path)  as output:
	        for line in file: 
	           line=line.strip() 
	           # print hashlib.md5(line).hexdigest() 
	           output.write(hashlib.md5(line).hexdigest() +'\n')