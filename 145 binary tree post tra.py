#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 21:33:57 2018

@author: KACHING
"""

class Solution:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        Stack=[]
        Ls=[]
        while Stack or root:
            while root:
                Ls.insert(0,root.val)
                Stack.append(root)
                root=root.right
            r=Stack.pop()
            root=r.left
        return Ls         
                