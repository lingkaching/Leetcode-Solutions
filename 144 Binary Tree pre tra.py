#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 21:33:23 2018

@author: KACHING
"""

class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        Stack=[]
        Ls=[]
        while Stack or root:
            while root:
                Ls.append(root.val)
                Stack.append(root)
                root=root.left
            r=Stack.pop()
            root=r.right
        return Ls   