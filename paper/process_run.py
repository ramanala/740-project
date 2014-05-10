#!/usr/bin/python
import os

all_list = [] 

f = open("rundata.txt")
for line in f:
    vlist = []
    strs = line.split()
    name = strs[0]
    checker_latency = float(strs[1])
    num_states = int(strs[2])
    num_calls = int(strs[3])
    num_syncs = int(strs[4])
    
    vlist.append(name)
    vlist.append(num_calls)
    vlist.append(num_syncs)
    vlist.append(num_states)
    vlist.append(checker_latency)
    vlist.append("%.0f" % ((checker_latency * num_states)/(60.0*60.0)))
    all_list.append(vlist)

all_list.sort(key=lambda x: float(x[5]))

for listx in all_list:
    ans = ""
    for i, x in enumerate(listx):
        if i:
            ans += " & "
        
        ans += str(x)
    
    ans += " \\\\ \\hline "    
    print ans     
