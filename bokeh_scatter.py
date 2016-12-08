import pandas as pd
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource, HoverTool, Div, BoxZoomTool, ResetTool
from bokeh.embed import file_html


def bokeh_scatter(df):

        output_file("tube_map.html", title="Tube Map")

        desc = Div(text=open("description.html", 'r').read(), width=800)

        source = ColumnDataSource(data=dict(x=[], y=[], 
                name=[], colour=[]))

        source.data = dict(
                x = df['X'],
                y = df['Y'],
                name=df['Name'],
                colour = df['Colour'],
        )

        hover = HoverTool(tooltips=[
                ("Name", "@name"),
        ])

        p = figure(plot_width=1200, plot_height=800,
           title='Travel Time Tube Map', toolbar_location="below", 
           tools=[hover, BoxZoomTool(),ResetTool()])


        p.circle(x='x', y='y', size=7, color='colour', 
                source=source, line_color=None)

        
        show(p)
