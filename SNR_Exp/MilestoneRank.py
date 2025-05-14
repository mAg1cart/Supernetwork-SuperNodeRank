# 算法1 候选集生成
# Input：用户集合V(N个)、一些拓扑特征W、聚类个数K
# Output：候选集合L(M个)
from random import choice
import math
from numpy import argmax
import networkx as nx
import pandas as pd
import numpy as np
import random
import time
'''
# G = (V,E,R)
# 图 = (用户集，边集，邻接矩阵)
'''
V = ["1", "2", "3", "4"]
E = (["1", "2"], ["1", "3"], ["1", "4"], ["2", "1"])
R = [[0, 1, 1, 1],
    [1, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]]
examG = [V, E, R]

print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))

#获取excel中的数据
def GetData():
    getdata=pd.read_excel(r'明星.xlsx')
    row_num = len(getdata.index.values)
    col_num = len(getdata.columns.values)
    e1 = []
    v = []
    i = 0
    while i<row_num:
        if str(getdata.loc[i].values[3]) not in v:
            v.append(str(getdata.loc[i].values[3]))
        if str(getdata.loc[i].values[9]) not in v:
            v.append(str(getdata.loc[i].values[9]))
        if ([str(getdata.loc[i].values[3]),str(getdata.loc[i].values[9])] not in e1) and (str(getdata.loc[i].values[3]) != str(getdata.loc[i].values[9])):
            e1.append([str(getdata.loc[i].values[3]),str(getdata.loc[i].values[9])])
        i = i + 1
    e = tuple(e1)
    r = np.zeros((len(v),len(v)))
    for k in e:
        for i in range(len(v)):
            if v[i] == k[0]:
                for j in range(len(v)):
                    if v[j] == k[1]:
                        r[i][j] = 1
    return getdata,v,e,r
getdata,V,E,R = GetData()
print(len(V))

# 基础公式 注意R是邻接矩阵
def idg(V,E,R,u):  # 入度    计算u所在的列（有向图矩阵是 行->列）的和
    uidg = 0
    uindex = V.index(u)  # 找不到u会报错
    for i in range(len(R)):
        uidg += R[i][uindex]
    return uidg


# 给下面两跳聚类系数用的函数，获取u的一跳追随者
def myFollowers(V,E,R,u):  # 记录u所在的列下，为1的行
    foll = {u}
    for i in range(len(R)):
        if R[i][V.index(u)] == 1:  # 遍历u所在的列，行i为1的时候，放入集合
            foll.add(V[i])
    foll.remove(u)  # 移除u！！！
    return foll


def myFollowings(V,E,R, u):  # 记录u所在的行下，为1的列
    foll = {u}
    for i in range(len(R)):
        if R[V.index(u)][i] == 1:  # 遍历u所在的行，列i为1的时候，放入集合
            foll.add(V[i])
    foll.remove(u)
    return foll


# 给下面两跳聚类系数用的函数，获取MN
def getMN(V,E,R, v):  # 获取邻近点之间边的条数（有向图用，无向图应该要除以个2）
    M = 0
    N = 0
    near = myFollowers(V,E,R, v)
    near.update(myFollowings(V,E,R, v))  # 邻近点集合 这里认为只要有边，就是邻近点
    N = len(near)
    for u in near:
        for v in near:
            M += R[V.index(u)][V.index(v)]  # 统计邻近点之间的边条数
    return M, N

