#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 21:28:30 2018

@author: KACHING
"""

class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root==None:
            return []
        Queue=[]
        ret=[]
        Queue.insert(0,root)
        while Queue:
            tmp=[]
            n=len(Queue)
            for i in range(0,n):
                r=Queue.pop()
                tmp.append(r.val)
                if r.left:
                    Queue.insert(0,r.left)
                if r.right:
                    Queue.insert(0,r.right)
            ret.insert(0,tmp)
        return ret