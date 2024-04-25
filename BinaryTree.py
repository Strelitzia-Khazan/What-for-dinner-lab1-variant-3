class BinaryTreeNode:
    # Initialize a binary tree node
    def __init__(self, value=-1, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def get_value(self):
        return self.value


class BinaryTree:
    # Initialize a binary tree
    def __init__(self, root=None):
        # root node of binary tree
        self.root = root
        # Store the hierarchical traversal order of tree nodes
        self.level_queue = []
        # Store current location
        self.current = 0
    
    def add_node(self, value):
        if value is None:
            return  # No node is generated when value is none

        new_node = BinaryTreeNode(value)
        # Checks whether the root node is empty
        if self.root is None:
            self.root = new_node
        else:
            node_queue = [self.root]
            while node_queue:
                current = node_queue.pop(0)
                # Checks whether the left child node of
                # the current node is empty
                if current.left is None:
                    current.left = new_node
                    break
                # Checks whether the right child node of
                # the current node is empty
                elif current.right is None:
                    current.right = new_node
                    break
                else:
                    node_queue.append(current.left)
                    node_queue.append(current.right)

    def get_parent(self, value):
        if self.root is None or self.root.value == value:
            return None

        node_queue = [self.root]
        # Use breadth-first search to traverse the tree
        while node_queue:
            current = node_queue.pop(0)
            if current.left:
                if current.left.value == value:
                    return current
                node_queue.append(current.left)
                
            if current.right:
                if current.right.value == value:
                    return current
                node_queue.append(current.right)               
        return None
    
    def remove(self, value):
        if self.root is None:
            return False
        
        if self.root.value == value:
            self.root = None
            return True

        # Find the parent node of the node to be deleted
        parent = self.get_parent(value)
        if parent:
            if parent.left.value == value:
                delete_node = parent.left
            else:
                delete_node = parent.right

            if delete_node.left is None:
                if parent.left.value == value:
                    parent.left = delete_node.right
                else:
                    parent.right = delete_node.right
            elif delete_node.right is None:
                if parent.left.value == value:
                    parent.left = delete_node.left
                else:
                    parent.right = delete_node.left
            else:
                # Find the successor node of the node to be deleted
                tmp_pre = delete_node
                tmp_next = delete_node.right
                if tmp_next.left is None:
                    tmp_pre.right = tmp_next.right
                    tmp_next.left = delete_node.left
                    tmp_next.right = delete_node.right
                else:
                    # Find the leftmost child node of the successor node
                    while tmp_next.left:
                        tmp_pre = tmp_next
                        tmp_next = tmp_next.left
                    tmp_pre.left = tmp_next.right
                    tmp_next.left = delete_node.left
                    tmp_next.right = delete_node.right

                # Link the successor node to the corresponding child node of the parent node
                if parent.left.value == value:
                    parent.left = tmp_next
                else:
                    parent.right = tmp_next
            return True
        else:
            return False

    def to_list_pre_order(self):
        if self.root is None:
            return []
        else:
            # Recursively obtain the pre-order traversal list of the left and right subtrees
            left_list = BinaryTree(self.root.left).to_list_pre_order()
            right_list = BinaryTree(self.root.right).to_list_pre_order()
            if left_list is None and right_list is None:
                return [self.root.value]
            elif left_list is None:
                return [self.root.value] + right_list
            elif right_list is None:
                return [self.root.value] + left_list
            else:
                return [self.root.value] + left_list + right_list

    def to_list_level_order(self):
        if self.root is None:
            return []
        list = []
        node_queue = [self.root]
        while len(node_queue):
            current = node_queue.pop(0)
            list.append(current.value)
            if current.left:
                node_queue.append(current.left)
            if current.right:
                node_queue.append(current.right)
        return list

    def get_depth(self):
        if self.root is None:
            return 0
        depth = 1
        # Recursively obtain the depth of the left and right subtrees
        left_depth = BinaryTree(self.root.left).get_depth()
        right_depth = BinaryTree(self.root.right).get_depth()
        return depth + max(left_depth, right_depth)

    def get_size(self):
        if self.root is None:
            return 0
        size = 1
        # Recursively calculate the number of nodes in the left and right subtrees
        left_size = BinaryTree(self.root.left).get_size()
        right_size = BinaryTree(self.root.right).get_size()
        return size + left_size + right_size
    
    def from_list(self, list):
        for value in list:
            self.add_node(value)
        return self

    def filter(self):
        list = self.to_list_pre_order()
        result = []
        for value in list:
            if isinstance(value, int):
                result.append(value)
        return result

    def map(self, function):
        if self.root is None:
            return self

        def apply_map(node):
            if node is not None:
                node.value = function(node.value)
                apply_map(node.left)
                apply_map(node.right)

        apply_map(self.root)
        return self

    def reduce(self, function, initial_state=0):
        state = initial_state
        list = self.to_list_pre_order()
        for value in list:
            state = function(state, value)
        return state

    def __iter__(self):
        self.level_queue = []
        if self.root is not None:
            self.level_queue.append(self.root)
        return self

    def __next__(self):
        if not self.level_queue:
            raise StopIteration
        node = self.level_queue.pop(0)
        if node.left is not None:
            self.level_queue.append(node.left)
        if node.right is not None:
            self.level_queue.append(node.right)
        return node.value

    def empty(self):
        return None

    def concat(self, tree_A, tree_B):
        if not tree_A:
            return tree_B
        if not tree_B:
            return tree_A
        root = BinaryTreeNode(tree_A.value + tree_B.value)
        root.left = self.concat(tree_A.left, tree_B.left)
        root.right = self.concat(tree_A.right, tree_B.right)
        return root
