from dash import Dash, html, dcc, Input, Output, callback
import plotly.express as px
import pandas as pd
import task4_styles as stl

DATA_PATH = "tabulated_sales.csv"

radio_items = ['north', 'south', 'west', 'east', 'all']

def visualize():

    df = pd.read_csv(DATA_PATH)

    # Sort the data so that it is in chronological order
    df = df.sort_values(by=['date'], ascending=True)

    # Create all the aspects of the application
    visualization = dcc.Graph(id='sales-chart')
    region_button = dcc.RadioItems(radio_items, 'all', id = 'region', inline=True, labelStyle= {'margin' :'1rem'}, style=stl.radio_style)
    header = html.H1(children='Pink Morsel Sales',style=stl.header_style)
    subtitle = html.Div(children='''The total sales for pink morsels and their respective dates.''', style=stl.subtitle_style)

    # Create callback to update when the radio button values get changed
    # Update the line chart to reflect the selected region
    @callback(
        Output('sales-chart', 'figure'),
        Input('region', 'value'))
    def update_chart(region):
        if region == 'all':
            filtered_df = df.groupby(['date'], as_index=False).agg({'sales': 'sum'})
            description = 'Pink Morsel Sales in all regions'
        else:
            filtered_df = df[df['region'] == region]
            description = 'Pink Morsel Sales in the {} region'.format(region)

        chart = px.line(filtered_df, x= 'date', y='sales', title=description)
        chart.update_layout(transition_duration=500, paper_bgcolor= stl.colors['background'], plot_bgcolor = stl.colors['plot_background'], font_color=stl.colors['text'], title_x = 0.5)
        return chart

    # Create App
    app = Dash()
    app.layout = html.Div(children=[header, subtitle, visualization, region_button], style=stl.app_style)
    app.run(debug=True)
    pass


if __name__ == "__main__":
    visualize()