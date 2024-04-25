import unittest
from hypothesis import given,  strategies
from BinaryTree import BinaryTree


class TestBinaryTree(unittest.TestCase):
    # strategies.integers() generate an Integer list as input
    @given(strategies.lists(strategies.integers()))
    def test_add_node(self, values):
        tree = BinaryTree()
        for value in values:
            tree.add_node(value)
        # Check if the tree contains all the added values
        for value in values:
            self.assertIn(value, tree.to_list_pre_order())

    def test_remove(self):
        tree = BinaryTree()
        tree.add_node(1)
        tree.add_node(2)
        tree.add_node(3)
        tree.add_node(4)
        tree.add_node(5)
        # test for attempting to remove a non-root & non-leaf node
        self.assertTrue(tree.remove(2))
        # test whether the removed node is still in the preorder traversal list
        self.assertNotIn(2, tree.to_list_pre_order())
        # test for attempting to remove a leaf node
        self.assertTrue(tree.remove(4))
        # test whether the removed node is still in the preorder traversal list
        self.assertNotIn(4, tree.to_list_pre_order())
        # test for attempting to remove a root node
        self.assertTrue(tree.remove(1))
        # test whether the removed node is still in the preorder traversal list
        self.assertNotIn(1, tree.to_list_pre_order())
        # test for attempting to remove a Non-existent node
        self.assertFalse(tree.remove(6))

    def test_to_list_pre_order(self):
        tree = BinaryTree()
        tree.add_node(1)
        tree.add_node(2)
        tree.add_node(3)
        tree.add_node(4)
        tree.add_node(5)
        self.assertEqual(tree.to_list_pre_order(), [1, 2, 4, 5, 3])

    def test_to_list_level_order(self):
        tree = BinaryTree()
        tree.add_node(1)
        tree.add_node(2)
        tree.add_node(3)
        tree.add_node(4)
        tree.add_node(5)
        self.assertEqual(tree.to_list_level_order(), [1, 2, 3, 4, 5])

    def test_get_depth(self):
        tree = BinaryTree()
        tree.add_node(1)
        tree.add_node(2)
        tree.add_node(3)
        tree.add_node(4)
        tree.add_node(5)
        self.assertEqual(tree.get_depth(), 3)

    def test_get_size(self):
        tree = BinaryTree()
        tree.add_node(1)
        tree.add_node(2)
        tree.add_node(3)
        self.assertEqual(tree.get_size(), 3)

    @given(strategies.lists(strategies.integers()))
    def test_from_list(self, values):
        tree = BinaryTree()
        tree.from_list(values)
        self.assertEqual(tree.to_list_level_order(), values)

    def test_filter(self):
        tree = BinaryTree()
        tree.from_list([1, "a", 2, "b", 3])
        self.assertEqual(tree.filter(), [1, 3, 2])

    def test_map(self):
        tree = BinaryTree()
        tree.from_list([1, 2, 3, 4, 5])
        tree.map(lambda x: x * 2)
        self.assertEqual(tree.to_list_level_order(), [2, 4, 6, 8, 10])

    def test_reduce(self):
        # test for empty list
        tree = BinaryTree()
        result = tree.reduce(lambda acc, x: acc + x, 0)
        self.assertEqual(result, 0)
        tree.from_list([1, 2, 3, 4, 5])
        result = tree.reduce(lambda acc, x: acc + x, 0)
        self.assertEqual(result, 15)

    def test_concat(self):
        tree_A = BinaryTree()
        tree_A.from_list([1, 2, 3])
        tree_B = BinaryTree()
        tree_B.from_list([1, 2, 3, 4])
        tree_AB = BinaryTree()
        tree_AB.root = tree_AB.concat(tree_A.root, tree_B.root)
        self.assertEqual(tree_AB.to_list_level_order(), [2, 4, 6, 4])
        # test for Identity element
        tree_C = BinaryTree()
        tree_AC = BinaryTree()
        tree_AC.root = tree_AC.concat(tree_A.root, tree_C.root)
        self.assertEqual(tree_AC.to_list_level_order(), [1, 2, 3])
        # test for associativity
        tree_D = BinaryTree()
        tree_D.from_list([1, 2, 3, 4, 5])
        tree_ABD1 = BinaryTree()
        tree_ABD1.root = tree_ABD1.concat(tree_AB.root, tree_D.root)
        tree_BD = BinaryTree()
        tree_BD.root = tree_BD.concat(tree_B.root, tree_D.root)
        tree_ABD2 = BinaryTree()
        tree_ABD2.root = tree_ABD2.concat(tree_A.root, tree_BD.root)
        listABD1 =  tree_ABD1.to_list_level_order()
        listABD2 =  tree_ABD2.to_list_level_order()
        self.assertEqual(listABD1, listABD2)

    def test_iterator(self):
        tree = BinaryTree()
        tree.from_list([1, 2, 3, 4, 5])
        result = []
        for node_value in tree:
            result.append(node_value)
        self.assertEqual(result, [1, 2, 3, 4, 5])

    if __name__ == "__main__":
        unittest.main()
