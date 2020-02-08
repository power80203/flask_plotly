from flask import Flask, render_template
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys
import plotly
import plotly.graph_objects as go
import json


app = Flask(__name__)

def create_plot():
    # creating a sample dataframe
    N = 40;x = np.linspace(0, 1, N);y = np.random.randn(N)
    df = pd.DataFrame({'x': x, 'y': y}) 
    
    # using data creating json data
    data = [
        go.Line( x=df['x'], # assign x as the dataframe column 'x'
                y=df['y'])
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
    bar = create_plot()
    print('#'*30)
    print(bar)
    print('#'*30)
    return render_template('trial_plot.html', plot = bar, plot2 = bar)


if __name__ == '__main__':
    app.run(debug = True)
    