def clc(V,E,R, u):  # 两跳聚类系数
    P = {u}  # u两跳距离内的跟随者,u拿来初始化，获取P的时候会去掉
    n = 0  # P的大小
    M = 0  # 邻近点 之间的 边 条数
    N = 0  # 邻近点 个数（入度）
    # 获取P：在R中，记录u所在的列中的跟随者（一跳），再记录这些跟随者的跟随者
    P = myFollowers(V,E,R, u)  # 放入一跳跟随者
    list_P = []
    for v in P:
        list_P.insert(0,v)
    for v in list_P:  # 放入两跳跟随者
        P.update(myFollowers(V,E,R, v))
    # 已获取P
    # 获取其它参数
    n = len(P)
    bigclc = 0
    for v in P:  # 计算求和部分
        MN = getMN(V,E,R, v)
        M = MN[0]
        N = MN[1]
        if(N==0 or N==1):
            bigclc+=0
        else:
            bigclc += M / (N * (N - 1))

    if n == 0:
        return 1
    c = bigclc / n
    return c


def btw(V,E,R, u):  # 介数中心度
    nxG = nx.Graph()
    nxG.add_nodes_from(V)
    nxG.add_edges_from(E)
    b = nx.centrality.betweenness_centrality(nxG, normalized=False, weight=None)  # 杀鸡用牛刀
    return b[u]


def cen(V,E,R, u):  # 中心度
    c = clc(V,E,R, u)
    if c == 0:
        return idg(V,E,R, u) * btw(V,E,R, u)
    cen = idg(V,E,R, u) * btw(V,E,R, u) / c
    return cen

# 相似度   todo：优化：生成一张相似度表，直接查找就好，不用每次调用都算一遍。另外没有矩阵计算，不用np
def dis(V,E,R, v, u):
    X = idg(V,E,R, u) - idg(V,E,R, v)
    Y = clc(V,E,R, u) - clc(V,E,R, v)
    Z = btw(V,E,R, u) - btw(V,E,R, v)
    Q = cen(V,E,R, u) - cen(V,E,R, v)
    return math.sqrt(pow(X, 2) + pow(Y, 2) + pow(Z, 2) + pow(Q, 2))


# 拓扑特征 这里传入的C是V的一个子集
def Cidg(V,E,R, C,feature_N):  # 平均入度
    Sum = 0
    for v in C:
        Sum += feature_N[V.index(v)][0]
    return Sum / len(C)


def Cclc(V,E,R, C,feature_N):  # 平均两跳聚类系数
    Sum = 0
    for v in C:
        Sum += feature_N[V.index(v)][1]
    return Sum / len(C)


def Cbtw(V,E,R, C,feature_N):  # 平均介数
    Sum = 0
    for v in C:
        Sum += feature_N[V.index(v)][2]
    return Sum / len(C)


def Ccenter(V,E,R, C,feature_N):  # 平均中心度
    Sum = 0
    for v in C:
        Sum += feature_N[V.index(v)][3]
    return Sum / len(C)


#初始化聚类中心
def begin_cluster_center(data_points,k):
    center=[]
    length=len(data_points)#长度
    rand_data = random.sample(range(0,length), k)#生成k个不同随机数
    for i in range(k):#得出k个聚类中心(随机选出)
        center.append(data_points[rand_data[i]])
    return center,rand_data

def dis_seed(N,w):
    X = N[0] - w[0]
    Y = N[1] - w[1]
    Z = N[2] - w[2]
    Q = N[3] - w[3]
    return math.sqrt(pow(X, 2) + pow(Y, 2) + pow(Z, 2) + pow(Q, 2))

def kidg(V,E,R,u,L):  # 入度    计算u所在的列（有向图矩阵是 行->列）的和
    uidg = 0
    uindex = V.index(u)  # 找不到u会报错
    for i in range(len(R)):
        if V[i] in L:
            uidg += R[i][uindex]
    return uidg
