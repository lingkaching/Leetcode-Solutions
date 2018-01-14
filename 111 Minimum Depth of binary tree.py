#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 21:30:35 2018

@author: KACHING
"""

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root==None:
            return 0
        if root.left==None and root.right==None:
            return 1
        elif root.left==None and root.right!=None:            
            return self.minDepth(root.right)+1
        elif root.right==None and root.left!=None:            
            return self.minDepth(root.left)+1
        else:
            return min(self.minDepth(root.left),self.minDepth(root.right))+1
