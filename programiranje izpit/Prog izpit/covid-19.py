import requests
import matplotlib.pyplot as plt
import numpy as np

data = requests.get("https://api.sledilnik.org/api/hospitals").json()
st_postelj = list()
st_vent = list()
datumi = list()
for i in range(len(data)):
    st_postelj.append(data[i]['overall']['beds']['total'])
    st_vent.append(data[i]['overall']['vents']['free'])
    datumi.append(str(data[i]['year']) + "-" + str(data[i]['month']) + "-" + str(data[i]['day']))

ind = np.arange(len(datumi))
width = 0.35

plt.figure()
fig, ax = plt.subplots()
rects1 = ax.bar(ind - width/2, st_postelj, width, label='Postelje')
rects2 = ax.bar(ind + width/2, st_vent, width, label='Ventilatorji')


ax.set_ylabel('Število (prostih) postelj in ventilatorjev')
ax.set_title('Datum')
plt.xticks(np.arange(min(ind), max(ind) + 1, len(datumi)//6))
plt.xticks(rotation=45)
ax.set_xticklabels(datumi[::len(datumi)//6])

ax.set_yscale('log')

ax.legend()


fig.savefig("covid-19.png")
