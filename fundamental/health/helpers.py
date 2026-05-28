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


STATUS_SCORE = {'pass': 1.0, 'warn': 0.5, 'fail': 0.0}


def score_layers(layers, pts):
    active = [(w, s) for w, s in layers if s != 'skip']
    if not active:
        return 0, 'skip'
    total_w = sum(w for w, _ in active)
    score = sum(w * STATUS_SCORE[s] for w, s in active) / total_w
    if score >= 0.8:
        status = 'pass'
    elif score >= 0.4:
        status = 'warn'
    else:
        status = 'fail'
    return score * pts, status


def layer_symbols(layers):
    symbols = []
    for label, status in layers:
        if status == 'skip':
            continue
        if status == 'pass':
            icon = '✓'
        elif status == 'warn':
            icon = '⚠'
        else:
            icon = '✗'
        symbols.append('{}{}'.format(icon, label))
    return ' '.join(symbols)
