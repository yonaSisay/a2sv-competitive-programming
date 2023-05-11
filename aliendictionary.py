#User function Template for python3
from collections import *

class Solution:
    def findOrder(self,alien_dict, N, K):
    # code here
        graph = defaultdict(list)
        indeg = defaultdict(int)
        
        for i in range(N - 1):
            word1  = alien_dict[i]
            word2 = alien_dict[i + 1]
            
            for i in range(min(len(word1), len(word2))):
                if word1[i] != word2[i]:
                    graph[word1[i]].append(word2[i])
                    indeg[word2[i]] += 1
                    break
            
        stack = []
        res = []
            
        for i in range(k):
            if indeg[chr(i + 97)] == 0:
                stack.append(chr(i + 97))
        
        while stack:
            temp = stack.pop()
            res.append(temp)
            
            for elm in graph[temp]:
                indeg[elm] -= 1
                
                if indeg[elm] == 0:
                    stack.append(elm)
        
        return "".join(res)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

class sort_by_order:
    def __init__(self,s):
        self.priority = {}
        for i in range(len(s)):
            self.priority[s[i]] = i
    
    def transform(self,word):
        new_word = ''
        for c in word:
            new_word += chr( ord('a') + self.priority[c] )
        return new_word
    
    def sort_this_list(self,lst):
        lst.sort(key = self.transform)

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        line=input().strip().split()
        n=int(line[0])
        k=int(line[1])
        
        alien_dict = [x for x in input().strip().split()]
        duplicate_dict = alien_dict.copy()
        ob=Solution()
        order = ob.findOrder(alien_dict,n,k)
        s = ""
        for i in range(k):
            s += chr(97+i)
        l = list(order)
        l.sort()
        l = "".join(l)
        if s != l:
            print(0)
        else:
            x = sort_by_order(order)
            x.sort_this_list(duplicate_dict)
            
            if duplicate_dict == alien_dict:
                print(1)
            else:
                print(0)


# } Driver Code Ends