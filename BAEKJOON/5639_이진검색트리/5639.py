import sys

sys.stdin = open('input.txt', 'r')


def preorder(n, N):
    global tree
    global idx

    if n <= N:
        tree[n] = preorder_seq[idx]
        idx += 1
        preorder(2 * n, N)
        preorder(2 * n + 1, N)


def postorder(n, N):
    global post_order_tree

    if n <= N:
        postorder(2 * n, N)
        postorder(2 * n + 1, N)
        post_order_tree.append(tree[n])


preorder_seq = []

while True:

    number = sys.stdin.readline()
    if number == '':
        break
    number = int(number)

    preorder_seq.append(number)

idx = 0
tree = [0] * (len(preorder_seq) + 1)
preorder(1, len(preorder_seq))
post_order_tree = []

postorder(1, len(preorder_seq))

for num in post_order_tree:
    print(num)
