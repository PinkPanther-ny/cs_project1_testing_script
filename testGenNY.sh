file="test_gen_result.txt"
test_dir="testGenByNuoyan"
if [ -d "$test_dir" ]; then rm -Rf $test_dir;
fi
if [ -f "$file" ] ; then
    rm "$file"
fi

python3 testGenByNuoyan.py