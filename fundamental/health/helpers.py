def ttm_compare_col(ttm_df, annual_df):
    """TTM 和 annual 同期时，返回 annual 第二列的 index，否则返回 0"""
    if ttm_df.empty or annual_df.empty:
        return 0
    if ttm_df.columns[0] == annual_df.columns[0]:
        return 1 if len(annual_df.columns) > 1 else 0
    return 0


def growth_rate(new, old):
    if new is None or old is None or old == 0:
        return None
    return (new - old) / abs(old)


def make_result(name, status, value, detail, weight):
    return {'name': name, 'status': status, 'value': value, 'detail': detail, 'weight': weight}


def score_dimension(metrics):
    total = sum(m['weight'] for m in metrics if m['status'] != 'skip')
    if total == 0:
        return None
    earned = 0
    for m in metrics:
        if m['status'] == 'pass':
            earned += m['weight']
        elif m['status'] == 'warn':
            earned += m['weight'] * 0.5
    return earned / total * 100
