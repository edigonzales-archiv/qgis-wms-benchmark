import matplotlib
matplotlib.use( "agg" )
import matplotlib.pyplot as plt
#import matplotlib.font_manager as fm

import pylab

#prop = fm.FontProperties(fname='/usr/share/fonts/truetype/FrutigerLTCom/FrutigerLTCom-Condensed.ttf')


t11 = [1, 2, 3, 4, 5, 6, 7]
t12 = [1, 2, 4, 8, 16, 32, 64]

area = [3.14159, 12.56636, 28.27431, 50.26544, 78.53975, 113.09724, 50]
square = [1.0, 4.0, 9.0, 16.0, 25.0, pylab.nan, pylab.nan]
#plt.plot(t11, area, label='Circle')
plt.plot(t11, square, marker='o', linestyle='--', color='r', label='Square', linewidth='2')

#plt.xticks(range(len(t12)), t12)



#plt.show()
#fig = plt.gcf()
#fig.set_size_inches(18.5,10.5)

#fig = plt.figure()
#ax1 = fig.add_subplot(1, 1, 1, axisbg='grey')
#ax1.plot(t11, area, 'c', linewidth=2.3)

#fig, ax = plt.subplots()
#ax.set_title('Text in a cool font', fontproperties=prop, size=20)
#ax.plot(t11, square, marker='o', linestyle='--', color='r', label='Square', linewidth='2')


plt.xlabel('Radius/Side')
plt.ylabel('Area')
plt.title('Area of Shapes')
plt.legend()

plt.xticks( [1, 2, 3, 4, 5, 6, 7],  t12 )

plt.ylim([0, 50])

plt.grid(b=True, which='major', linestyle='dotted') 
plt.grid(b=True, which='minor', linestyle='dashed') 

plt.savefig('./test.png', dpi=100)
