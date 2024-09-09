from datetime import datetime
from time import sleep

# Record the start time
start_time = datetime.now()

# Perform the task
sleep(5)

# Record the end time
end_time = datetime.now()

# Calculate the time cost
time_cost = (end_time - start_time).total_seconds()

# Print the time cost
print(f'Task finished, cost: {time_cost}s')
