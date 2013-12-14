import matplotlib
matplotlib.use( "agg" )
import matplotlib.pyplot as plt
import pylab


t11 = [1, 2, 3, 4, 5, 6, 7]
t12 = [1, 2, 4, 8, 16, 32, 64]

# AV-WMS (farbig)
filename = "avwms_bench"
direkt = [5.5, 10.9, 12.8, 21.4, 22.8, 29.9, 31.5]
embedded = [5.3, 10.4, 15.4, 19.8, 21.6, 30.4, 31.9]
wms = [4.0, 5.7, 8.6, 9.7, 5.8, 1.9, pylab.nan]

square = [1.0, 4.0, 9.0, 16.0, 25.0, pylab.nan, pylab.nan]



plt.plot(t11, direkt,  marker='s', color='b', label='direkt', linewidth='2')
plt.plot(t11, embedded, marker='o', color='y', label='embedded', linewidth='2')
plt.plot(t11, wms, marker='^', color='m', label='wms', linewidth='2')

plt.xlabel('N Requests')
plt.ylabel('Throughput (Req/s)')
plt.title('AV-WMS (farbig)')
plt.legend(bbox_to_anchor=(0.02, 0.98), loc=2, borderaxespad=0.)

plt.xticks( [1, 2, 3, 4, 5, 6, 7],  t12 )
plt.ylim([0, 40])

plt.grid(b=True, which='major', linestyle='dotted') 

plt.savefig('./'+filename+'.png', dpi=100)
