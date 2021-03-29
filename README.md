https://github.com/PinkPanther-ny/cs_project1_testing_script
testGenNY.sh
testGenByNuoyan.py
runTests.sh

testGenNY.sh calls the python script to randomly generate input files.

runTests.sh
n is the number of processors for running current set of tasks in testGenByNuoyan folder

Tasks configuration can be modified from testGenByNuoyan.py, very simple logic.

Usage: 
1: put these 3 file at same directory to your make file
2: run "./testGenNY.sh"
3: run "./runTests.sh n"
4: send testGenByNuoyan folder to your peer, let him/her run "./runTests.sh n", 
compare your test_gen_result.txt(better not with your eyes) to see if any of you have bugs.


Written by NuoyanChen(nuoyanc@student.unimelb.edu.au) for testing purposes for comp30023-2021-project-1.

I did found 2 edge case bugs using this after pass the CI test, lol, good luck.

example output in wsl shell

alvin@Alvin:/mnt/d/CLionProjects/comp30023-2021-project-1$ ./testGenNY.sh
Generating task.....
All done(50 tasks generated)! Run "./runTests.sh n" to test(n is number of cpu).

alvin@Alvin:/mnt/d/CLionProjects/comp30023-2021-project-1$ ./runTests.sh 3
gcc -Wall -g -std=c11 -c allocate allocate.c
Testing 1 - testGenByNuoyan/test_1.txt
...
Testing 50 - testGenByNuoyan/test_50.txt
Testing finished. Compare result with your peers only, no code sharing.

example test_gen_result.txt
Testing 1 - testGenByNuoyan/test_1.txt
0,RUNNING,pid=544,remaining_time=26,cpu=0
210,FINISHED,pid=1121,proc_remaining=0
Turnaround time xxx
Time overhead xxx xxx
Makespan xxx
Testing 2 - testGenByNuoyan/test_10.txt
0,RUNNING,pid=237.0,remaining_time=3,cpu=0
0,RUNNING,pid=237.1,remaining_time=3,cpu=1
189,FINISHED,pid=54,proc_remaining=0
Turnaround time xx
Time overhead xxx xxx
Makespan xxx