def kclc(V,E,R, u,L):  # 两跳聚类系数
    P = {u}  # u两跳距离内的跟随者,u拿来初始化，获取P的时候会去掉
    n = 0  # P的大小
    M = 0  # 邻近点 之间的 边 条数
    N = 0  # 邻近点 个数（入度）
    # 获取P：在R中，记录u所在的列中的跟随者（一跳），再记录这些跟随者的跟随者
    P = myFollowers(V,E,R, u)  # 放入一跳跟随者
    list_P = []
    for v in P:
        list_P.insert(0,v)
    for v in list_P:  # 放入两跳跟随者
        P.update(myFollowers(V,E,R, v))
    # 已获取P
    # 获取其它参数
    n = len(P)
    bigclc = 0
    for v in P:  # 计算求和部分
        if v in L:
            MN = getMN(V,E,R, v)
            M = MN[0]
            N = MN[1]
            if(N==0 or N==1):
                bigclc+=0
            else:
                bigclc += M / (N * (N - 1))
    if n == 0:
        return 0
    c = bigclc / n
    return c
def kbtw(V,E,R, u,L):  # 介数中心度
    nxG = nx.Graph()
    E1 = []
    nxG.add_nodes_from(L)
    for e in E:
        if (E[0] in L) and (E[1] in L):
            E1.append(e)
    nxG.add_edges_from(E1)
    b = nx.centrality.betweenness_centrality(nxG, normalized=False, weight=None)  # 杀鸡用牛刀
    return b[u]
def kcen(V,E,R, u,L):  # 中心度
    if(clc(V,E,R, u)==0):
        return 0
    return kidg(V,E,R, u,L) * kbtw(V,E,R, u,L) / kclc(V,E,R, u,L)
# 第一阶段：聚类生成候选集
#def candidates_generator(V,E,R, W, K):
def candidates_generator(V,E,R,K):
    print('开始聚类')
    #V = G.V
    # 获取种子（聚类中心）todo:和原算法不同
    feature_N = []
    N = len(V)  # 计算出有N个用户
    print(N)
    for i in range(N):
        if N % 10 == 0:
            print(i)
        feature_N.append([idg(V,E,R, V[i]), clc(V,E,R, V[i]), btw(V,E,R, V[i]), cen(V,E,R, V[i])])
    distance_list = []
    print('计算距离')
    for i in range(N):
        distance_list_list = []
        for j in range(N):
            distence = dis_seed(feature_N[i], feature_N[j])
            distance_list_list.append(distence)
        distance_list.append(distance_list_list)
    seeds = []
    seeds_i = []
    D = []  # 容量为N的距离容器
    for user in V:  # 设置其容量，初始化Dj
        D.append(100000)
    # Sum = 0  # 记录已经选择了多少个聚类中心（后面用作终止条件）
    print("正在获取种子")
    seeds,seeds_i = begin_cluster_center(V,1)#随机获得一个种子

    for i in range(K-1):  # 寻找k个聚类中心
        for j in range(N):  # 这个聚类中心距离现存中心距离最大【填写Dj列表】
            for seed in seeds:  # 确定最小距离（和现存的中心比较）【算某个Dj】
                #print(V[j])
                distence = distance_list[V.index(seed)][j]
                if D[j] > distence:
                    D[j] = distence
        # 找最大的Dj放入种子库中
        seeds.append(V[D.index(max(D))])
        seeds_i.append(D.index(max(D)))
    print(len(seeds))
    # 种子获取完毕
    print("种子获取完毕")
    Cluster = [[] for i in range(K)]
    flag = False
    W = []
    distance_list = []

    for i in range(K):
        W.append(0)
        distance_list_list = []
        for user in V:
            distence = dis_seed(feature_N[i], feature_N[V.index(user)])
            distance_list_list.append(distence)
        distance_list.append(distance_list_list)

    while not flag:
        pre_seeds = seeds
        flag = True
        # 聚类
        Cluster = [[] for i in range(K)]  # 是说这个写法可以创建不定长二维数组
        for i in range(len(Cluster)):
            Cluster[i].append(seeds[i])
        L = []
        for user in V:  # 对每一个用户进行分类
            userDcenter = []  # 容量为k的距离容器
            for seed in seeds:  # 【填写Dcenter】
                userDcenter.append(distance_list[seeds.index(seed)][V.index(user)])
            # 划分到距离最小的那个集合
            if user not in seeds:
                Cluster[userDcenter.index(min(userDcenter))].append(user)

        # 更新每个聚类中心的拓扑特征
        for seed in seeds:
            i = seeds.index(seed)
            W[i] = [Cidg(V,E,R, Cluster[i],feature_N), Cclc(V,E,R, Cluster[i],feature_N), Cbtw(V,E,R, Cluster[i],feature_N), Ccenter(V,E,R, Cluster[i],feature_N)]
        # 更新聚类中心
        for i in range(K):
            min_dis = 10000000
            min_user = ''
            for user in Cluster[i]:
                distance = dis_seed(W[i], feature_N[V.index(user)])
                if distance < min_dis:
                    min_dis = distance
                    min_user = user
            if min_user == '':
                for v in V:
                    if v not in seeds:
                        seeds[i] = v
                        min_user = v
                        break
            else:
                seeds[i] = min_user
            seeds_i[i] =  V.index(min_user)
        for seed in seeds:
            if seed not in pre_seeds:
                flag = False
        #更新feature_N和distance_list
        feature_N = []
        distance_list = []
        for clu in Cluster:
            for i in range(len(clu)):
                feature_N.append([kidg(V,E,R, clu[i],clu), kclc(V,E,R, clu[i],clu), kbtw(V,E,R, clu[i],clu), kcen(V,E,R, clu[i],clu)])
        for i in range(K):
            distance_list_list = []
            for user in V:
                distence = dis_seed(feature_N[i], feature_N[V.index(user)])
                distance_list_list.append(distence)
            distance_list.append(distance_list_list)

        break

    # 找到那个最好的聚类
    SeedsCenter = []
    for seed in seeds:
        SeedsCenter.append(0)
    for seed in seeds:
        i = seeds.index(seed)
        SeedsCenter[i] = cen(V,E,R, seed)
    print("聚类中心的值和个数")
    for i in range(6):
        print(W[i])
        print(len(Cluster[i]))
    for i in range(K):
        if len(L) < len(Cluster[i]):
            L = Cluster[i]
    #candidate = argmax(SeedsCenter)  # arg是索引的意思，是np的函数，上面X.index(max(Y))应该可以改成这个函数
    #L = Cluster[candidate]

    return L

