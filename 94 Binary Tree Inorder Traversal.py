#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 21:20:46 2018

@author: KACHING
"""

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack=[]
        Ls=[]
        while root or stack:
            while root:
                stack.append(root)
                root=root.left
            r=stack.pop()
            Ls.append(r.val)
            root=r.right
        return Ls