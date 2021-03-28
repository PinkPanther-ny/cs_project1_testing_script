#!/bin/bash
make clean
make -B
declare -i n_processors=$1
declare -i i=0
file="test_gen_result.txt"
if [ -f "$file" ] ; then
    rm "$file"
fi

for filename in testGenByNuoyan/*.txt; do
    i=$i+1
	echo "Testing $i - $filename"
    echo "Testing $i - $filename" >> test_gen_result.txt
    ./allocate -f $filename -p $1 >> test_gen_result.txt
done
echo "Testing finished. Compare result with your peers only, no code sharing."
make clean