# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.


from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash()

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.read_csv('pink_morsel_sales.csv')

df['date'] = pd.to_datetime(df['date'])

start_date = '2021-01-01'
end_date = '2021-01-31'
filtered_df = df[(df['date'] >= start_date) & (df['date'] <= end_date)]


fig = px.line(filtered_df, x='date', y='sales',title='Daily Sales Over Time')

app.layout = html.Div(children=[
    html.H1("Pink Morsel Sales",
    id="header"),

    dcc.Graph(
        id='line-chart',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)
