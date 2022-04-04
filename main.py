# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import numpy.matlib

# 有向图节点
edges = [(1, 2), (1, 3), (1, 4), (1, 5), (1, 8), (1, 6), (2, 1), (2, 3), (3, 1), (3, 2), (4, 1), (4, 2), (4, 3), (4, 6),
         (4, 7), (4, 8), (5, 1), (5, 2), (5, 3), (5, 9), (5, 10), (5, 8), (6, 1), (6, 2), (6, 3), (7, 1), (7, 2),
         (7, 3), (8, 1), (8, 2), (8, 3), (9, 1), (9, 2), (9, 3), (10, 1), (10, 2), (10, 3)]

# edges = [(1, 2), (1, 3), (1, 4), (1, 5)]

# 矩阵文件 csv格式，无向图
mat_file_name = "./graph_adjacency_matrix.csv"


# 画有向图
def cal_dg():
    DG = nx.DiGraph()
    DG.add_edges_from(edges)

    # g = nx.petersen_graph()
    # plt.subplots(121)
    nx.draw(DG, with_labels=True)
    # plt.subplots(122)

    plt.show()


# 问题1 解决方案
def question_1():
    # matrix
    # 0 1 1 1 1 1 1 1 1 1
    # 1 0 1 1 1 1 1 1 1 1
    # 1 1 0 1 1 1 1 1 1 1
    # 1 1 1 0 0 1 1 1 0 0
    # 1 1 1 0 0 0 0 1 1 1
    # 1 1 1 1 0 0 0 0 0 0
    # 1 1 1 1 0 0 0 0 0 0
    # 1 1 1 1 1 0 0 0 0 0
    # 1 1 1 0 1 0 0 0 0 0
    # 1 1 1 0 1 0 0 0 0 0
    m = np.matrix('0,1,1,1,1,1,1,1,1,1;1,0,1,1,1,1,1,1,1,1;1,1,0,1,1,1,1,1,1,1;1,1,1,0,0,1,1,1,0,0;1,1,1,0,0,0,0,1,1,'
                  '1;1,1,1,1,0,0,0,0,0,0;1,1,1,1,0,0,0,0,0,0;1,1,1,1,1,0,0,0,0,0;1,1,1,0,1,0,0,0,0,0;1,1,1,0,1,0,0,0,'
                  '0,0')
    print(m)

    # 计算矩阵m特征值和特征向量
    b = np.linalg.eig(m)
    print("特征值：")
    for i in b[0]:
        print(i)


# question 2解决方案
def question_2():
    # 使用numpy打开文件，默认只有矩阵
    csv_mat = numpy.loadtxt(open(mat_file_name),delimiter=",",skiprows=0)
    print(csv_mat)
    [rows, cols] = csv_mat.shape
    G = nx.Graph() #无向图

    # 添加节点
    for i in range(rows):
        for j in range(cols):
            if csv_mat[i,j] == 1:
                G.add_edge(i, j)
    # G.add_edges_from(csv_mat)
    # 计算特征向量中心度
    eigenvector = nx.eigenvector_centrality(G, max_iter=100)

    # 输出
    for item in eigenvector:
        print(item, eigenvector[item])
    # 中间中心度
    # dc = nx.degree_centrality(G)
    # print(dc)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # cal_dg()
    # question_1()
    question_2()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
