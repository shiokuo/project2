#郭先生
import numpy as np
import matplotlib.pyplot as plt 
from mpl_toolkits import mplot3d
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
#曾先生
x=data[:,1]
y=data[:,0]
z=data[:,2]
v=data[:,5]
t=data[:,3]
ax = plt.axes(projection='3d')
bar=ax.scatter3D(x,y,z,c=v,cmap='YlOrRd',s=((-t+123000)/5)**(1/2))
xLabel = ax.set_xlabel('lon')
yLabel = ax.set_ylabel('lat')
zLabel = ax.set_zlabel('ele')
plt.xlim([2.32,2.36])
plt.ylim([48.747,48.754])
ax.set_zlim([-50,100])
plt.colorbar(bar)
data2=data[0::8,:]
x2=data2[:,1]
y2=data2[:,0]
z2=data2[:,2]
t2=data2[:,3]
#bar=ax.scatter3D(x2,y2,z2,c='green',s=(t2-120800)/20,alpha=0.8)
ax.set_title('route mapping')
#劉先生
plt.show()


