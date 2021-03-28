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