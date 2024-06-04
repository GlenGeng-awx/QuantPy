import plotly.graph_objects as go
from plotly.subplots import make_subplots

# (client_num, tps, avg_latency, p99_latency)
data_2 = [
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
        x=[row[0] for row in data_2],
        y=[row[2] for row in data_2],
        mode='markers+lines',
        marker_color='blue',
        line=dict(
            dash='dash'  # Options include 'solid', 'dash', 'dot', 'dashdot'
        )
    ),
    secondary_y=True,
)

fig.add_trace(
    go.Scatter(
        name='P99 Latency',
        x=[row[0] for row in data_2],
        y=[row[3] for row in data_2],
        mode='markers+lines',
        marker_color='red',
        line=dict(
            dash='dash'  # Options include 'solid', 'dash', 'dot', 'dashdot'
        )
    ),
    secondary_y=True,
)

fig.add_trace(
    go.Scatter(
        name='TPS',
        x=[row[0] for row in data_2],
        y=[row[1] for row in data_2],
        mode='markers+lines',
        marker_color='black',
        line=dict(
            dash='dash'  # Options include 'solid', 'dash', 'dot', 'dashdot'
        )
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

fig.update_xaxes(title_text="Concurrent Client Num", dtick=25)
fig.update_yaxes(title_text="TPS", dtick=500, secondary_y=False)
fig.update_yaxes(title_text="Latency in MS", dtick=10, secondary_y=True)

fig.show()
# fig.write_html("./fileX.html")
# fig.write_image("./fileY.svg")

# create graph
fig = make_subplots(rows=2, cols=2,
                    specs=[[{"secondary_y": True}, {"secondary_y": True}],
                           [{"secondary_y": True}, {"secondary_y": True}]])

# setup x/y axis and baseline
for row in [1, 2]:
    for col in [1, 2]:
        fig.update_xaxes(title_text="Concurrent Client Num", dtick=25, row=row, col=col)
        fig.update_yaxes(title_text="TPS", dtick=500, secondary_y=False, row=row, col=col)
        fig.update_yaxes(title_text="Latency in MS", dtick=10, secondary_y=True, row=row, col=col)

        fig.add_trace(
            go.Scatter(
                name='Avg Latency',
                x=[row[0] for row in data_2],
                y=[row[2] for row in data_2],
                mode='markers+lines',
                line=dict(width=0.75, dash='dot'),
                marker_size=3,
                marker_color='blue',
            ),
            row=row, col=col,
            secondary_y=True,
        )

        fig.add_trace(
            go.Scatter(
                name='P99 Latency',
                x=[row[0] for row in data_2],
                y=[row[3] for row in data_2],
                mode='markers+lines',
                line=dict(width=0.75, dash='dot'),
                marker_size=3,
                marker_color='red',
            ),
            row=row, col=col,
            secondary_y=True,
        )

        fig.add_trace(
            go.Scatter(
                name='TPS',
                x=[row[0] for row in data_2],
                y=[row[1] for row in data_2],
                mode='markers+lines',
                line=dict(width=0.75, dash='dot'),
                marker_size=3,
                marker_color='black',
            ),
            row=row, col=col,
            secondary_y=False,
        )

# divide the graph
fig.add_vline(x=100, line_dash="dash")

fig.update_layout(
    title='Firm Wallet Perf Test',
    hovermode="x unified",
)

fig.show()
