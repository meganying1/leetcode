# https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/
# difficulty: medium
# topics: tree, depth-first search, binary search tree, binary tree

# problem:
# Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        ans = None
        def traverse(node):
            nonlocal ans
            nonlocal count
            if not node: return
            traverse(node.left)
            count += 1
            if count == k:
                ans = node.val
                return
            traverse(node.right)
        traverse(root)
        return ans

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def getInorder(node):
            if not node: return []
            return getInorder(node.left) + [node.val] + getInorder(node.right)
        return getInorder(root)[k-1]
