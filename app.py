from flask import Flask, render_template
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys
import plotly
import plotly.graph_objects as go
import json
import csv

app = Flask(__name__)


# df = pd.read_csv('iris.csv')

# _x = df['sp']
# _y = df['x2']
# _z = df['x1']
# _a = df['y1']


#########################################################
#generate sample data#
#########################################################

pie = {
        'x': [40, 50, 30, 20],
        'y': [100, 50, 30, 20],
        'type': 'scatter',
        'name': 'Line1'
    }

pie2 = {
        'x': [40, 50, 30, 20],
        'y': [50, 50, 30, 20],
        'type': 'scatter',
        'name': 'Line2'
    }

graphs = [
        dict(
            data=[
                pie,pie2
            ],
            layout=dict(
                 autosize = True,
                xaxis = {
                    'title': 'X-axis Title',
                    'titlefont': { 'size':30 }
                    }              
            )
        )
    ]

# 序列化
graphJSON = json.dumps(graphs, cls=plotly.utils.PlotlyJSONEncoder)


def create_plot(_x, _y):# 要抽離
    # creating a sample dataframe
    # N = 40;x = np.linspace(0, 1, N);y = np.random.randn(N)
    # df = pd.DataFrame({'x': x, 'y': y}) 

    # using data creating json data
    data = [
        go.Line( x= _x,  #df['x'], # assign x as the dataframe column 'x'
                y= _y,
                name = 'x2'),
        go.Line( x= _x,  #df['x'], # assign x as the dataframe column 'x'
                y= _z,
                name = 'x1'), #df['y'])
        go.Line( x= _x,  #df['x'], # assign x as the dataframe column 'x'
                y= _a,
                name = 'y1') #df['y'])
           ]
    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

    # return format data
    return graphJSON

def create_layout():
    pass

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/plot')
def plot():
    # bar = create_plot(_x, _y)
    # bar2 = create_plot(_x, _z)
    # print(bar)
    # print('#'*30)

    # print('#'*30)
    
    return render_template('trial_plot.html', graphJSON = graphJSON)


if __name__ == '__main__':
    app.run(debug = True)
    
