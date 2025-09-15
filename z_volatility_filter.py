import os
import re

# 36m_h6_r85_no_vol
# 42m_h5_r8_no_vol

# Directory path
input_dir = '/Users/glen.geng/workspace/QuantPy/_train_36m_h5_r8_has_vol'
output_dir = '/Users/glen.geng/workspace/QuantPy/_train_36m_h7_r85_no_vol'

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

            if not ((up + down) >= 7 and (up + down) / total >= 0.85):
                continue

            if 'vol box 30d' in line or 'vol box 25d' in line or 'vol box 20d' in line or 'vol box 15d' in line:
                continue

            writer.write(line)
