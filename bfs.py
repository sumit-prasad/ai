class graph:
    adj=[]
    def __init__(self,v,e):
        self.v=v
        self.e=e
        graph.adj=[[0 for i in range(v)] for j in range (v) ]
    def addedge(self,start,e):
        graph.adj[start][e]=1
        graph.adj[e][start]=1
    def BFS(self,start):
        print('The path to goal is :')
        visited=[False]*self.v
        q=[start]
        visited[start]=True
        while q:
            vis=q[0]
            print(vis,end=' ')
            q.pop(0)
            for i in range(self.v):
                if (graph.adj[vis][i]==1 and (not visited[i])):
                    q.append(i)
                    visited[i]=True
                if i==goal:
                    break
v=int(input('Enter number of vertices:'))
e=int(input('Enter number of edges:'))
goal=int(input('Enter goal node:'))
g=graph(v,e)
for x in range(e):
    x=int(input('Enter graph edge source:'))
    y=int(input('Enter graph edge destination:'))
    g.addedge(x,y)
g.BFS(0)