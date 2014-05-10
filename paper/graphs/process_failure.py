#!/usr/bin/python
import os

all_list = [] 

f = open("failure2.tsv")
for line in f:
    vlist = []
    strs = line.split()

    name = strs[0]
    corrupt_read = strs[1]
    silent = strs[2]
    inaccessible = strs[3]
    read_only = strs[4]
    partial_read = strs[5]
    doc_fail = strs[6]
    fsck = strs[7]
    repo = strs[8]
    dirstate = strs[9]
    chmod = strs[10]
    reflog = strs[11]

    if not corrupt_read.isdigit():
        print line
        continue

    misc = str(int(fsck) + int(chmod) + int(reflog) + int(read_only) +
               int(partial_read))

    vlist.append(name ) 
    vlist.append(misc) 
    vlist.append(doc_fail ) 
    vlist.append(dirstate ) 
    vlist.append(repo ) 
    vlist.append(inaccessible ) 
    vlist.append(silent ) 
    vlist.append(corrupt_read ) 
    all_list.append(vlist)

rn = 1
for listx in reversed(all_list):
    ans = str(rn) + " " 
    # need to provide stacked numbers
    total_vul = 0

    for i, x in enumerate(listx):
        if i == 0:
            ans += x + " "

        if i:
            ans += "  "
        
        if i and str(x) != "-":
            total_vul += int(str(x))
        #else:
            #ans += " 0 "
        if i:    
            ans += str(total_vul)

    print ans     
    rn += 1



