cd tests; 
unzip tests_a.zip ; 
unzip tests_a_dense.zip ; 
unzip tests_tr0.zip ; 
unzip tests_t.zip ;
unzip tests_t_MORE.zip ;
cd ..; 
echo "RUN naive.py for tests_a"; python3 test.py naive.py tests/tests_a;
echo "RUN naive.py for tests_a_dense"; python3 test.py naive.py tests/tests_a_dense;
echo "RUN trees.py for tests_tr0"; python3 test.py trees.py tests/tests_tr0;
echo "RUN trees.py for tests_t"; python3 test.py trees.py tests/tests_t;
echo "RUN trees.py for tests_t_MORE"; python3 test.py trees.py tests/tests_t_MORE
