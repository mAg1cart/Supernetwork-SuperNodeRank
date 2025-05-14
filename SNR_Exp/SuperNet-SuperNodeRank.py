import random
import json
import jieba
import jieba.analyse
import pandas as pd
import openpyxl
import networkx as nx
import math
import numpy as np
from openpyxl.workbook import Workbook
from scipy.spatial.distance import cosine
from snownlp import SnowNLP


class SuperNode:

    def __init__(self, user_name, info, keywords, sentiment):
        self.user_name = user_name  # 用户子节点
        self.info = info  # 信息子节点
        self.keywords = keywords  # 关键词集子节点
        self.sentiment = sentiment  # 情感子节点
        self.user_feature = 0  # 用户特征值
        self.SNR_value = 1.0  # SNR值
        self.info_feature = 0  # 信息特征值
        self.comNum = 0  # 用户评论数

    # 用户名
    def set_user_name(self, user_name):
        self.user_name = user_name

    # 获取用户名
    def get_user_name(self):
        return self.user_name

    # 用户发布的信息
    def set_info(self, info):
        self.info = info

    # 获取用户发布的信息
    def get_info(self):
        return self.info

    # 用户的关键词集
    def set_keywords(self, keywords):
        self.keywords = keywords

    # 获取用户的关键词集
    def get_keywords(self):
        return self.keywords

    # 用户的情感值
    def set_sentiment(self, sentiment):
        self.sentiment = sentiment

    def get_sentiment(self):
        return self.sentiment

    # SNR值
    def set_SNR_value(self, SNR_value):
        self.SNR_value = SNR_value

    def get_SNR_value(self):
        return self.SNR_value

    # 信息特征值
    def set_info_feature(self, info_feature):
        self.info_feature = info_feature

    def get_info_feature(self):
        return self.info_feature

    # 评论数
    def set_com(self, comNum):
        self.comNum = comNum

    def get_com(self):
        return self.comNum


# 定义用户
class User:
    def __init__(self, user_name):
        self.user_name = user_name

        self.user_in = 0  # 入度中心度
        self.user_cc = 0  # 接近中心度
        self.user_btw = 0  # 中介中心度
        self.user_score = 0  # 用户得分
        self.like = 0  # 点赞数
        self.com = 0  # 评论数
        self.inf = 0  # 影响人数
        self.comNum = 0  # 评论数
        self.id = 0  # 用户ID

    # 重写函数利用用户名去重
    def __hash__(self):
        # 返回username的哈希值，用于集合中的元素唯一性判断
        return hash(self.get_user_name())

    def __eq__(self, other):
        # 比较 user_name，这里假设 other.user_name 也是 numpy 数组
        if isinstance(other, User):
            return self.get_user_name() == other.get_user_name()
        return False

    def set_user_name(self, user_name):
        self.user_name = user_name

    def get_user_name(self):
        return self.user_name

    # 用户的入度中心度
    def get_user_in(self):
        return self.user_in

    def set_user_in(self, user_in):
        self.user_in = user_in

    # 用户的接近中心度
    def get_user_cc(self):
        return self.user_cc

    def set_user_cc(self, user_cc):
        self.user_cc = user_cc

    # 用户的中介中心度
    def get_user_btw(self):
        return self.user_btw

    def set_user_btw(self, user_btw):
        self.user_btw = user_btw

    # 用户得分
    def get_user_score(self):
        return self.user_score

    def set_user_score(self, user_score):
        self.user_score = user_score

    # 获取点赞数
    def get_like(self):
        return self.like

    def set_like(self, like):
        self.like = like

    # 获取评论数
    def get_com(self):
        return self.com

    def set_com(self, com):
        self.com = com

    # id
    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

        # 得到用户特征值

    def set_user_feature(self, user_feature):
        self.user_feature = user_feature

        # 得到用户特征值

    def get_user_feature(self):
        return self.user_feature


# 存储所有的超级节点值
super_nodes = []
# 存储所有的用户节点
users = []


