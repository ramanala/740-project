#! /usr/bin/env python

from zplot import *

c = postscript(title='failure.eps', dimensions=['3.5in','3.2in'])
d = drawable(canvas=c, yrange=[0,14], xrange=[0,25], coord=[75, 100],
             dimensions=['2.5in','1.8in'])
t = table(file='failure3.plot')

p = plotter()
L = legend()

# num name misc docfail dirstate repo inaccessible loss silent 
p.horizontalbars(drawable=d, table=t, yfield='num', xfield='silent', fill=True,
                 fillcolor='black', fillstyle='dline1', fillsize=1.0,
                 barwidth=0.5, linewidth=1, legend=L, legendtext='Silent Corruption')
p.horizontalbars(drawable=d, table=t, yfield='num', xfield='loss', fill=True,
                 fillcolor='black',
                 barwidth=0.5, linewidth=1, legend=L, legendtext='Data Loss')
p.horizontalbars(drawable=d, table=t, yfield='num', xfield='inaccessible', fill=True,
                 fillcolor='dimgray',
                 barwidth=0.5, linewidth=1, legend=L, legendtext='Inaccessible')
p.horizontalbars(drawable=d, table=t, yfield='num', xfield='repo', fill=True,
               fillcolor='gray',
               barwidth=0.5, linewidth=1, legend=L, legendtext='Repo Corruption ')
p.horizontalbars(drawable=d, table=t, yfield='num', xfield='dirstate', fill=True,
               fillcolor='darkgray',
               barwidth=0.5, linewidth=1, legend=L, legendtext='Dirstate Corruption')
p.horizontalbars(drawable=d, table=t, yfield='num', xfield='docfail', fill=True,
                 fillcolor='lightgrey', 
                 barwidth=0.5, linewidth=1, legend=L, legendtext='Documented Failure')
p.horizontalbars(drawable=d, table=t, yfield='num', xfield='misc',
               fill=True, fillcolor='white',  
               barwidth=0.5, linewidth=1, legend=L, legendtext='Misc')

axis(drawable=d, style='xy',
     ymanual=[['BDB-BTree',13],['BDB-Hash',12],['LevelDB-1.10',11],['LevelDB-1.15',10],['LMDB',9],['GDBM',8],
              ['HSqlDB',7], ['SQLite-R',6], ['VMWare', 5],
              ['Postgres',4], ['Git', 3], ['Mercurial',2], ['HDFS',1]
             ],
     xlabelfontsize=10.0,
     linewidth=0.5,
     doymajortics=False,
     yauto=[0,60,10],
     xtitle='# static vulnerabilities', xtitlesize=10, xtitleshift=[-4,0])

#c.text(coord=d.map([1,-10]), text='Write', size=10, anchor='c,c')
#c.text(coord=d.map([2,-10]), text='Write', size=10, anchor='c,c')
#c.text(coord=d.map([3,-10]), text='Files', size=10, anchor='c,c')
#c.text(coord=d.map([4,-10]), text='Server', size=10, anchor='c,c')
#c.text(coord=d.map([5,-10]), text='Server', size=10, anchor='c,c')
c.text(coord=d.map([13,13]), text='Misc: Partial Read Failure', size=8, anchor='c,c')
#c.line(coord=([109,230], [105,230]), arrow=True)
c.text(coord=d.map([17,3]), text='Misc: Fsck and Reflog Errors', size=8, anchor='c,c')
#c.line(coord=([149,200], [145,200]), arrow=True)
c.text(coord=d.map([6.9,9]), text='Misc: Read-Only Error', size=8, anchor='c,c')
#c.line(coord=([92,107], [88,107]), arrow=True)
c.text(coord=d.map([9.5,1]), text='Misc: Chmod Atomicity', size=8, anchor='c,c')
#c.line(coord=([169,48], [165,48]), arrow=True)

#L.draw(drawable=d, coord=[0,15], skipnext=4, width=10, height=10, fontsize=12)
#L.draw(drawable=d, coord=[0,-2], skipnext=4, width=10, height=10, fontsize=8)
L.draw(drawable=d, coord=[-7,-4.3], skipnext=4, skipspace=110.0, width=10,
       height=10, fontsize=10)

c.render()
# num name misc    silent    cread pread pwrite fread fwrite 
