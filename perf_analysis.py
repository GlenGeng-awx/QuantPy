import plotly.graph_objects as go
from plotly.subplots import make_subplots

# data_str = """
# 10	1200	8	14	2400
# 20	2200	9	18	4400
# 30	3000	10	26	6000
# 40	3800	10	35	7600
# 50	4500	11	43	9000
# 60	4800	12	50	9600
# 70	5300	13	56	10600
# 80	5700	14	62	11400
# 90	6100	14	69	12200
# 100	7000	14	69	14000
# 150	7200	21	94	14400
# 200	7600	26	106	15200
# 250	7600	33	161	15200
# """
#
# data_lines = data_str.strip().split('\n')
# data_items = []
#
# for line in data_lines:
#     parts = line.split('\t')
#     if len(parts) == 5:
#         client_num = int(parts[0])
#         bao_tps = int(float(parts[1]))
#         avg_latency = int(float(parts[2]))
#         p99_latency = int(float(parts[3]))
#         ao_tps = int(float(parts[4]))
#         data_items.append((client_num, bao_tps, avg_latency, p99_latency, ao_tps))
#
# print(data_items)

# (client_num, bao_tps, avg_latency, p99_latency, ao_tps)
data_2 = [
    (10, 1200, 8, 14, 2400),
    (20, 2200, 9, 18, 4400),
    (30, 3000, 10, 26, 6000),
    (40, 3800, 10, 35, 7600),
    (50, 4500, 11, 43, 9000),
    (60, 4800, 12, 50, 9600),
    (70, 5300, 13, 56, 10600),
    (80, 5700, 14, 62, 11400),
    (90, 6100, 14, 69, 12200),
    (100, 7000, 14, 69, 14000),
    (150, 7200, 21, 94, 14400),
    (200, 7600, 26, 106, 15200),
    (250, 7600, 33, 161, 15200)
]

data_5 = [
    (10, 850, 11, 21, 4250),
    (20, 1600, 12, 27, 8000),
    (30, 2600, 12, 39, 13000),
    (40, 3100, 13, 45, 15500),
    (50, 3600, 14, 43, 18000),
    (60, 4500, 13, 49, 22500),
    (70, 4650, 15, 63, 23250)
]

data_10 = [
    (10, 980, 10, 19, 9800),
    (20, 1800, 12, 28, 18000),
    (30, 2400, 12, 30, 24000),
    (40, 2900, 14, 43, 29000),
    (50, 3200, 15, 48, 32000),
    (60, 3200, 18, 57, 32000),
    (70, 3180, 21, 65, 31800)
]

data_15 = [
    (10, 1100, 9, 17, 16500),
    (20, 1900, 11, 22, 28500),
    (30, 2300, 12, 29, 34500),
    (40, 2350, 16, 49, 35250),
    (50, 2450, 19, 49, 36750),
    (60, 2360, 22, 63, 35400)
]

data_20 = [
    (10, 1000, 10, 17, 20000),
    (20, 1500, 13, 29, 30000),
    (30, 1800, 16, 40, 36000),
    (40, 1850, 20, 48, 37000),
    (50, 1870, 25, 57, 37400)
]


def plot_bao2_data(fig: go.Figure, data, tag):
    fig.add_trace(
        go.Scatter(
            name=f'{tag} Avg Latency',
            x=[row[0] for row in data],
            y=[row[2] for row in data],
            mode='markers+lines',
            line=dict(width=1, dash='dash'),
            marker_size=4,
            marker_color='blue',
        ),
        secondary_y=True,
    )

    fig.add_trace(
        go.Scatter(
            name=f'{tag} P99 Latency',
            x=[row[0] for row in data],
            y=[row[3] for row in data],
            mode='markers+lines',
            line=dict(width=1, dash='dash'),
            marker_size=4,
            marker_color='purple',
        ),
        secondary_y=True,
    )

    fig.add_trace(
        go.Scatter(
            name=f'{tag} BatchAccountOp TPS',
            x=[row[0] for row in data],
            y=[row[1] for row in data],
            mode='markers+lines',
            line=dict(width=2),
            marker_size=8,
            marker_color='red',
        ),
        secondary_y=False,
    )

    fig.add_trace(
        go.Scatter(
            name=f'{tag} AccountOp TPS',
            x=[row[0] for row in data],
            y=[row[4] for row in data],
            mode='markers+lines',
            line=dict(width=2),
            marker_size=8,
            marker_color='green',
        ),
        secondary_y=False,
    )


# create graph for BAO 2
fig_bao2 = make_subplots(specs=[[{"secondary_y": True}]])

plot_bao2_data(fig_bao2, data_2, 'BAO 2')
fig_bao2.add_vline(x=100, line_dash="dash")

# setup graph layout
fig_bao2.update_xaxes(title_text="Concurrent Client Num", dtick=10, )
fig_bao2.update_yaxes(title_text="TPS", secondary_y=False)
fig_bao2.update_yaxes(title_text="Latency in ms", secondary_y=True)

fig_bao2.update_layout(
    title='Batch Account Operation (2 Accounts) V.S. Concurrent Client Num',
    hovermode="x unified",
    hoverlabel=dict(
        namelength=200
    )
)
fig_bao2.show()


def plot_bao_tps_data(fig: go.Figure, data, color, tag):
    fig.add_trace(
        go.Scatter(
            name=f'{tag} BatchAccountOp TPS',
            x=[row[0] for row in data],
            y=[row[1] for row in data],
            mode='markers+lines',
            line=dict(width=2),
            marker_size=8,
            marker_color=color,
        ),
        row=1, col=1,
    )


