import unittest
from hypothesis import given
from hypothesis import strategies as st
from BinaryTree import BinaryTree


class TestBinaryTree(unittest.TestCase):
    # strategies.integers() generate an Integer list as input
    @given(st.lists(st.integers()))
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

    @given(st.lists(st.integers()))
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

    @given(st.lists(st.integers()), st.lists(st.integers()), st.lists(st.integers()))
    def test_concat_associativity(self, list_a, list_b, list_c):
        tree_a = BinaryTree()
        tree_a.from_list(list_a)
        tree_b = BinaryTree()
        tree_b.from_list(list_b)
        tree_c = BinaryTree()
        tree_c.from_list(list_c)
        tree_ab = BinaryTree()
        tree_ab.root = tree_ab.concat(tree_a.root, tree_b.root)
        tree_ab_c = BinaryTree()
        tree_ab_c.root = tree_ab_c.concat(tree_ab.root, tree_c.root)
        tree_bc = BinaryTree()
        tree_bc.root = tree_bc.concat(tree_b.root, tree_c.root)
        tree_a_bc = BinaryTree()
        tree_a_bc.root = tree_a_bc.concat(tree_a.root, tree_bc.root)
        listABC1 = tree_a_bc.to_list_level_order()
        listABC2 = tree_ab_c.to_list_level_order()
        self.assertEqual(listABC1, listABC2)

    @given(st.lists(st.integers()))
    def test_concat_identity(self, list_a):
        tree_a = BinaryTree()
        tree_a.from_list(list_a)
        tree_empty = BinaryTree()
        tree_ea = BinaryTree()
        tree_ea.root = tree_ea.concat(tree_empty.root, tree_a.root)
        tree_ae = BinaryTree()
        tree_ae.root = tree_ae.concat(tree_a.root, tree_empty.root)
        list_ae = tree_ae.to_list_level_order()
        list_ea = tree_ea.to_list_level_order()
        self.assertEqual(list_ae, list_ea)

    def test_iterator(self):
        tree = BinaryTree()
        tree.from_list([1, 2, 3, 4, 5])
        result = []
        for node_value in tree:
            result.append(node_value)
        self.assertEqual(result, [1, 2, 3, 4, 5])

    if __name__ == "__main__":
        unittest.main()