L = candidates_generator(V,E,R,6)

print("聚类长度")
print(len(L))
# 第二阶段：计算领导力，排名后选择
#转发 L为分类后的
def fa(V,E,R,L,getdata):
    fwd_list = dict()
    row_num = len(getdata.index.values)
    fwdid = []
    num = 0
    for i in range(len(L)):
        fwd_list[L[i]] = 0
    for j in range(row_num):
        if (str(getdata.loc[j].values[9]) in L) and (str(getdata.loc[j].values[12]) == '2'):
            if getdata.loc[j].values[0] not in fwdid:
                fwdid.append(getdata.loc[j].values[0])
                fwd_list[str(getdata.loc[j].values[9])] = fwd_list[str(getdata.loc[j].values[9])] + 1
                num += 1
    return fwd_list
fwd_list = fa(V,E,R,L,getdata)

#发布
def pa(V,E,R,L,getdata):
    pub_list = dict()
    row_num = len(getdata.index.values)
    pubid = []
    num = 0
    for i in range(len(L)):
        pub_list[L[i]] = 0
    for j in range(row_num):
        if str(getdata.loc[j].values[3]) in L:
            if getdata.loc[j].values[0] not in pubid:
                pubid.append(getdata.loc[j].values[0])
                pub_list[str(getdata.loc[j].values[3])] = pub_list[str(getdata.loc[j].values[3])] + 1
                num += 1
    return pub_list
pub_list = pa(V,E,R,L,getdata)

