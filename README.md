# What of dinner - lab 1 - variant 3 - Set based on binary-tree

This is an example project which demonstrates project structure and necessary
CI checks. It is not the best structure for real-world projects, but good
enough for educational purposes.

## Project structure

- `BinaryTree.py` -- implementation of `BinaryTree` class and `BinaryTreeNode` class.

- `BinaryTree_test.py` -- unit and PBT tests for `BinaryTree`.

## Features

- PBT: `test_add_commutative`

## Contribution

- Lu Bin (1476683166@qq.com) -- BinaryTree.py.
- Wang Yining (351432511@qq.com) -- BinaryTree_test.py.

## Changelog

- 17.04.2024 - 0
   - Change the README.md title and enter the development stage
- 19.04.2024 - 1
   - Added BinaryTreeNode class and BinaryTree class.
     Added some custom functions.
     At the same time, the file name was changed to BinaryTree.py.
- 19.04.2024 - 2
   - Changed the names of some functions.
   - Deleted some unnecessary functions.
   - Added new functions.
- 19.04.2024 - 3
   - All required functions have been added, and BinaryTree.py has been completed.
   - Implemented unit tests for BinaryTree and updated the README.
- 20.04.2024 - 4
   - Implemented property-based tests for BinaryTree.
- 25.04.2024 - 5
   - fixed mistyping problem in BinaryTree.py.
   - improved code style.  

## Design notes

- Implementation restrictions:
   - For mutable, we define a node structure and a tree structure, and the functions
     are all in the tree class. In the custom function stage, recursion is used to
     handle various operations on the binary tree, which simplifies the code
     implementation. At the same time, iterators are implemented through breadth-first
     search to facilitate iterative traversal of binary trees.
- Advantages of unit test and PBT test
   - Unit tests focus on testing individual units of the code in isolation.
     This allows for pinpointing bugs or issues within specific functions.
   - When a unit test fails, it's usually easy to pinpoint the cause of the failure
     since the scope is limited to a specific unit of code.
   - PBT generates test cases automatically based on properties or specifications
     of the system, allowing for more thorough and exploratory testing.
   - PBT can uncover edge cases and corner scenarios that may not be covered by
     traditional unit tests, leading to the discovery of bugs or unexpected behavior.
- Disadvantages of unit test and PBT test
   - Unit tests only verify the behavior of individual units in isolation,
     which may not capture integration issues or interactions between components.
   - When a property-based test fails, it may be challenging to pinpoint the exact
     cause of the failure since the test cases are generated automatically.
