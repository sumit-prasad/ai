import math

if __name__ == "__main__":
    n = int(input('Enter the number of nodes: '))
    scores = list(map(int, input('Enter the value of nodes in bfs manner: ').split()))
    tree = []
    tree.append(scores)
    treedepth = math.log(len(scores), 2)
    mx = treedepth % 2
    while treedepth > 0:
        lis = []
        i = 0
        while i < len(scores):
            if mx:
                lis.append(max(scores[i], scores[i+1]))
            else:
                lis.append(min(scores[i], scores[i+1]))
            i += 2
        tree.append(lis)
        scores = lis.copy()
        treedepth -= 1
        mx = treedepth % 2

    print(tree[::-1])