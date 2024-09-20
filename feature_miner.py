from glob import glob

import plotly.graph_objects as go
from plotly.subplots import make_subplots

from features import FEATURE_BUF


# one day per graph, one margin per subplot
def setup_graph(names: list[str]):
    rows = len(names)

    fig = make_subplots(rows=rows, cols=1,
                        row_heights=[0.1] * rows,
                        subplot_titles=names,
                        shared_xaxes=True,
                        vertical_spacing=0.05,
                        )

    fig.update_layout(
        hovermode="x unified",
    )

    for row in range(rows):
        fig.update_xaxes(
            tickmode = 'array',
            tickvals = [pos for (pos, _) in enumerate(FEATURE_BUF)],
            ticktext = [f'{pos} {f.KEY}' for (pos, f) in enumerate(FEATURE_BUF)],
            tickangle=-45,  # Set the angle of the tick labels
            row=row + 1, col=1,
        )

    return fig


# stats per day per margin
def calculate_feature_stats(name) -> dict:
    # position -> long/short -> hit_num
    feature_stats = {}

    for i in range(len(FEATURE_BUF)):
        feature_stats[i] = {'long': 0, 'short': 0}

    for filename in glob(f'./storage/predict/*{name}*.txt'):
        with open(filename) as fd:
            for line in fd:
                fields = line.strip().split('\t')
                direction = fields[0]
                features = fields[1].split(',')

                for feature in features:
                    feature_stats[int(feature)][direction] += 1

    return feature_stats


# plot per day per margin
def plot_feature_stats(feature_stats: dict, fig: go.Figure, row: int):
    feature_stats = list(feature_stats.items())
    feature_stats.sort(key=lambda x: x[0])

    fig.add_trace(
        go.Bar(
            x=[f[0] for f in feature_stats],
            y=[f[1]['long'] for f in feature_stats],
            name='long',
            marker_color='red'
        ),
        row=row, col=1
    )

    fig.add_trace(
        go.Bar(
            x=[f[0] for f in feature_stats],
            y=[f[1]['short'] for f in feature_stats],
            name='short',
            marker_color='green'
        ),
        row=row, col=1
    )


if __name__ == '__main__':
    all_names = [
        ['3d_0.05', '3d_0.10', '3d_0.20'],
        ['4d_0.05', '4d_0.10', '4d_0.20'],
        ['5d_0.05', '5d_0.10', '5d_0.20'],
    ]

    for names in all_names:
        fig = setup_graph(names)

        for row, name in enumerate(names):
            feature_stats = calculate_feature_stats(name)
            plot_feature_stats(feature_stats, fig, row + 1)

        fig.show()