# 得到关键词集
def find_kws(info):
    seg_list = jieba.cut(info, cut_all=True)  # 分词处理
    # print(" ".join(seg_list))
    # n是普通名词,a是形容词,v是动词
    keywords = jieba.analyse.extract_tags(info, topK=20, withWeight=False, allowPOS=('v', 'a'), withFlag=False)  # 寻找关键词
    return keywords


# 处理数据
# 构建超级网络
# 获取评论数

def create_super_net():
    # 明星 记录数：55654 用户数：36615 发文用户数：121.xlsx
    data = pd.read_excel(r'明星 记录数：55654 用户数：36615 发文用户数：121.xlsx')
    print("构建超级网络")

    # 行数和列数
    row_num = len(data.index.values)
    col_num = len(data.columns.values)
    # 定义两个超级节点分别用于发文的用户,和对该用户进行评论的用户
    org_node = SuperNode(' ', ' ', ' ', 0)
    com_node = SuperNode(' ', ' ', ' ', 0)

    org_user = User(' ')
    com_user = User(' ')

    i = 0
    while i < 55653:
        # org_是原本发这篇微博的用户,com_是评论这条微博的用户
        # 每20行的发文用户是同一个
        org_node = SuperNode(' ', ' ', ' ', 0)
        org_user = User(' ')

        # print(data.values[[i], [2]])
        # 获取发文用户id

        id = data.values[[i], [2]]
        # print("发文用户id:" + str(id))
        org_user.set_id(id)
        # 获取发文用户名
        org_user_name = data.values[[i], [3]]
        # 获取发文信息
        org_info = data.values[[i], [5]]
        org_kws = find_kws(str(org_info))
        org_node.set_user_name(str(org_user_name))
        org_user.set_user_name(str(org_user_name))
        org_node.set_info(org_info)
        org_node.set_keywords(org_kws)

        org_user.set_like(data.values[[i], [15]])
        # org_user.set_com(data.values[[i], [14]])
        org_node.set_keywords(org_kws)
        comNum = 0

        # 判断下一行是否为该用户的评论用户
        j = i + 1
        super_nodes.append(org_node)
        # users.append(org_user)
        com_node = SuperNode(' ', ' ', ' ', 0)
        com_user = User(' ')
        com_id = data.values[[j], [2]]
        com_user_name = str(data.values[[i], [10]])
        com_info = data.values[[i], [12]]
        com_kws = find_kws(str(com_info))
        com_user.set_user_name(com_user_name)
        com_node.set_user_name(com_user_name)
        super_nodes.append(com_node)
        users.append(com_user)

        # print("第一个while里的下标i:" + str(i))
        j = i
        while com_id == id:
            if j > 55653:
                comNum += 1
                break

            com_id = data.values[[j], [2]]

            com_node = SuperNode(' ', ' ', ' ', 0)
            com_user = User(' ')
            com_user_name = str(data.values[[j], [10]])
            com_info = data.values[[j], [12]]
            com_kws = find_kws(str(com_info))
            com_user.set_user_name(com_user_name)
            com_node.set_user_name(com_user_name)
            com_node.set_info(com_info)
            com_node.set_keywords(com_kws)
            super_nodes.append(com_node)
            users.append(com_user)

            j = j + 1
            comNum += 1
            # print("com_id:" + str(com_id))

        comNum -= 1
        j = 0
        if comNum == 0:
            comNum += 1
        if i > 500:
            print(str(id) + "对应的评论数:" + str(int(comNum)))
        # print("没加评论数i:" + str(i))
        org_user.set_com(comNum)
        users.append(org_user)

        i = i + int(comNum)
        # print("i:" + str(i))


create_super_net()
print("超级网络构建完成")


# super_net = nx.DiGraph()

def create_user_net(all_user):
    count = 0
    i = 0
    length = len(all_user)
    G = set()
    while i < length:
        count = 0
        while count <= all_user[i].get_com():
            if all_user[i].get_com() == 0:
                break
            G.add((all_user[i], all_user[count]))
            count = count + 1
        i = i + count
    return G