def plot_ao_tps_data(fig: go.Figure, data, color, tag):
    fig.add_trace(
        go.Scatter(
            name=f'{tag} AccountOp TPS',
            x=[row[0] for row in data],
            y=[row[4] for row in data],
            mode='markers+lines',
            line=dict(width=2),
            marker_size=8,
            marker_color=color,
        ),
        row=1, col=2,
    )


# create graph for TPS
fig_tps = make_subplots(rows=1, cols=2)

plot_bao_tps_data(fig_tps, data_2[:10], 'black', 'BAO 2')
plot_bao_tps_data(fig_tps, data_5, 'red', 'BAO 5')
plot_bao_tps_data(fig_tps, data_10, 'green', 'BAO 10')
plot_bao_tps_data(fig_tps, data_15, 'blue', 'BAO 15')
plot_bao_tps_data(fig_tps, data_20, 'purple', 'BAO 20')

plot_ao_tps_data(fig_tps, data_2[:10], 'black', 'BAO 2')
plot_ao_tps_data(fig_tps, data_5, 'red', 'BAO 5')
plot_ao_tps_data(fig_tps, data_10, 'green', 'BAO 10')
plot_ao_tps_data(fig_tps, data_15, 'blue', 'BAO 15')
plot_ao_tps_data(fig_tps, data_20, 'purple', 'BAO 20')

# setup graph layout
fig_tps.update_xaxes(title_text="Concurrent Client Num", dtick=10)
fig_tps.update_yaxes(title_text="BatchAccountOperation TPS", row=1, col=1)
fig_tps.update_yaxes(title_text="AccountOperation TPS", row=1, col=2)

fig_tps.update_layout(
    title='TPS of BatchAccountOperation & AccountOperation V.S. Concurrent Client Num',
    hovermode="x unified",
    hoverlabel=dict(
        namelength=200
    )
)
fig_tps.show()


def plot_avg_latency_data(fig: go.Figure, data, color, tag):
    fig.add_trace(
        go.Scatter(
            name=f'{tag} Avg Latency',
            x=[row[0] for row in data],
            y=[row[2] for row in data],
            mode='markers+lines',
            line=dict(width=2),
            marker_size=8,
            marker_color=color,
        ),
    )


def plot_p99_latency_data(fig: go.Figure, data, color, tag):
    fig.add_trace(
        go.Scatter(
            name=f'{tag} P99 Latency',
            x=[row[0] for row in data],
            y=[row[3] for row in data],
            mode='markers+lines',
            line=dict(width=2, dash='dash'),
            marker_size=8,
            marker_color=color,
        ),
    )


# create graph for Latency
fig_latency = go.Figure()

plot_avg_latency_data(fig_latency, data_2[:10], 'black', 'BAO 2')
plot_avg_latency_data(fig_latency, data_5, 'red', 'BAO 5')
plot_avg_latency_data(fig_latency, data_10, 'green', 'BAO 10')
plot_avg_latency_data(fig_latency, data_15, 'blue', 'BAO 15')
plot_avg_latency_data(fig_latency, data_20, 'purple', 'BAO 20')

plot_p99_latency_data(fig_latency, data_2[:10], 'black', 'BAO 2')
plot_p99_latency_data(fig_latency, data_5, 'red', 'BAO 5')
plot_p99_latency_data(fig_latency, data_10, 'green', 'BAO 10')
plot_p99_latency_data(fig_latency, data_15, 'blue', 'BAO 15')
plot_p99_latency_data(fig_latency, data_20, 'purple', 'BAO 20')

# setup graph layout
fig_latency.update_xaxes(title_text="Concurrent Client Num", dtick=10)
fig_latency.update_yaxes(title_text="Latency in ms")

fig_latency.update_layout(
    title='BatchAccountOperation P99/Avg Latency V.S. Concurrent Client Num',
    hovermode="x unified",
    hoverlabel=dict(
        namelength=200
    )
)
fig_latency.show()


# create graph for Summary
fig_summary = make_subplots(specs=[[{"secondary_y": True}]])

fig_summary.add_trace(
    go.Scatter(
        name=f'handle_command Latency in US',
        x=[2, 5, 10, 15, 20],
        y=[100, 150, 250, 350, 450],
        mode='markers+lines',
        line=dict(width=2),
        marker_size=8,
        marker_color='red',
    ),
    secondary_y=False,
)

fig_summary.add_trace(
    go.Scatter(
        name=f'peak BAO TPS',
        x=[2, 5, 10, 15, 20],
        y=[7600, 4600, 3200, 2400, 1800],
        mode='markers+lines',
        line=dict(width=2),
        marker_size=8,
        marker_color='black',
    ),
    secondary_y=True,
)

# setup graph layout
fig_summary.update_xaxes(title_text="Account Operation Num in BatchAccountOperation")
fig_summary.update_yaxes(title_text="Avg Latency of handle_command in us", secondary_y=False)
fig_summary.update_yaxes(title_text="Peak BatchAccountOperation TPS", secondary_y=True)

fig_summary.update_layout(
    title='handle_command latency & Peak BAO TPS V.S. AO num in BAO',
    hovermode="x unified",
    hoverlabel=dict(
        namelength=200
    )
)

fig_summary.show()


def save_fig(fig, file_name):
    fig.write_html(f"/Users/glen.geng/Downloads/{file_name}.html")
    fig.write_image(f"/Users/glen.geng/Downloads/{file_name}.svg")


save_fig(fig_bao2, 'fig_bao2')
save_fig(fig_tps, 'fig_tps')
save_fig(fig_latency, 'fig_latency')
save_fig(fig_summary, 'fig_summary')
