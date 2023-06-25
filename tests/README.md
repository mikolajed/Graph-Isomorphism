## Test Directories
The tests are located in directories with the following acronyms:
- `tests_a`: Contains small random graphs.
- `tests_a_dense`: Contains small dense graphs.
- `tests_t`: Contains trees.
- `tests_t_MORE`: Contains trees but more cases with bigger trees.
- `tests_tr0`: Contains tress rooted at 0.

## Test File Format
Each file contains one test case and describes two graphs, one after another. The format of the test file is as follows:
1. Number of nodes and edges for the first graph.
2. List of the edges, with one edge per line. (parent, node)
3. Number of nodes and edges for the second graph.
4. List of the edges, with one edge per line. (parent, node)
5. Nodes are numbered starting from 0.

## Test File Decompression
Please note that the test files need to be manually decompressed before use.

## Naming Scheme
Input files have names `*.in` and contain information about two graphs. The output files named `*.out` contain an answer `YES` or `NO`. Name of each test case contains number of nodes, type of a graph, number of the case having with its number of nodes and the last digit indicates if it is a positive of negative case. 
