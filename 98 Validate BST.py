#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 21:22:09 2018

@author: KACHING
"""

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        import numpy as np
        return self.ValidBST(root,-np.inf,np.inf)
        
    def ValidBST(self,root,minVal,maxVal):
        if root==None:
            return True
        if root.val<=minVal or root.val>=maxVal:
            return False
        return  self.ValidBST(root.left,minVal,root.val) and self.ValidBST(root.right,root.val,maxVal)