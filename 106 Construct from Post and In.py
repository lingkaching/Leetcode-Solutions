#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 21:27:35 2018

@author: KACHING
"""class Solution:
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if len(inorder)==0:
            return None
        return self.creat(inorder,postorder,0,len(inorder)-1,0,len(postorder)-1)
        
    def creat(self,inorder,postorder,ins,ine,posts,poste):
        if ine<ins:
            return None
        root=TreeNode(postorder[poste])
        for i in range(ins,ine+1):
            if inorder[i]==postorder[poste]:
                pos=i
                break
        root.left=self.creat(inorder,postorder,ins,pos-1,posts,posts+pos-1-ins)
        root.right=self.creat(inorder,postorder,pos+1,ine,pos+1-ine+poste-1,poste-1)
        return root