create_user_net(users)
print("构建用户网络完成")
# 构建用户图
# user_graph = nx.DiGraph()
# interaction = create_user_net(users)
# user_graph.add_edges_from(interaction)

print("用户数:" + str(len(users)))
in_list = []
bwt_list = []
cc_list = []


# 入度中心度
def cal_in(V):
    # cal_in_list = []
    nxG = nx.DiGraph()
    nxG.add_nodes_from(V)
    i = 0
    while i < len(users):
        #
        j = 1
        while j <= users[i].get_com():
            nxG.add_edge(users[i + j], users[i])
            j = j + 1

        i += j
    in_net = nx.centrality.in_degree_centrality(nxG)
    in_list.append(in_net)
    print("计算中心度完成")
    # print(in_list)


# 计算接近中心度和中介中心度
def cal_cc(V):
    nxG = nx.Graph()
    nxG.add_nodes_from(V)  # 添加节点
    i = 0
    while i < len(users):
        #
        j = 1
        while j <= users[i].get_com():
            nxG.add_edge(users[i + j], users[i])
            j = j + 1

        i += j
    cc_net = nx.centrality.closeness_centrality(nxG)
    cc_list.append(cc_net)
    bwt_net = nx.centrality.betweenness_centrality(nxG, normalized=False, weight=None)
    bwt_list.append(bwt_net)


# 中介中心度
def cal_btw(V):
    cal_btw_list = []
    nxG = nx.Graph()
    nxG.add_nodes_from(V)
    i = 0
    while i < len(users):
        #
        j = 1
        while j <= 20:
            nxG.add_edge(users[i + j], users[i])
            j = j + 1

        i += j
    b = nx.centrality.betweenness_centrality(nxG, normalized=False, weight=None)
    cal_btw_list.append(b)
    return cal_btw_list


def cal_info_feature():
    for node in super_nodes:
        # 信息所在的超级节点的数量
        C_i = sum(1
                  for n in super_nodes
                  if n.get_info() == node.get_info())
        # 超级网络模型中超级节点总数
        N = len(super_nodes)
        # 与该信息共同形成超级节点的用户数量
        A_i = len(set(str(n.get_user_name())
                      for n in super_nodes
                      if n.get_info() == node.get_info()))
        # 用户节点中的用户总数
        N_U = len(users)
        # 计算信息特征 I_SN
        if A_i > 0:  # 防止除以零的情况
            I_SN = (C_i ** 2 * N_U) / (N ** 2 * A_i)
        else:
            I_SN = 0

        # 赋值信息特征值给超级节点
        node.set_info_feature(I_SN)


# 加载情感词典文件
def load_sentiment_dictionary(file_path):
    sentiment_dict = {}
    with open(file_path, encoding='utf-8') as file:
        for line in file:
            word = line.strip()
            # 假设积极情感标签为 'positive'，消极情感标签为 'negative'
            sentiment_dict[word] = 'positive' \
                if word in positive_words \
                else 'negative' \
                if word in negative_words \
                else 'neutral'
    return sentiment_dict


# 读取积极和消极情感词典文件
positive = r'E:\论文\代码\NTUSD_positive_simplified.txt'
positive_words = set(line.strip() for line in open(r'E:\论文\代码\NTUSD_positive_simplified.txt', encoding='utf-8'))
negative_words = set(line.strip() for line in open(r'E:\论文\代码\NTUSD_negative_simplified.txt', encoding='utf-8'))

# 合并情感词典
# sentiment_dictionary = load_sentiment_dictionary(positive_words, negative_words)
sentiment_dictionary = load_sentiment_dictionary(positive)


def calculate_sentiment_scores(keywords, sentiment_dictionary):
    sentiment_score = 0
    for kw in keywords:
        # 将文本分割成单词
        # words = t.split()
        # print(words)
        # 初始化情感值为0
        sentiment_score = 0
        # 遍历文本中的每个单词

        if kw in sentiment_dictionary:
            sentiment_score += 1 \
                if sentiment_dictionary[kw] == 'positive' else -1 \
                if sentiment_dictionary[kw] == 'negative' else 0
        # 将情感值添加到列表中

    if (len(keywords) == 0):
        sentiment_score = 0
    else:
        sentiment_score = sentiment_score / len(keywords)
    return sentiment_score


