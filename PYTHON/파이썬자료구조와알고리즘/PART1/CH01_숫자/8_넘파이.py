import numpy as np

a = np.array(((11, 12, 13), (21, 22, 23), (31, 32, 33)))
print(a)

x = np.array(((11, 12, 13), (21, 22, 23)))
print(x.ndim)  # 차원수

print("-" * 50)


def testing_numpy():
    '''tests many feature of numpy'''
    ax = np.array([1, 2, 3])
    ay = np.array([3, 4, 5])
    print(ax)
    print(ax * 2)
    print(ax + 10)
    print(np.sqrt(ax))
    print(np.cos(ax))
    print(ax - ay)
    print(np.where(ax < 2, ax, "2보다 크지롱"))

    m = np.matrix([ax, ay, ax])
    print(m)
    print(m.T)

    grid1 = np.zeros(shape=(10, 10), dtype=float)
    grid2 = np.ones(shape=(10, 10), dtype=float)
    print(grid1)
    print(grid2)
    print(grid1[1])
    print(grid2[:, 2] * 2)


if __name__ == '__main__':
    testing_numpy()
