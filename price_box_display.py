import plotly.graph_objects as go
from price_box_analysis import PriceBoxAnalysis


class PriceBoxDisplay:
    def __init__(self, fig: go.Figure, analysis: PriceBoxAnalysis):
        self.fig = fig
        self.enable_box_label = analysis.stock_df.shape[0] < 500

        # [(from_idx, from_date, from_low, to_idx, to_date, to_high, length, delta, pst, mid), ...]
        self.up_box = analysis.up_box
        # [(from_idx, from_date, from_high, to_idx, to_date, to_low, length, delta, pst, mid), ...]
        self.down_box = analysis.down_box

    def add_up_box(self, _from_idx, from_date, from_low, _to_idx, to_date, to_high, length, delta, pst, mid,
                   *, forcast=False):
        text = f'{length}D <br> {delta:.2f}$ <br> +{pst:.2f}%' if self.enable_box_label else None

        self.fig.add_shape(
            type="rect",
            x0=from_date, y0=from_low, x1=to_date, y1=to_high,
            line=dict(
                color="Red" if not forcast else "Blue",
                width=1,
                dash="dot"
            ),
            label=dict(
                text=text,
                textposition="bottom center"
            ),
        )

        self.fig.add_shape(
            type="line",
            x0=from_date, y0=mid, x1=to_date, y1=mid,
            line=dict(
                color="Red",
                width=0.5,
                dash="dot"
            )
        )

        self.fig.add_shape(
            type="line",
            x0=from_date, y0=from_low, x1=to_date, y1=to_high,
            line=dict(
                color="Red",
                width=1,
                # dash="dot"
            )
        )

    def add_down_box(self, _from_idx, from_date, from_high, _to_idx, to_date, to_low, length, delta, pst, mid,
                     *, forcast=False):
        text = f'-{pst:.2f}% <br> {delta:.2f}$ <br> {length}D' if self.enable_box_label else None

        self.fig.add_shape(
            type="rect",
            x0=from_date, y0=from_high, x1=to_date, y1=to_low,
            line=dict(
                color="Green" if not forcast else "Blue",
                width=1,
                dash="dot",
            ),
            label=dict(
                text=text,
                textposition="top center"
            ),
        )

        self.fig.add_shape(
            type="line",
            x0=from_date, y0=mid, x1=to_date, y1=mid,
            line=dict(
                color="Green",
                width=0.5,
                dash="dot",
            )
        )

        self.fig.add_shape(
            type="line",
            x0=from_date, y0=from_high, x1=to_date, y1=to_low,
            line=dict(
                color="Green",
                width=1,
                # dash="dot",
            )
        )

    def build_graph(self):
        for item in self.up_box:
            self.add_up_box(*item)

        for item in self.down_box:
            self.add_down_box(*item)