for i in super_nodes:
    sen_scores = calculate_sentiment_scores(i.get_keywords(), sentiment_dictionary)
    i.set_sentiment(sen_scores)

cal_in(users)
cal_cc(users)
for user, inDegree in in_list[0].items():
    user_name = user.get_user_name()  # 获取用户名称
    user.set_user_in(inDegree)
    for i in users:
        if user.get_user_name() == i.get_user_name():
            i.set_user_in(float(inDegree))

for user, btw in bwt_list[0].items():
    user_name = user.get_user_name()  # 获取用户名称
    user.set_user_btw(btw)
    for i in users:
        if user.get_user_name() == i.get_user_name():
            i.set_user_btw(float(btw))

# 存储用户的接近中心度
for user, cc in cc_list[0].items():
    user_name = user.get_user_name()  # 获取用户名称
    user.set_user_cc(cc)
    for i in users:
        if user.get_user_name() == i.get_user_name():
            i.set_user_cc(float(cc))


# 计算用户特征
def cal_user_feature():
    for user in users:
        user_name = user.get_user_name()  # 获取用户名称
        user_cc = user.get_user_cc()  # 获取用户中心度
        user_btw = user.get_user_btw()  # 获取用户介于中心度
        user_in = user.get_user_in()  # 获取用户入度
        user_feature = user_cc + user_btw + user_in
        user.set_user_feature(user_feature)


cal_user_feature()
cal_info_feature()


# 计算用户特征相似度
def cal_user_fea_sim(node_i, node_j):
    if node_i.get_user_name() == node_j.get_user_name() and node_j.get_com() == node_j.get_com():
        return 1
    for i in users:
        if node_i.get_user_name() == i.get_user_name():
            i_in = i.get_user_in()
            i_btw = i.get_user_btw()
            i_cc = i.get_user_cc()
            # print("i_in:"+str(i_in))
        if node_j.get_user_name() == i.get_user_name():
            j_in = i.get_user_in()
            j_btw = i.get_user_btw()
            j_cc = i.get_user_cc()

    if i_in == 0 and i_btw == 0 and i_cc == 0:
        return 0
    if j_in == 0 and j_btw == 0 and j_cc == 0:
        return 0

    sim_user = (i_in * j_in + i_btw * j_btw + i_cc * j_cc) / math.sqrt(
        pow(i_in * j_in, 2) + pow(i_btw * j_btw, 2) + pow(i_cc * j_cc, 2))
    return sim_user


# 用于计算一个关键词集中每个关键词的特征值
def cal_kw_value(keywords):
    kw_total = len(keywords)  # 具体某个关键词集的关键词个数
    TF = 1 / kw_total  # 每个关键词的出现次数都是1,则TF为倒数
    Ni = len(super_nodes)  # 所有用户的信息总数
    KW_dict = {}  # 存储具体关键词的DF值的映射
    for i in keywords:
        DF = 0  # 存储具体关键词出现在所有信息中的次数
        for j in super_nodes:
            if i in j.get_keywords():
                DF += 1

        KW_dict[i] = TF * math.log(Ni / DF)

    return KW_dict


# 计算关键词相似度
def cal_kw_sim(node_i, node_j):
    i_len = len(node_i.get_keywords())
    j_len = len(node_j.get_keywords())
    sim_kw = 0
    if i_len == 0:
        return sim_kw
    if j_len == 0:
        return sim_kw
    else:
        i_kw = cal_kw_value(node_i.get_keywords())
        j_kw = cal_kw_value(node_j.get_keywords())
        lenth = 0
        if len(node_i.get_keywords()) < len(node_j.get_keywords()):
            lenth = len(node_i.get_keywords())
        else:
            lenth = len(node_j.get_keywords())

        for i in range(lenth):
            sim_kw += i_kw[node_i.get_keywords()[i]] * j_kw[node_j.get_keywords()[i]] / \
                      math.sqrt(pow(i_kw[node_i.get_keywords()[i]], 2) + pow(j_kw[node_j.get_keywords()[i]], 2))

        return sim_kw


