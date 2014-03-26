#! /usr/bin/env python

from zplot import *

c = postscript(title='./timing.eps', dimensions=[200,450])
d = drawable(canvas=c, xrange=[0,16], yrange=[0,1], dimensions=[150,250], coord=[38,96])
t = table(file='./data.txt')
t.addcolumn(column='zero', value=0)
t.addcolumn(column='one',  value=1)

axis(drawable=d, style='y', ymanual=[ ['0%', 0], ['20%', 0.2], ['40%', 0.4], ['60%', 0.6], ['80%', 0.8], ['100%', 1.0]], ylabelfontsize=12)
axis(drawable=d, style='x', domajortics=False, xmanual=[ ['', 2.5]])

p = plotter()
L = legend()

lw = 0
bw = 2

# task names
p.points(drawable=d, table=t, xfield='c0', yfield='zero', style='label', labelfield='c1', labelrotate=90.0,
         labelanchor='r,c', labelsize=10.0, labelshift=[0,-5])

p.points(drawable=d, table=t, xfield='c0', yfield='one',  style='label', labelfield='c6', labelrotate=90.0,
         labelanchor='l,c', labelsize=10.0, labelshift=[0,+2])


p.verticalbars(drawable=d, table=t, xfield='c0', fill=True, barwidth=bw, yfield='c2',
    fillcolor='black', fillstyle='dline1',
    linewidth=lw, legendtext='Client Queuing', legend=L)

p.verticalbars(drawable=d, table=t, xfield='c0', fill=True, barwidth=bw, yfield='c3',
    stackfields=['c2'], fillcolor='black', bgcolor='white', fillstyle='dline12', fillsize=0.1, fillskip=5,
    linewidth=lw, legendtext='Incoming Browser', legend=L)

p.verticalbars(drawable=d, table=t, xfield='c0', fill=True, barwidth=bw, yfield='c4',
    stackfields=['c2','c3'], fillcolor='black', bgcolor='white', #fillstyle='dline1',
               fillsize=2, fillskip=3,
    linewidth=lw, legendtext='Incoming webserver', legend=L)

p.verticalbars(drawable=d, table=t, xfield='c0', fill=True, barwidth=bw, yfield='c5',
    stackfields=['c2','c3','c4'], fillcolor='0.5,0.5,0.5',
    linewidth=lw, legendtext='Incoming data', legend=L)


L.draw(drawable=d, coord=[-2.5,1.285], skipnext=5, skipspace=50, fontsize=7,
       order=[0,1,2,3], width=10, height=10)

c.render()