#评论
def ea(V,E,R,L,getdata):
    eva_list = dict()
    row_num = len(getdata.index.values)
    num = 0
    for i in range(len(L)):
        eva = 0
        for j in range(row_num):
            if (str(getdata.loc[j].values[9]) == L[i]) and (str(getdata.loc[j].values[12]) == '1'):
                eva += 1
                num += 1
        eva_list[L[i]] = eva
    return eva_list
eva_list = ea(V,E,R,L,getdata)

#UA
def ua(V,E,R,L,fwd_list,pub_list,eva_list):
    ua_list = dict()
    fwd_sum = 0
    pub_sum = 0
    eva_sum = 0
    for i in L:
        fwd_sum += fwd_list[i]
        pub_sum += pub_list[i]
        eva_sum += eva_list[i]
    for i in L:
        try:
            ua_list[i] = 0.33*fwd_list[i]/fwd_sum + 0.33*pub_list[i]/pub_sum + 0.33*eva_list[i]/eva_sum
        except:
            ua_list[i] = 0
    return ua_list
ua_list = ua(V,E,R,L,fwd_list,pub_list,eva_list)

#CR
def cal_CR(V,E,R,L,pub_list,fwd_list):
    cr_list = dict()
    row_num = len(getdata.index.values)
    for u in L:
        cr = 0
        num = 0
        for i in range(row_num):
            if str(getdata.loc[i].values[3]) == u:
                num += 1
        if (pub_list[u] + fwd_list[u]) != 0:
            cr = num / (pub_list[u] + fwd_list[u])
            cr_list[u] = cr
        else:
            cr_list[u] = 0
    return cr_list
cr_list = cal_CR(V,E,R,L,pub_list,fwd_list)

#AD
def cal_AD(V,E,R,L,pub_list,fwd_list,eva_list,cr_list):
    UI_list = dict()
    row_num = len(getdata.index.values)
    for u in L:
        following_list_u = []
        following_list = list(myFollowers(V,E,R,u))
        for k in following_list:
            if k in L:
                following_list_u.append(k)
        AD_sum = 0
        for v in following_list_u:
            #fwd_v_u = 0
            eva_v_u = 0
            following_list_v = list(myFollowers(V,E,R,v))
            fwd_pub_following = 0
            for i in following_list_v:
                if i not in L:
                    following_list_v.remove(i)
                else:
                    fwd_pub_following += (fwd_list[i] + pub_list[i])
            if fwd_pub_following != 0:
                fwd_pub_following = (fwd_list[u]+pub_list[u])/fwd_pub_following
            else:
                fwd_pub_following = 0
            for i in range(row_num):
                if (str(getdata.loc[i].values[3]) == u) and (str(getdata.loc[i].values[9]) == v):
                    eva_v_u += 1
            if (eva_list[v] + fwd_list[v])==0:
                fwd_eva = 0
            else:
                fwd_eva = eva_v_u / (eva_list[v] + fwd_list[v])
            AD_sum += (fwd_pub_following * fwd_eva * cr_list[v])
        UI_list[u] = AD_sum + cr_list[u]
    return UI_list
UI_list = cal_AD(V,E,R,L,pub_list,fwd_list,eva_list,cr_list)

#center
def cal_center(V,E,R,L):
    #中心度
    cen_list = dict()
    for v in L:
        #print(v)
        cen_list[v] = cen(V,E,R,v)
    return cen_list
cen_list = cal_center(V,E,R,L)


#领导力
def leadership(L,ua_list,UI_list,cen_list):
    leadership_list = dict()
    for u in L:
        leadership_list[u] = ua_list[u] * UI_list[u] * cen_list[u]
    return leadership_list
leadership_list = leadership(L,ua_list,UI_list,cen_list)
leadership_list = dict(sorted(leadership_list.items(), key=lambda x: x[1],reverse=True))
Cluster = []

NUMS = 10    #领导数
print("意见领袖")
for i in range(NUMS):
    Cluster.append(list(leadership_list.keys())[i])
print(Cluster)
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
