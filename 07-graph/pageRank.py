__author__ = 'yangbin1729'

import pandas as pd
import numpy as np
import networkx as nx
import jieba

"""一、PageRank 算法"""


def pagerank_v1(graph, damping=0.85, epsilon=1.0e-8):
    """从图中获取相关信息"""
    inlink_map = {}  # 从值中的所有节点可以到键节点
    outlink_counts = {}  # 从键节点可以到多少个节点

    def new_node(node):
        if node not in inlink_map:
            inlink_map[node] = set()
        if node not in outlink_counts:
            outlink_counts[node] = 0

    for tail_node, head_node in graph:
        new_node(tail_node)
        new_node(head_node)

        if tail_node == head_node:
            continue
        if tail_node not in inlink_map[head_node]:
            inlink_map[head_node].add(tail_node)
            outlink_counts[tail_node] += 1

    all_nodes = set(inlink_map.keys())
    N = len(all_nodes)
    for node, outlink_count in outlink_counts.items():
        if outlink_count == 0:  # 处理孤立的节点
            outlink_counts[node] = len(all_nodes)
            for l_node in all_nodes:
                inlink_map[l_node].add(node)

    """计算PageRank值"""
    initial_value = 1 / N
    ranks = {}
    for node in inlink_map.keys():
        ranks[node] = initial_value

    new_ranks = {}
    delta = 1.0
    n_iterations = 0
    while delta > epsilon:
        new_ranks = {}
        for node, inlinks in inlink_map.items():
            new_ranks[node] = ((1 - damping) / N) + (damping * sum(
                ranks[inlink] / outlink_counts[inlink] for inlink in inlinks))
            # 每个节点的 rank 值 = sum(其它节点o 到本节点的概率 * o 的 rank 值)

        delta = sum(
            abs(new_ranks[node] - ranks[node]) for node in new_ranks.keys())
        ranks, new_ranks = new_ranks, ranks
        n_iterations += 1
    return ranks, n_iterations


class NetworkXError(ValueError):
    pass


"""networkx模块内实现的PageRank算法"""


def pagerank_v2(G, alpha=0.85, personalization=None,
                max_iter=100, tol=1.0e-6, nstart=None, weight='weight',
                dangling=None):
    """
    :param G: NetworkX 图对象
    :param alpha: Damping parameter(??)
    :param personalization: 自定义的 节点-值 词典
    :param max_iter:
    :param tol:
    :param nstart: 所有节点 PageRank 初始值
    :param weight:
    :param dangling: 处理孤立节点，键为指向该孤立节点的节点，值为权重(??)
    :return: 节点-PageRank值 词典
    """
    if len(G) == 0:
        return {}

    if not G.is_directed():
        D = G.to_directed()
    else:
        D = G

    W = nx.stochastic_graph(D, weight=weight)  # 使得从 每个节点 出发的所有边权重和为 1
    N = W.number_of_nodes()

    if nstart is None:
        x = dict.fromkeys(W, 1.0 / N)
    else:
        s = float(sum(nstart.values()))
        x = {(k, v / s) for k, v in nstart.items()}

    if personalization is None:
        p = dict.fromkeys(W, 1 / N)
    else:
        missing = set(G) - set(personalization)
        if missing:
            raise NetworkXError('Personalization dictionary '
                                'must have a value for every node. '
                                'Missing nodes %s' % missing)
        s = float(sum(personalization.values()))
        p = {(k, v / s) for k, v in personalization.items()}

    if dangling is None:
        dangling_weights = p
    else:
        missing = set(G) - set(dangling)
        if missing:
            raise NetworkXError('Dangling node dictionary '
                                'must have a value for every node. '
                                'Missing nodes %s' % missing)
        s = float(sum(dangling.values()))
        dangling_weights = dict((k, v / s) for k, v in dangling.items())

    dangling_nodes = [n for n in W if W.out_degree(n, weight=weight) == 0]

    for _ in range(max_iter):
        xlast = x
        x = dict.fromkeys(xlast.keys(), 0)
        danglesum = alpha * sum(xlast[n] for n in dangling_nodes)

        for n in x:
            for nbr in W[n]:
                x[nbr] += alpha * xlast[n] * W[n][nbr][weight]
            x[n] += danglesum * dangling_weights[n] + (1.0 - alpha) * p[n]
            # todo: 具体怎么计算的？？？

        err = sum([abs(x[n] - xlast[n]) for n in x])
        if err < N * tol:
            return x
    raise NetworkXError('pagerank: power iteration failed to converge '
                        'in %d iterations.' % max_iter)


"""二、PageRank 算法用于单词"""

from gensim.summarization.keywords import get_graph
from gensim.summarization.pagerank_weighted import pagerank_weighted

graph = get_graph("The road to hell is paved with good intentions.")
result = pagerank_weighted(graph)
# todo : 如何用于中文？？

