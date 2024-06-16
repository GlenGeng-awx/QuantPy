import plotly.graph_objects as go
from price_box_analysis import PriceBoxAnalysis


class PriceBoxDisplay:
    def __init__(self, fig: go.Figure, analysis: PriceBoxAnalysis):
        self.fig = fig
        self.stock_df = analysis.stock_df

        # [(from_idx, from_date, from_low, to_idx, to_date, to_high, length, delta, pst, mid), ...]
        self.up_box = analysis.up_box
        # [(from_idx, from_date, from_high, to_idx, to_date, to_low, length, delta, pst, mid), ...]
        self.down_box = analysis.down_box

        self.x_of_up_box = []
        self.y_of_up_box = []

        self.x_of_up_text = []
        self.y_of_up_text = []
        self.up_text = []

        self.x_of_down_box = []
        self.y_of_down_box = []

        self.x_of_down_text = []
        self.y_of_down_text = []
        self.down_text = []

    def add_up_box(self, from_idx, from_date, from_low, to_idx, to_date, to_high, length, delta, pst, mid):
        # box
        self.x_of_up_box.extend([from_date, from_date, to_date, to_date, from_date, None])
        self.y_of_up_box.extend([from_low, to_high, to_high, from_low, from_low, None])

        # middle line
        self.x_of_up_box.extend([from_date, to_date, None])
        self.y_of_up_box.extend([mid, mid, None])

        # trend line
        self.x_of_up_box.extend([from_date, to_date, None])
        self.y_of_up_box.extend([from_low, to_high, None])

        # label
        x = self.stock_df.loc[(from_idx + to_idx) // 2]['Date']
        y = from_low
        text = f'{length}D <br> {delta:.2f}$ <br> +{pst:.2f}%'

        self.x_of_up_text.append(x)
        self.y_of_up_text.append(y)
        self.up_text.append(text)

    def add_down_box(self, from_idx, from_date, from_high, to_idx, to_date, to_low, length, delta, pst, mid):
        # box
        self.x_of_down_box.extend([from_date, to_date, to_date, from_date, from_date, None])
        self.y_of_down_box.extend([from_high, from_high, to_low, to_low, from_high, None])

        # middle line
        self.x_of_down_box.extend([from_date, to_date, None])
        self.y_of_down_box.extend([mid, mid, None])

        # trend line
        self.x_of_down_box.extend([from_date, to_date, None])
        self.y_of_down_box.extend([from_high, to_low, None])

        # label
        x = self.stock_df.loc[(from_idx + to_idx) // 2]['Date']
        y = from_high
        text = f'-{pst:.2f}% <br> {delta:.2f}$ <br> {length}D'

        self.x_of_down_text.append(x)
        self.y_of_down_text.append(y)
        self.down_text.append(text)

    def build_graph(self):
        for item in self.up_box:
            self.add_up_box(*item)

        for item in self.down_box:
            self.add_down_box(*item)

        self.fig.add_trace(
            go.Scatter(
                name='up box',
                x=self.x_of_up_box,
                y=self.y_of_up_box,
                mode='lines',
                line=dict(width=1, color='red', dash="dot",),
                visible='legendonly',
            )
        )

        self.fig.add_trace(
            go.Scatter(
                name='up text',
                x=self.x_of_up_text,
                y=self.y_of_up_text,
                text=self.up_text,
                mode="text",
                textfont=dict(
                    color="red",
                ),
                visible='legendonly',
            )
        )

        self.fig.add_trace(
            go.Scatter(
                name='down box',
                x=self.x_of_down_box,
                y=self.y_of_down_box,
                mode='lines',
                line=dict(width=1, color='green', dash="dot",),
                visible='legendonly',
            )
        )

        self.fig.add_trace(
            go.Scatter(
                name='down text',
                x=self.x_of_down_text,
                y=self.y_of_down_text,
                text=self.down_text,
                mode="text",
                textfont=dict(
                    color="green",
                ),
                visible='legendonly',
            )
        )
