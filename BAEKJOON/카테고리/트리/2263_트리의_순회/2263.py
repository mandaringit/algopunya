import sys

sys.stdin = open('input.txt', 'r')


def inorder(n, last):
    global tree
    global idx
    if n <= last:
        inorder(2 * n, last)
        tree[n] = inorder_seq[idx]
        idx += 1
        inorder(2 * n + 1, last)


def preorder(n, last):
    global tree
    global seq

    if n <= last:
        seq.append(tree[n])
        preorder(2 * n, last)
        preorder(2 * n + 1, last)


N = int(input())

tree = [0] * (N + 1)
idx = 0
inorder_seq = list(map(int, input().split()))
preorder_seq = list(map(int, input().split()))

inorder(1, N)

seq = []
preorder(1, N)
print(' '.join(map(str, seq)))
