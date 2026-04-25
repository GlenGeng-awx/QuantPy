import pandas as pd


def pick_top_percentile(stock_df: pd.DataFrame, candidates: list,
                        ratio: float = 0.1, rolling_size: int = 200) -> list:
    """Pick dates where value is in the top `ratio` of the rolling window."""
    hits = []
    for i in range(rolling_size, len(candidates)):
        value, idx = candidates[i]
        if value is None:
            continue

        window_values = sorted(
            [v for v, _ in candidates[i - rolling_size:i] if v is not None],
            reverse=True,
        )
        if window_values and value >= window_values[int(len(window_values) * ratio) - 1]:
            hits.append(stock_df['Date'][idx])

    return hits
