import os
import re

# Directory path
input_dir = '/Users/glen.geng/workspace/QuantPy/_train.v1'
output_dir = '/Users/glen.geng/workspace/QuantPy/_train.v9'

for file_name in os.listdir(input_dir):
    input_path = f'{input_dir}/{file_name}'
    output_path = f'{output_dir}/{file_name}'

    with open(input_path, 'r') as fd, open(output_path, 'w') as writer:
        for line in fd:
            match = re.search(r'total (\d+), up (\d+), down (\d+)', line)
            if not match:
                print(f"No match found: {line}")
                continue

            total, up, down = map(int, match.groups())
            print(f"Total: {total}, Up: {up}, Down: {down}")

            # v1: 6, 0.8    --- Bronze
            # v2: 6, 0.85   --- Silver
            # v3: 6, 0.9
            # v4: 7, 0.8    --- Gold
            # v5: 7, 0.85g
            # v6: 7, 0.9
            # v7: 8, 0.8
            # v8: 8, 0.85
            # v9: 8, 0.9

            # v1：最大覆盖+稳定中高准确率=最高（或并列最高）平均命中；主力生产位。
            # v2：准确率略优、覆盖略小；与v1互为首选，偏好精度时优先。
            # v4：准确率持续高、覆盖中等、稳定性好；综合性价比极佳。
            # v4：日常准确率长期在0.5上下且波动小，信号量中等，最符合“稳准少”的日选需求。
            # v1/v2已达到行业较好水平；v4为高性价比与稳定性代表

            if (up + down) >= 8 and (up + down) / total >= 0.9:
                writer.write(line)
