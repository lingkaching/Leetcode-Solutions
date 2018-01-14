#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 21:24:16 2018

@author: KACHING
"""

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
    
#        if root==None:
#            return True
#        return self.isMirror(root.left,root.right)
        
    def isMirror(self,root1,root2):
        if root1==None and root2==None:
            return True
        if root1==None or root2==None:
            return False
        if root1.val!=root2.val:
            return False
        else:            
            return self.isMirror(root1.left,root2.right) and self.isMirror(root1.right,root2.left)