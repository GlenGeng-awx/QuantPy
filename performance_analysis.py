import plotly.graph_objects as go
from plotly.subplots import make_subplots

# (client_num, tps, avg_latency, p99_latency)
data = [
    (5, 450, 11, 16),
    (10, 870, 12, 18),
    (15, 1360, 11, 18),
    (20, 1700, 11, 20),
    (25, 2300, 10, 21),
    (30, 2800, 11, 21),
    (35, 3200, 11, 27),
    (40, 3600, 12, 30),
    (45, 3900, 11, 33),
    (50, 4300, 12, 36),
    (60, 5000, 12, 41),
    (70, 4900, 14, 54),
    (80, 5700, 14, 58),
    (90, 6300, 16, 60),
    (100, 6700, 15, 59),
    (150, 6400, 24, 83),
    (200, 6500, 30, 108),
    (250, 6400, 32, 110),
]

fig = make_subplots(specs=[[{"secondary_y": True}]])

fig.add_trace(
    go.Scatter(
        name='Avg Latency',
        x=[row[0] for row in data],
        y=[row[2] for row in data],
        mode='markers+lines',
        marker_color='blue',
    ),
    secondary_y=True,
)

fig.add_trace(
    go.Scatter(
        name='P99 Latency',
        x=[row[0] for row in data],
        y=[row[3] for row in data],
        mode='markers+lines',
        marker_color='red',
    ),
    secondary_y=True,
)

fig.add_trace(
    go.Scatter(
        name='TPS',
        x=[row[0] for row in data],
        y=[row[1] for row in data],
        mode='markers+lines',
        marker_color='black',
    ),
    secondary_y=False,
)

fig.add_vline(x=100, line_dash="dash")

fig.update_layout(
    title='Transfer between Two Accounts',
    # hovermode="x",
    hovermode="x unified",
    # width=2000,
    # height=1000,
)

# fig.update_xaxes(title_text="TPS", range=[0, 8000])
# fig.update_yaxes(title_text="Latency in Milliseconds", range=[0, 200], secondary_y=False)
# fig.update_yaxes(title_text="Parallelism", range=[0, 100], secondary_y=True)

fig.update_xaxes(title_text="Client Num", dtick=5)
fig.update_yaxes(title_text="TPS", secondary_y=False)
fig.update_yaxes(title_text="Latency in Milliseconds", secondary_y=True)

fig.show()
# fig.write_html("./fileX.html")
# fig.write_image("./fileY.svg")
