import numpy as np


file_gpx=open('3148203-4.txt')
line=file_gpx.readline().strip()

data=np.ones((77,6))
index=0
for line in file_gpx:
    inf=line.strip().split()
    data[index,:]=[
        float(inf[0]), #lat
        float(inf[1]), #lon
        float(inf[2]), #ele
        int(inf[3]), #time
        float(inf[4]), #hdop
        float(inf[5])  #speed
    ]
    index+=1


