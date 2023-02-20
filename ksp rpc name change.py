import re
import numpy as np
#read and parse file for use
craft=open(r"reuseable.craft",'r+')
posvals=[]
data=craft.read()
clist=data.split("\n")
#iterate per line
for i in range(len(clist)):
    #find index of start of part
    if (clist[i]=='PART'):
        #if a vector engine
        if(re.search("SSME",clist[i+2])):
            #grab values
            pos=clist[i+5].split(' ')[-1].split(',')
            posvals.append(pos)
#do math with pos data, find delta and min/max 
posvals=np.array(posvals,dtype=np.float32)
delta=(posvals[0]-posvals[1])[0]
posvalsi=(posvals/delta).round().astype(np.int8)
mi=np.amin(posvalsi,axis=0)
#debugging, good to have but not needed
ma=np.amax(posvalsi,axis=0)
finind=posvalsi[:,0:3:2]-[mi[0],mi[2]]
print(mi,ma)
#final edit
for i in range(len(clist)):
    #find index of start of part
    if (clist[i]=='PART'):
        clist[i]=clist[i]+"\n"
        #if a vector engine
        if(re.search("SSME",clist[i+2])):
            #fun code
            pos=(np.array(clist[i+5].split(' ')[-1].split(','),dtype=np.float32)/delta).round().astype(np.int8)[0:3:2]-[mi[0],mi[2]]
            #gives a string to the 'tag' of the engine. becomes parseable in krpc/kos
            clist[i+202]="		nameTag =" + str(pos[0]) + "," + str(pos[1]) 
    else:
        #bring the tab back in
        clist[i]=clist[i]+"\n"
#new craft file name
with open('reuseable2.craft', 'w') as file:
    file.writelines( clist )
