import sys
import re
import glob
#file_name = sys.argv[1]
file=glob.glob("*.txt")
print file
for file_name in file:
	with open(file_name,'r') as f:
		e=f.readline()
		replaced = re.sub(r'_',' ',e)
	with open(file_name, 'r') as fin:
    	 data = fin.read().splitlines(True)
	with open(file_name, 'w') as fout:
		fout.write(replaced)
	with open(file_name, 'a') as fou:
    	 fou.writelines(data[1:])
with open('H837566_T20170101_E20180409_Visit_Diagnosis.txt','r') as f:
		e=f.readline()
		replaced1 = re.sub(r' ','_',e)
	with open('H837566_T20170101_E20180409_Visit_Diagnosis.txt', 'r') as fun:
    	 data = fun.read().splitlines(True)
	with open('H837566_T20170101_E20180409_Visit_Diagnosis.txt', 'w') as fout:
		fout.write(replaced1)
	with open('H837566_T20170101_E20180409_Visit_Diagnosis.txt', 'a') as fou:
    	 fou.writelines(data[1:])



