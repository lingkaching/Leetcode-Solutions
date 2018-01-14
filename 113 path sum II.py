#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 21:31:51 2018

@author: KACHING
"""

class Solution:
    
    Ls=[]
    i=0
    def pathSum(self, root, s):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        res=[]
        ls=[]
        
        self.dfs(root,s,ls,res)
        return res
        
    def dfs(self,root,s,ls,res):
        if root==None:
            return
        if root.left:
            self.dfs(root.left,s-root.val,ls+[root.val],res)
        if root.right:
            self.dfs(root.right,s-root.val,ls+[root.val],res)    
        if root.left==None and root.right==None and s==root.val:
            ls.append(root.val)
            res.append(ls)
        