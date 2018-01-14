#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 21:26:13 2018

@author: KACHING
"""

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root==None:
            return 0
       
        else:
            return max(self.maxDepth(root.left),self.maxDepth(root.right))+1
        