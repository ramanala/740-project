#! /usr/bin/env python

from zplot import *

c = postscript(title='overall3.eps', dimensions=[340,185])
d = drawable(canvas=c, xrange=[0.5,7.5], yrange=[0,60], coord=[50,35],
             dimensions=[280,140])

t = table(file='overall3.plot')

p = plotter()
L = legend()
# earlyckpt mixed tx earlycommit
p.verticalbars(drawable=d, table=t, xfield='num', yfield='earlyckpt',
               fill=True, fillcolor='lightgrey',
               barwidth=0.5, linewidth=0, legend=L, legendtext='Early Checkpoint')
p.verticalbars(drawable=d, table=t, xfield='num', yfield='tx', fill=True, fillcolor='black',
               barwidth=0.5, linewidth=0, legend=L, legendtext='Transaction Misorder')
p.verticalbars(drawable=d, table=t, xfield='num', yfield='mixed', fill=True,
               fillcolor='gray',
               barwidth=0.5, linewidth=0, legend=L, legendtext='Mixed')
p.verticalbars(drawable=d, table=t, xfield='num', yfield='earlycommit', fill=True,
               fillcolor='darkgray',
               barwidth=0.5, linewidth=0, legend=L, legendtext='Early Commit')
p.verticalintervals(drawable=d, table=t, xfield='num', ylofield='devlo',
                    yhifield='devhi', devwidth=5, linewidth=0.5,
                    linecolor='dimgray')
               
axis(drawable=d, style='xy',
     xmanual=[['Seq',1],['Rand',2],['Create',3],['Web',4],['File',5],['Varmail',6],['MySQL',7],],
     xlabelfontsize=10.0,
     linewidth=0.5,
     doxmajortics=False,
     yauto=[0,60,10],
     ytitle='P (inconsistency)', ytitlesize=12, ytitleshift=[-4,0])

c.text(coord=d.map([1,-10]), text='Write', size=10, anchor='c,c')
c.text(coord=d.map([2,-10]), text='Write', size=10, anchor='c,c')
c.text(coord=d.map([3,-10]), text='Files', size=10, anchor='c,c')
c.text(coord=d.map([4,-10]), text='Server', size=10, anchor='c,c')
c.text(coord=d.map([5,-10]), text='Server', size=10, anchor='c,c')

L.draw(drawable=d, coord=[18,30], skipnext=4, width=10, height=10, fontsize=12)

c.render()