from jieba.analyse import textrank

textrank('下面附上本次的源代码和结果示意，有兴趣的朋友可以自己实验', withWeight=True)

"""三、TextRank 计算句子重要性"""


def calculate_rank(M, ranks, i, d=0.85):
    """
    :param M: 句子间的相似性矩阵
    :param ranks: 当前的 PageRank 向量
    :param i: 第 i 个句子
    :param d: 阻尼系数
    :return: 第 i 个句子的 PageRank 值
    """
    n = len(M)
    added_score = 0.0

    for j in range(n):
        denominator = 0.0
        fraction = M[j][i] * ranks[j]
        for k in range(n):
            denominator += M[j][k]
        # if denominator == 0:
        #     denominator = 1
        added_score += fraction / denominator

    rank = (1 - d) + d * added_score
    return rank


def sentence_ranks(M):
    ranks = [0.5 for _ in range(len(M))]
    old_ranks = [0.0 for _ in range(len(M))]

    n_iters = 0
    diff = float('inf')
    while diff > 1e-6:
        for i in range(len(M)):
            old_ranks[i] = ranks[i]
        for i in range(len(M)):
            ranks[i] = calculate_rank(M, old_ranks, i)
            # ranks[i] = calculate_rank(M, ranks, i)
            # ranks[i]的值 基于第 1~i-1 元素本次迭代的值和 第 i+1~n 个元素的上一次迭代的值
        n_iters += 1
        diff = sum([(i - j) ** 2 for i, j in zip(ranks, old_ranks)])
    return ranks, n_iters


def sentence_ranks_v2(M, d=0.85):
    n = len(M)
    ranks = np.full(n, 1 / n)
    old_ranks = np.zeros(n)

    n_iters = 0
    while np.sum((ranks - old_ranks) ** 2) > 1e-6:
        old_ranks = ranks[:]
        ranks = (1 - d) + d * np.matmul(M.T / np.sum(M, axis=1), ranks)
        #     ranks 的每一个值都是基于 上一迭代的所有值
        n_iters += 1
    return ranks, n_iters


"""四、基于 TextRank 进行文本摘要"""


def sent_tokenize(text):
    """将原始文本拆分为句子"""
    pass

def sent_vectorize(sent, model):
    """词向量相加，生成句子向量"""
    wordlist = jieba.cut(sent)
    word_vectors = [model.vector(w) for w in wordlist]
    return np.sum(word_vectors, axis=0)


def similarity(v1, v2):
    """向量余弦相似度"""
    a = np.dot(v1, v2)
    b = np.sqrt(np.power(v1, 2))
    c = np.sqrt(np.power(v2, 2))
    return a / (b * c)


from sklearn.metrics.pairwise import cosine_similarity


def similarity_matrix(sents):
    """生成相似度矩阵"""

    sent_vectors = [sent_vectorize(sent) for sent in sents]
    # n = len(sents)
    # M = np.ones((n, n))
    # for i in range(0, n - 1):
    #     for j in range(i + 1, n):
    #         M[i][j] = similarity(sent_vectors[i], sent_vectors[j])
    #         M[j][i] = M[i][j]
    M = cosine_similarity(sent_vectors)
    return M


def summarize(text, n=3):
    """获得 TextRank 值最大的 n 句话"""
    sents = sent_tokenize(text)
    M = similarity_matrix(sents)
    # ranks, _ = sentence_ranks_v2(M, d=0.85)
    # mask = np.argsort(ranks)[-n:]
    # return [sents[i] for i in mask]

    graph = nx.from_numpy_array(M)
    ranks = nx.pagerank(graph)
    ranked_sentences = sorted([(ranks[i], s) for i, s in enumerate(sents)],
                              reverse=True)
    return ranked_sentences[:n]


"""五、文本摘要 Todo

1、应用RNN和LSTM的文本摘要
2、应用加强学习的文本摘要
3、应用生成对抗神经网络（GAN）的文本摘要

"""

if __name__ == '__main__':
    # nodes = 'ABCD'
    # edges = [('A', 'B'), ('A', 'C'), ('A', 'D'),
    #          ('B', 'A'), ('B', 'D'),
    #          ('C', 'A'), ('D', 'B'), ('D', 'C')]
    #
    # G = nx.DiGraph()
    # G.add_nodes_from(nodes)
    # G.add_edges_from(edges)
    #
    # node2rank = pagerank_v2(G)
    # print(node2rank)
    #
    # ranks, n_iterations = pagerank_v1(G.edges())
    # print(ranks, n_iterations)
    #
    # pr = nx.pagerank(G, alpha=0.85)
    # print(pr)
    M = np.array([[1.0, 0.2, 0.6, 0.3],
                  [0.2, 1.0, 0.4, 0.1],
                  [0.6, 0.4, 1.0, 0.5],
                  [0.3, 0.1, 0.5, 1.0]])
