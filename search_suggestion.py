'''You are given an array of strings products and a string searchWord.

Design a system that suggests at most three product names from products after each character of searchWord is typed. Suggested products should have common prefix with searchWord. If there are more than three products with a common prefix return the three lexicographically minimums products.

Return a list of lists of the suggested products after each character of searchWord is typed.



Example 1:

Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
Output: [["mobile","moneypot","monitor"],["mobile","moneypot","monitor"],["mouse","mousepad"],["mouse","mousepad"],["mouse","mousepad"]]
Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"].
After typing m and mo all products match and we show user ["mobile","moneypot","monitor"].
After typing mou, mous and mouse the system suggests ["mouse","mousepad"].

'''
from typing import List


class SearchSuggestion:
    def binarySearch(self, words, substring):
        left, right = 0, len(words) - 1
        index = -1
        while left <= right:
            mid = (left + right) // 2
            if words[mid].startswith(substring):
                index = mid
                right = mid - 1  # Move left to find the first occurrence
            elif words[mid] < substring:
                left = mid + 1
            else:
                right = mid - 1
        return index

    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        res = []

        sortedProducts = products.sort()
        i=1

        while i <= len(searchWord) :
            c = searchWord[0:i]
            temp = []
            counter = 0
            l = self.binarySearch(products, c)
            if l == -1:
                res.append(temp)
                i = i+1
                continue
            temp.append(products[l])
            l = l + 1
            while l < len(products) and counter < 2:
                if(products[l].startswith(c)):
                    temp.append(products[l])
                    l=l+1
                    counter = counter+1
                else:
                    break

            res.append(temp)

            i = i+1


        return res

