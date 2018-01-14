#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 21:24:54 2018

@author: KACHING
"""

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ret=[]
        if root==None:
            return ret       
        Queue1=[]
    
        Queue1.insert(0,root)
        while Queue1:
            tmp=[]
            n=len(Queue1)
            i=0
            while i<n:
                r=Queue1.pop()
                tmp.append(r.val)
                if r.left!=None:
                    Queue1.insert(0,r.left)
                if r.right!=None:
                    Queue1.insert(0,r.right)
                i+=1
            ret.append(tmp)
        return ret
                    