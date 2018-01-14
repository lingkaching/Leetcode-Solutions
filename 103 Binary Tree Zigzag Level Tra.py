#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 21:25:39 2018

@author: KACHING
"""

class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        Queue=[]
        
        ret=[]
        if not root:
            return ret
        cnt=1
        Queue.insert(0,root)
        while Queue: 
            tmp=[]
            n=len(Queue)
            for i in range(0,n):
                r=Queue.pop()
                if cnt%2==0:
                    tmp.insert(0,r.val)
                else:
                    tmp.append(r.val)
                if r.left:
                    Queue.insert(0,r.left)
                if r.right:
                    Queue.insert(0,r.right)    
            ret.append(tmp)       
            cnt+=1
        return ret    