# test_sim = cal_kw_sim(super_nodes[2], super_nodes[3])


# 计算情感相似度
def cal_sentiment_sim(node_i, node_j):
    if node_i.get_sentiment() == node_j.get_sentiment():
        return 1
    else:
        return (node_i.get_sentiment() * node_j.get_sentiment()) / abs(node_i.get_sentiment() - node_j.get_sentiment())


# 假设有一个函数 sim(SN_i, SN_j) 来计算超级节点之间的相似度
def cal_edge_sim(node_i, node_j):
    sim = 1 / 3 * (cal_user_fea_sim(node_i, node_j)) + 1 / 3 * (cal_kw_sim(node_i, node_j)) + 1 / 3 * (
        cal_sentiment_sim(node_i, node_j))
    return sim


# SNR迭代
def calculate_SNR_optimized():
    n = len(super_nodes)
    convergence_threshold = 0.001  # 可以调整收敛阈值
    print("迭代开始")

    # 预先计算并存储每个节点与其他所有节点的相似度
    similarity_matrix = [[cal_edge_sim(node_i, node_j)
                          for node_j in super_nodes]
                         for node_i in super_nodes]
    SNR_change = 1.0
    counter = 1

    while True:
        # 缓存每个节点的旧SNR值
        old_SNR_values = [node.get_SNR_value() for node in super_nodes]

        # 计算新的 SNR 值
        new_SNR_values = []
        for i, node_i in enumerate(super_nodes):
            I_SNi = node_i.get_info_feature()
            sum_sim = sum(
                similarity_matrix[i][j] * node_j.get_SNR_value()
                for j, node_j in enumerate(super_nodes)
                if i != j
            )
            n_j = 100  # 假设的节点j的n值，这里可以根据实际情况调整
            SNR_new = (1 - I_SNi) / n + I_SNi * sum_sim / n_j \
                if n_j > 0 \
                else 0
            new_SNR_values.append(SNR_new)
        # 计算两次迭代之间的最大变化量

        # SNR_change = max(abs(old_SNR - new_SNR) for old_SNR, new_SNR in zip(old_SNR_values, new_SNR_values))
        # 更新节点的 SNR 值
        for node, new_SNR, old_SNR in zip(super_nodes, new_SNR_values, old_SNR_values):
            node.set_SNR_value(new_SNR)
            SNR_change = min(SNR_change, abs(old_SNR - new_SNR))  # 更新最大SNR变化值
        # SNR_change = abs(SNR_change)
        # print("第" + str(counter) + "次迭代的最大变化量:"+str(SNR_change))
        # print(old_SNR_values[0])
        # print("SNR_change:"+str(SNR_change))

        counter += 1

        # 检查是否收敛
        if SNR_change < convergence_threshold:
            break


# 计算用户分数
def cal_user_score():
    print("计算用户分数")
    for i in users:
        u_score = 0
        count = 0
        for j in super_nodes:
            if i.get_user_name() == j.get_user_name():
                u_score += j.get_SNR_value()
                count += 1
        user_score = u_score / count
        i.set_user_score(user_score)


# 创建一个字典来存储唯一的 User 对象
unique_users = {}

# 遍历列表，根据 user_name 去重
for user in users:
    # print(user.get_user_name())
    if user.user_name not in unique_users:
        unique_users[user.user_name] = user

# 通过字典的值创建一个新的去重后的列表
users = list(unique_users.values())
print("总用户数:" + str(len(users)))
# 创建用户网络
# users = list(userSet)

# SNR迭代
calculate_SNR_optimized()
print("迭代完成")
cal_user_score()
users.sort(key=lambda x: x.get_user_score(), reverse=True)
for t in range(0, 101):
    print(users[t].get_id())
