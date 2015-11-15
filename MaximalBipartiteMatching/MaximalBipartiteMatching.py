

def maxMatch(graph):
    result = 0
    numA = len(graph)
    numJ = len(graph[0])
    assignedJobs = [-1] * numJ
    for applicant in xrange(numA):
        visited = [False] * numJ
        isPossible = bfs(graph, applicant, visited, assignedJobs)
        if isPossible:
            result += 1
    return result
        
def bfs(graph,applicant,visited,assignedJobs):
    for job in xrange(len(graph[applicant])):
        interestedJobs = graph[applicant][job]
        if interestedJobs and not visited[job]:
            visited[job] = True
            # Checking if job was freely available
            if assignedJobs[job] < 0:
                assignedJobs[job] = applicant
                return True
            else:
                candidateOnThisJob = assignedJobs[job]
                isPossible = bfs(graph,candidateOnThisJob,visited,assignedJobs)
                if isPossible:
                    assignedJobs[job] = applicant
                    return True
            
    return False

                    
                
if __name__ == '__main__':
    graph = [[0, 1, 1, 0, 0, 0], [1, 0, 0, 1, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1]]
    print maxMatch(graph)
                   
        
        


