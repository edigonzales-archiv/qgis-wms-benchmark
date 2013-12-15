import matplotlib
matplotlib.use( "agg" )
import matplotlib.pyplot as plt
import pylab


t11 = [1, 2, 3, 4, 5, 6, 7]
t12 = [1, 2, 4, 8, 16, 32, 64]

## AV-WMS (farbig)
#filename = "avwms_bench_resp"
#title = "AV-WMS (farbig)"
#direkt = [24, 16, 16, 20, 15, 31, 31]
#embedded = [21, 21, 18, 16, 20, 29, 28]
#wms = [41, 55, 30, 30, 84, 69, pylab.nan]

## Plan fuer das Grundbuch
#filename = "grundbuchplan_bench_resp"
#title = "Grundbuchplan"
#direkt = [20, 16, 15, 15, 22, 23, 25]
#embedded = [24, 15, 16, 19, 17, 22, 27]
#wms = [36, 39, 35, 31, 68, 75, pylab.nan]

## Basisplan
#filename = "basisplan_bench_resp"
#title = "Basisplan"
#direkt = [11, 10, 7, 8, 10, 12, 18]
#embedded = [12, 11, 7, 14, 14, 17, 17]
#wms = [37, 35, 24, 29, 41, pylab.nan, pylab.nan]

## Orthofoto
#filename = "orthofoto_bench_resp"
#title = "Orthofoto"
#direkt = [70, 70, 50, 70, 54, 77, 104]
#embedded = [73, 69, 52, 50, 37, 79, 91]
#wms = [113, 140, 89, 140, 205, pylab.nan, pylab.nan]

# Kombination
filename = "kombination_bench_resp"
title = "Kombination"
direkt = [64, 67, 54, 55, 123, 100, 99]
embedded = [69, 52, 67, 67, 106, 37, 48]
wms = [174, 146, 157, 281, 224, pylab.nan, pylab.nan]

plt.plot(t11, direkt,  marker='s', color='b', label='direkt', linewidth='2')
plt.plot(t11, embedded, marker='o', color='y', label='embedded', linewidth='2')
plt.plot(t11, wms, marker='^', color='m', label='wms', linewidth='2')

plt.xlabel('N Requests')
plt.ylabel('Min. Resp. Time (ms)')
plt.title(title)
plt.legend(bbox_to_anchor=(0.02, 0.98), loc=2, borderaxespad=0.)

plt.xticks( [1, 2, 3, 4, 5, 6, 7],  t12 )
plt.ylim([0, 300])

plt.grid(b=True, which='major', linestyle='dotted') 

plt.savefig('./'+filename+'.png', dpi=100)
