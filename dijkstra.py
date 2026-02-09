class Solution:
    # Returns shortest distances from src to all other vertices
    def dijkstra(self, V, edges, src):
        # code here
        adj_list=[]
        for i in range(V):
            adj_list.append([])
            
        for u,v,d in edges:
            adj_list[u].append([v,d])
            
        print(adj_list)

solution=Solution()

solution.dijkstra(3,[[0, 1, 1], [1, 2, 3], [0, 2, 6]],2)