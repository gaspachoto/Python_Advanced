from collections import deque

jobs = deque([int(x) for x in input().split(", ")])
index = int(input())
our_job = jobs[index]
clock_cycles = 0
counter = -1

while jobs:
    current_job = jobs.popleft()
    counter += 1
    if current_job < our_job:
        clock_cycles += current_job
    elif current_job == our_job:
        if counter <= index:
            clock_cycles += current_job
        else:
            continue
    elif current_job > our_job:
        continue
print(clock_cycles)