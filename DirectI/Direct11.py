from collections import defaultdict
s = "aaa_b"
d = "baa_a"

index = s.index("_")



visited = defaultdict(lambda : False)
calculated = defaultdict(lambda : float("inf"))


def checkEqual(s, d):
    for i in xrange(len(s)):
        if s[i] != d[i]:
            return False
    return True

def dfs(source, visited, index, s, d):
    visited[source] = True
    if checkEqual(s, d):
        return 0
    else:
        minimum = float("inf")
        if index + 1 < len(s):
            s[index], s[index + 1] = s[index + 1], s[index]
            news = "".join(s)
            if not visited[news]:
                calculated[news] = dfs(news, visited, index + 1, s, d)
            minimum = min(minimum, calculated[news])
            s[index], s[index + 1] = s[index + 1], s[index]
            
        
        if index + 2 < len(s) and s[index + 1] != s[index + 2]:
            s[index], s[index + 2] = s[index + 2], s[index]
            news = "".join(s)
            if not visited[news]:
                calculated[news] = dfs(news, visited, index + 2, s, d)
            minimum = min(minimum, calculated[news])
            s[index], s[index + 2] = s[index + 2], s[index]
            
        if index - 1 >= 0:
            s[index], s[index - 1] = s[index - 1], s[index]
            news = "".join(s)
            if not visited[news]:
                calculated[news] = dfs(news, visited, index - 1, s, d)
            minimum = min(minimum, calculated[news])
            s[index], s[index - 1] = s[index - 1], s[index]
            
        if index - 2 >= 0 and s[index - 1] != s[index - 2]:
            s[index], s[index - 2] = s[index - 2], s[index]
            news = "".join(s)
            if not visited[news]:
                calculated[news] = dfs(news, visited, index - 2, s, d)
            minimum = min(minimum, calculated[news])
            s[index], s[index - 2] = s[index - 2], s[index]
            
        calculated[source] = 1 + minimum
        return calculated[source]
        
            
        
            
            
        
                
        

s = list(s)
d = list(d)
print dfs("".join(s), visited, index, s, d)
        
    
    
