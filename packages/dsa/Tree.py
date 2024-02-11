from typing import Optional, TypeVar, Generic
T = TypeVar("T")


# Definition for a binary tree node.
class TreeNode(Generic[T]):
    def __init__(self, val: T = 0, left: Optional["TreeNode[T]"] = None, right: Optional["TreeNode[T]"] = None):
        self.val = val
        self.left = left
        self.right = right


# TODO: BST + traversals/insert/find/delete
class Tree(Generic[T]):
    def __init__(self, root: TreeNode[T]):
        self.root = root
