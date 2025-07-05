from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

DATA_PATH = "tabulated_sales.csv"

def visualize():

    # Read csv and aggregate sales data for entries that have the same date
    df = pd.read_csv(DATA_PATH)
    df = df.groupby(['date'], as_index=False).agg({'sales': 'sum'})

    # Sort the data so that it is in chronological order
    df = df.sort_values(by=['date'], ascending=True)

    # Set up the line chart for the sales of overtime of pink morsels
    chart = px.line(df, x='date', y='sales', title='Pink Morsel Sales Over Time')
    visualization = dcc.Graph(id='sales-chart', figure=chart)
    header = html.H1(children='Pink Morsel Sales')
    subtitle = html.Div(children='''The total sales for pink morsels and their respective dates.''')

    # Create App
    app = Dash()
    app.layout = html.Div(children=[header, subtitle, visualization])
    app.run(debug=True)
    pass



if __name__ == "__main__":
    visualize()