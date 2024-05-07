from typing import List
'''Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
https://leetcode.com/problems/group-anagrams/description/'''

class Anangrams:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        tmpList = []
        for l in strs:
            m = sorted(l)
            strr = ""
            tmpList.append(str(strr.join(m)))
        dic = {}
        print(tmpList)
        for i in strs:
            ind = strs.index(i)
            val = dic[tmpList[ind]] if dic.__contains__(tmpList[ind]) else []
            val.append(i)
            dic[tmpList[ind]] = val
        print(dic)
        res = []
        for v in dic.values():
            res.append(v)

        return res