# Graph-Isomorphism

This project implements two basis algorithms for checking an isomorphism of two directed acyclic graphs.

# Naive approach
The naive approach is implemented in `naive.py` and it works by checking all possible bijection between two n-sized sets of nodes of two different graphs. Case with different number of nodes or edges is trivial. Since the time complexity of such an approach is O(n!) thus it is only practical for small-sized graphs.

# Tree isomorphism
The script in `trees.py` contains an implementation of an algorithm checking isomorphism of only specific class of graphs - trees. This solution has polynomial time complexity. 
## Isomorphism of rooted trees
For simplicity we can assume that the roots of both trees are known. The algorithm works by assigning a distance from root to any node, i.e. the depth. Next, we processes a set of nodes with the same depth, starting with leaves. Each node in the layer has all its children already processed, thus we encode a multiset of its children with a number unique for each different multiset(those are reused if a multiset has been seen already). With each node in a layer being encoded with a number we can compare the corresponding layers in the two trees. If the both of those layers have the same numbers with the same multiplicities we continue with another layer. Otherwise, the trees are not isomorphic. 
![Isomorhism](./images/figure.png)

## Finding roots
If roots of tree are not known they can be found in linear time complexity. In tree.py it is done by finding the longest path in both trees. The roots are the nodes in the middle. Since there can be two nodes in the middle, isomorphism should be checked for all root combinatoins.

# Drawing
Either `draw.py` or `drawApp.py` can be used for drawing the graphs. 
The latter method is recommended since it features simple GUI. Run it with `python3 drawApp.py` and then select a file from with to draw. It should be used with provided test cases, where each of then contains two graphs, whose isomorphism we want to check, so choose if it should be the first or the second graph from the file.
The former takes an input from stdin but only for a single graph, so using tests graph needs taking only a part of a file. Note both graph in those file may have different number of edges. Example use:
`head -n 8 tests/tests_tr0/dag_8_0_1.in | python3 draw.py`

| Image 1 | Image 2 |
|---------|---------|
| ![Image 1](./images/sample_drawing.png) | ![Image 2](./images/sample_drawing2.png) |

The edges do not show direction, however, in the test caes if an edges from `v` to `u` it present, this means there isno edge between `u` and `v`. For DAGs the drawing might seem to have cycles but it is only on the drawing.

# Tests
All tests in the tests directory have successfully passed.
To repliceate the tests first zip file in `./tests/` should be uncompresssed. Following tests were run:
`python3 test.py naive.py tests/tests_a`
`python3 test.py naive.py tests/tests_a_dense`
`python3 test.py trees.py tests/tests_tr0`
`python3 test.py trees.py tests/tests_t`. The script `test.py` takes two command line arguments the script for running the test and the data source.

