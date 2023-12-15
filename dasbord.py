import dash
from dash import dcc, html, dash_table
import pandas as pd
import plotly.express as px


df_schedule = pd.read_csv('your_data.csv')
df_schedule['Дата'] = pd.to_datetime(df_schedule['Дата'])

df_game_location = pd.read_csv('poligon.csv')

df_popular_gear = pd.read_csv('popular airsoft weapons.csv')
df_popular_equipment = pd.read_csv('popular_airsoft_equipment.csv')


app = dash.Dash(__name__)


app.layout = html.Div([
    html.H1("Страйкбол"),


    html.H2("Время занятий с тренерами"),


    dash_table.DataTable(
        id='coach-schedule-table',
        columns=[
            {'name': col, 'id': col} for col in df_schedule.columns
        ],
        data=df_schedule.to_dict('records'),
        style_table={'height': '400px', 'overflowY': 'auto'},
        editable=True
    ),


    dcc.Graph(
        id='game-location-map',
        figure=px.scatter_mapbox(
            df_game_location,
            lat='Широта',
            lon='Долгота',
            hover_name='Место игры',
            title='Распределение игр в Комсомольске-на-Амуре',
            mapbox_style="open-street-map",
            zoom=10
        )
    ),


    dcc.Graph(
        id='popular-gear-bar-chart',
        figure=px.bar(
            df_popular_gear,
            x='Тип',
            y='Количество',
            color='Тип',
            title='Популярное оружие для страйкбола',
            labels={'Количество': 'Количество участников'}
        )
    ),


    dcc.Graph(
        id='popular-equipment-pie-chart',
        figure=px.pie(
            df_popular_equipment,
            names='Тип',
            values='Количество',
            title='Популярное снаряжение для страйкбола'
        )
    ),


    dcc.RangeSlider(
        id='date-slider',
        min=df_schedule['Дата'].min().timestamp(),
        max=df_schedule['Дата'].max().timestamp(),
        marks={str(date.timestamp()): str(date) for date in df_schedule['Дата'].unique()},
        step=None,
        value=[df_schedule['Дата'].min().timestamp(), df_schedule['Дата'].max().timestamp()]
    ),


    dcc.Dropdown(
        id='weapon-type-dropdown',
        options=[
            {'label': weapon_type, 'value': weapon_type} for weapon_type in df_popular_gear['Тип'].unique()
        ],
        multi=True,
        value=df_popular_gear['Тип'].unique()
    )
])


if __name__ == '__main__':
    app.run_server(debug=True)
