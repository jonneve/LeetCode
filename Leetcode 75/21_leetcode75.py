class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        # terminate recurssive fucntion when end of a branch of the tree has been reached (i.e root.left or root.right is not another nested TreeNode)
        if type(root) != TreeNode:
            return 0

        # recurssively call the maxdepth function for both sides of the binary tree
        # this which eventually finds the final root node (as 0 will be returned when root is not a TreeNode) down each path 
        # then count bottom-up to the source node to show the max depth, the greatest depth is kept after each recurssion 
        lh = self.maxDepth(root.left)
        rh = self.maxDepth(root.right)

        return max(lh, rh) + 1