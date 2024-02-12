from typing import Optional, TypeVar
from packages.dsa.Tree import TreeNode


class Solution:

    # 94. Binary Tree Inorder Traversal
    def inorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        visited = []

        def dfs(root):
            if root:
                dfs(root.left)
                visited.append(root.val)
                dfs(root.right)

        dfs(root)
        return visited

    def iterInorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        if not root:
            return []

        visited = []
        stack = []

        while root or stack:
            # Traverse as left as possible
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            if root:
                visited.append(root.val)
                root = root.right

        return visited

    # 98. Validate Binary Search Tree
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False

        stack = []
        previous = None

        while root or stack:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            if root:
                if previous and previous.val >= root.val:
                    return False
                previous = root
                root = root.right

        return True

    # 100. Same Tree
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(left, right):
            if not left or not right:
                return not left and not right

            return left.val == right.val and dfs(left.left, right.left) and dfs(left.right, right.right)

        return dfs(p, q)

    # 101. Symmetric Tree
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def dfs(left, right):
            if not left or not right:
                return not left and not right

            return left.val == right.val and dfs(left.left, right.right) and dfs(left.right, right.left)

        return dfs(root.left, root.right)

    # 104. Maximum Depth of Binary Tree
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        l = self.maxDepth(root.left)
        r = self.maxDepth(root.right)
        return max(l, r) + 1

    # 108. Convert Sorted Array to Binary Search Tree
    def sortedArrayToBST(self, nums: list[int]) -> Optional[TreeNode]:
        def makeBST(nums, lo, hi):
            if lo >= hi:
                return None

            return TreeNode(
                val=nums[(lo + hi) // 2],
                left=makeBST(nums, lo, (lo + hi) // 2),
                right=makeBST(nums, ((lo + hi) // 2) + 1, hi)
            )

        return makeBST(nums, 0, len(nums))
