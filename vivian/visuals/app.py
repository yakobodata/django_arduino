import dash

import dash_core_components as dcc

import dash_html_components as html

import pandas as pd


data = pd.read_csv("motion_data.csv")

# data = data.query("type == 'conventional' and region == 'Albany'")

data["date"] = pd.to_datetime(data["date"], format="%Y-%m-%d")

data.sort_values("date", inplace=True)


app = dash.Dash(__name__)
server = app.server
app.layout = html.Div(

    children=[

        html.H1(children="Game play Analytics",),

        html.P(

            children=" Game consoles A",

        ),

        dcc.Graph(

            figure={

                "data": [

                    {

                        "x": data["time"],

                        "y": data["status"],

                        "type": "lines",

                    },

                ],

                "layout": {"title": "Gaming"},

            },

        ),

        # dcc.Graph(

        #     figure={

        #         "data": [

        #             {

        #                 "x": data["date"],

        #                 "y": data["time"],

        #                 "type": "lines",

        #             },

        #         ],

        #         "layout": {"title": "Motion data of Game play"},

        #     },

        # ),

    ]

)


if __name__ == "__main__":

    app.run_server(debug=True)
