#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 21:29:22 2018

@author: KACHING
"""

class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        n=len(nums)
        if n==0:
            return None
        elif n==1:
            root=TreeNode(nums[0])
        elif n==2:
            root=TreeNode(nums[1])
            root.left=TreeNode(nums[0])            
        elif n==3:
            root=TreeNode(nums[1])
            root.left=TreeNode(nums[0])
            root.right=TreeNode(nums[2])
        else:
            i=(n-1)//2
            root=TreeNode(nums[i])
            root.left=self.sortedArrayToBST(nums[:i])
            root.right=self.sortedArrayToBST(nums[i+1:])
        return root