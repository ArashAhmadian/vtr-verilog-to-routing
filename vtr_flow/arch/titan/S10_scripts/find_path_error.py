from typing import ContextManager
from path_parser import * 
import matplotlib.pyplot as plt
import itertools


wire_paths_errors_real=[]
wire_paths_errors_modelled=[]
w=open("error_check.txt",'w')

for index in range(len(path_lines)): 
	if path_lines[index].type == "PATH_START":
		line=path_lines[index+1]
		quartus_delay=0
		modelled_delay=0
		print("=================",file=w)
		while line.type in wire_types:
			if line.type == "LAB_RE" and line.switch_type is not None:
				quartus_delay=quartus_delay+line.delay
				modelled_delay=modelled_delay+cbo_results[dict[line.switch_type]]
			elif line.type== "LAB_LINE"and line.switch_type is not None:
				quartus_delay=quartus_delay+line.delay
				modelled_delay=modelled_delay+cbi_results[dict[line.switch_type]]
			elif line.type== "LEIM":
				quartus_delay=quartus_delay+line.delay
				modelled_delay=modelled_delay+leim_results
			else: 
				quartus_delay=quartus_delay+line.delay
				modelled_delay=modelled_delay+sb_results[dict[line.type]]
			print(line.routing_element,file=w)
			index=index+1
			line=path_lines[index+1]	
		if modelled_delay !=0: 
			wire_paths_errors_modelled.append(abs(quartus_delay-modelled_delay)/modelled_delay)
			wire_paths_errors_real.append(abs(quartus_delay-modelled_delay)/quartus_delay)
		
w.close()
print("Average Error wrt path reporting by Quartus, normalized to the actual delay:",sum(wire_paths_errors_real)/len(wire_paths_errors_real))
print("Average Error wrt path reporting by Quartus, normalized to the actual delay:",sum(wire_paths_errors_modelled)/len(wire_paths_errors_modelled))
print("###########################\n NO LEIM")
