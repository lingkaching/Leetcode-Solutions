#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 21:27:00 2018

@author: KACHING
"""

class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(preorder)==0:
            return None
        return self.creat(preorder,inorder,0,len(preorder)-1,0,len(inorder)-1)
        
    def creat(self,preorder,inorder,pres,pree,ins,ine):
        if ine<ins:
            return None
        root=TreeNode(preorder[pres])
        for i in range(ins,ine+1):
            if inorder[i]==preorder[pres]:
                pos=i
                break
        root.left=self.creat(preorder,inorder,pres+1,pres+pos-ins,ins,pos-1)
        root.right=self.creat(preorder,inorder,pree-ine+pos+1,pree,pos+1,ine)
        return root
        