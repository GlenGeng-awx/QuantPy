import json
import os
from conf import *


def build_cross_vix(date: str) -> dict:
    cross_vix = {}

    for stock_name in ALL:
        file_name = f'tmp/{stock_name}.{date}.res'
        print(f'build cross_vix for {date}, Processing {file_name}')

        if not os.path.exists(file_name):
            print(f'{file_name} not exists')
            continue

        with open(file_name, 'r') as fd:
            for line in fd:
                record = json.loads(line)
                op_names = tuple(record['op_names'])

                result = record['result']
                total_num, long_num, short_num = result['total_num'], result['long_num'], result['short_num']

                if op_names not in cross_vix:
                    cross_vix[op_names] = {
                        'total_num': 0,
                        'long_num': 0,
                        'short_num': 0,
                        'hits': [],
                        'op_names': op_names,
                    }

                cross_vix[op_names]['total_num'] += total_num
                cross_vix[op_names]['long_num'] += long_num
                cross_vix[op_names]['short_num'] += short_num
                cross_vix[op_names]['hits'].append(stock_name)

    return cross_vix


def train_cross(date: str):
    cross_vix = build_cross_vix(date)

    with open(f'tmp/cross_vix.{date}.res', 'w') as fd:
        for op_names, data in cross_vix.items():
            total_num, long_num, short_num = data['total_num'], data['long_num'], data['short_num']

            if total_num >= 10 and (long_num + short_num) / total_num >= 0.8:
                fd.write(json.dumps(data) + '\n')
