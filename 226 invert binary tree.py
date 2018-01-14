#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 21:34:42 2018

@author: KACHING
"""

class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root:   
            root.left,root.right=root.right,root.left
            root.left=self.invertTree(root.left)
            root.right=self.invertTree(root.right)
        return root
            