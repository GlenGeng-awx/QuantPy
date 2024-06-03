import plotly.graph_objects as go
from plotly.subplots import make_subplots

avg_latency = {
    'tps':     [100, 300, 500, 700, 900, 1000, 2000, 3000, 4000, 5000, 6000, 7000],
    'latency': [9,   11,  12,  13,  14,  15,   20,   21,   25,   27,   31,   38],
}

p99_latency = {
    'tps':     [100, 300, 500, 700, 900, 1000, 2000, 3000, 4000, 5000, 6000, 7000],
    'latency': [19,  21,  22,  23,  24,  25,   30,   31,   35,   37,   41,   48],
}

parallelism = {
    'tps':        [100, 300, 500, 700, 900, 1000, 2000, 3000, 4000, 5000, 6000, 7000],
    'client_num': [5,   10,  20,  25,  30,  35,   40,   45,   50,   55,   60,   70],
}

fig = make_subplots(specs=[[{"secondary_y": True}]])

fig.add_trace(
    go.Scatter(
        name='Avg Latency',
        x=avg_latency['tps'],
        y=avg_latency['latency'],
        mode='markers+lines',
        marker_color='blue',
    ),
    secondary_y=False,
)

fig.add_trace(
    go.Scatter(
        name='P99 Latency',
        x=p99_latency['tps'],
        y=p99_latency['latency'],
        mode='markers+lines',
        marker_color='red',
    ),
    secondary_y=False,
)

fig.add_trace(
    go.Scatter(
        name='Parallelism',
        x=parallelism['tps'],
        y=parallelism['client_num'],
        mode='markers+lines',
        marker_color='black',
    ),
    secondary_y=True,
)

fig.update_layout(
    title='Transfer between Two Accounts',
    # hovermode="x",
    hovermode="x unified",
    width=2000,
    height=1000,
)

# fig.update_xaxes(title_text="TPS", range=[0, 8000])
# fig.update_yaxes(title_text="Latency in Milliseconds", range=[0, 200], secondary_y=False)
# fig.update_yaxes(title_text="Parallelism", range=[0, 100], secondary_y=True)

fig.update_xaxes(title_text="TPS")
fig.update_yaxes(title_text="Latency in Milliseconds", secondary_y=False)
fig.update_yaxes(title_text="Parallelism", secondary_y=True)

# fig.show()
fig.write_html("./fileX.html")
fig.write_image("./fileY.svg")
