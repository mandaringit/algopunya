import sys

sys.stdin = open('input.txt', 'r')


def preorder(N):
    global graph

    if N in graph:
        print(N, end="")
        preorder(graph[N][0])
        preorder(graph[N][1])


def inorder(N):
    global graph

    if N in graph:
        inorder(graph[N][0])
        print(N, end="")
        inorder(graph[N][1])


def postorder(N):
    global graph

    if N in graph:
        postorder(graph[N][0])
        postorder(graph[N][1])
        print(N, end="")


N = int(input())

graph = {}

for _ in range(N):
    p, c1, c2 = input().split()

    graph[p] = [c1, c2]

preorder('A')
print()
inorder('A')
print()
postorder('A')
