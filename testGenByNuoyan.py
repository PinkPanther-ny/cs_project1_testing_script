import os
import random
from numpy.random import exponential

n_test = 50
n_process_per_test = random.randint(20, 40)
parallel_spawn_rate = random.randint(0, 2)

# Exponential distribution for task arrival time and execution time
task_arrive_scale = 30
task_total_execution_time_scale = 15

path = os.getcwd()
path += "/testGenByNuoyan"

try:
    os.mkdir(path)
except OSError:
    pass
cur_path = os.path.dirname(__file__)
os.path.join(cur_path, 'testGenByNuoyan')

new_path = os.path.relpath('..\\testGenByNuoyan', cur_path)

print(f"Generating task.....")
for i in range(n_test):
    f_name = "test_" + str(i+1) + ".txt"
    f = open(os.path.join(cur_path, "testGenByNuoyan", f_name), "w")

    task_arrive_time = exponential(scale=task_arrive_scale, size=n_process_per_test - 1)
    task_arrive_time = [int(i) for i in task_arrive_time]
    task_arrive_time.append(0)
    task_arrive_time.sort()

    task_execution_time = exponential(scale=task_total_execution_time_scale, size=n_process_per_test)
    task_execution_time = [int(i) + 1 for i in task_execution_time]

    task_id = random.sample(range(n_process_per_test * n_process_per_test), n_process_per_test)

    for j in range(n_process_per_test):
        x = "n" if bool(random.randint(0, 2)) else "p"
        f.write(f"{task_arrive_time[j]} {task_id[j]} {task_execution_time[j]} {x}\n")

    f.close()
print(f'All done({n_test} tasks generated)! Run "./runTests.sh n" to test(n is number of cpu).')