"""
File: display.py
Author: Zachary King

Description: Creates display(s) for the exoplanet
data using the bokeh library.
"""

from bokeh.models import ColumnDataSource, TapTool, HoverTool, Toggle, OpenURL
from bokeh.plotting import figure, output_file, show

output_file('index.html')

def foo(y):
    print(y)

plot = figure(width=600, height=600, tools='tap', 
    title='Exoroam - Map of the Universe')

source = ColumnDataSource(data=dict(
    x=[1,2,3], 
    y=[1,2,3], 
    size=30, 
    color=['blue', 'red', 'green']
))

plot.circle('x', 'y', color='color', size=20, source=source)


tap = TapTool(label='SELECT')
tap.callback

show(plot)