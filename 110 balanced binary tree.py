#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 21:29:58 2018

@author: KACHING
"""
class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.Depth(root)!=-1
        
    def Depth(self,root):
        if root==None:
            return 0
        left=self.Depth(root.left)
        if left==-1:
            return -1
        right=self.Depth(root.right)
        if right==-1:
            return -1 
        if (abs(left-right)>1):
            return -1
        else:
            return max(left,right)+1
        
