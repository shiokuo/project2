#郭先生&劉先生
import numpy as np
import matplotlib.pyplot as plt 
from mpl_toolkits import mplot3d
#file_gpx=open('3148203-4.txt')
#line=file_gpx.readline().strip()

file_gpx=[]
with open ('3148203.gpx') as gps:
    for line in gps:
        file_gpx.append(line.strip())

while file_gpx[0]!='<trkseg>':
    file_gpx.pop(0)
inf=[]
for line in file_gpx:
    if line.startswith ('<trkpt'):
        l=line.split()       
        lat=l[1][5:-1]
       #lat.strip('\"')
        lon=l[2][5:-2]
        inf.append(float(lat))
        inf.append(float(lon))
    if line.startswith('<ele>'):
        ele=float(line[5:-6])
        inf.append(ele)
    if line.startswith('<time>'):
        time_s=''
        hour=line[17:19]
        minu=line[20:22]
        sec=line[23:25]
        time_s=time_s+hour+minu+sec
        time_n=int(time_s)
        
        #time=[]
        #time.append(time_n)
        
        inf.append(time_n)
    if line.startswith('<hdop>'):
        hdop=float(line[6:-7])
        inf.append(hdop)
    if line.startswith('<speed>'):
        speed=float(line[7:-8])
        inf.append(speed)
#print(inf)
#上面修好才有下面
long=int(len(inf)/6)
data=np.ones((long,6))
index=0
row=0
while index<len(inf)-5:
    data[row,0]=inf[index]
    data[row,1]=inf[index+1]
    data[row,2]=inf[index+2]
    data[row,3]=inf[index+3]
    data[row,4]=inf[index+4]
    data[row,5]=inf[index+5]
    row+=1
    index+=6

#print(data)

#still something to do


#data=np.ones((77,6))
#index=0
#for line in file_gpx:
#    inf=line.strip().split()           #this part may be deleted
#    data[index,:]=[
#        float(inf[0]), #lat
#        float(inf[1]), #lon
#        float(inf[2]), #ele
#        int(inf[3]), #time
#        float(inf[4]), #hdop
#        float(inf[5])  #speed
#    ]
#    index+=1
#曾先生
x=data[:,1]
y=data[:,0]
z=data[:,2]
v=data[:,5]
hdop=data[:,4]
ax = plt.axes(projection='3d')
bar=ax.scatter3D(x,y,z,c=v,cmap='YlOrRd',s=hdop**4,marker='>',label='size:hdop\ncolor:v')
xLabel = ax.set_xlabel('longtitude')
yLabel = ax.set_ylabel('latitude')
zLabel = ax.set_zlabel('elevatiion')
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
#ax.text(0.9,0.9,0,transform=r.transFigure,s='velocity')
for timespan in range(0,9):
    ax.text(x2[timespan],y2[timespan],z2[timespan],s='t=%d'%(t2[timespan]-t2[0]))

#劉先生
for index in range(1,77,1):
    acc=np.array((data[index-1,:]+data[index+1,:]-2*data[index,:])/25)
    linedot=[]
    for dot in range(0,3):
        linedot.append(data[index,:]+dot*acc[:]*10)
        #linedot.append((data[index,:]+data[index+1,:])/2+10*dot*acc[:]/3)
    #if acc[:,1]**2+acc[:,2]**2+acc[:,0]**2 >100:
        #print(data[index-1,:],data[index,:],data[index+1,:])
        
    acc_draw=np.array(linedot)
    #print(acc_draw)
    ax.plot3D(acc_draw[:,1],acc_draw[:,0],acc_draw[:,2],color='green')
ax.plot3D(acc_draw[:,1],acc_draw[:,0],acc_draw[:,2],color='green',label='acc in 10s')
plt.legend()
plt.show()



