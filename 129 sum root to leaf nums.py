#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 21:32:12 2018

@author: KACHING
"""

class Solution:
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        val=0
        return self.sumNum(root,val)
        
        
    def sumNum(self,root,val):
        if root==None:
            return 0
        val=val*10+root.val
        if root.left==None and root.right==None:
            return val
        return self.sumNum(root.left,val)+self.sumNum(root.right,val)
    