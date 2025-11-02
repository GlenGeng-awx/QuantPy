# mode
TRAIN = 'train'
RECALL = 'recall'


def get_key(target: str, mode: str) -> str:
    return f'{target} - {mode}'


# 15d
def get_size() -> int:
    return 15


# 10% for train, 20% for recall
def get_ratio(mode: str) -> float:
    if mode == TRAIN:
        return 0.1
    elif mode == RECALL:
        return 0.2
    else:
        raise ValueError(f'Unknown mode: {mode}')
