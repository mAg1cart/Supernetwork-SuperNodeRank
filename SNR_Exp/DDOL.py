import math
import pandas as pd
import jieba
import numpy as np
# 读取数据集
df = pd.read_excel('明星.xlsx')

# 去除重复数据
# df.drop_duplicates(subset=['发文/转发内容'], keep='first', inplace=True)

# 定义社交信号的权重
social_signal_weights = {
    '评论数': 3,
    '转发数': 2,
    '点赞数': 4
}

# 计算ScoreImp
def calculate_score_imp(row):
    score_imp = (row['评论数'] * social_signal_weights['评论数'] +
                 row['转发数'] * social_signal_weights['转发数'] +
                 row['点赞数'] * social_signal_weights['点赞数'])
    return score_imp

df['ScoreImp'] = df.apply(calculate_score_imp, axis=1)

# 定义中文意见词列表
ListOp = ['好', '不好', '推荐', '喜欢', '赞', '差评']  # 初始列表，需要扩展

# 预处理和计算ScoreOp
def preprocess_and_scoreop(text, list_op):
    seg_list = jieba.lcut(text)
    return sum(word in list_op for word in seg_list)

df['ScoreOp'] = df['发文/转发内容'].apply(lambda x: preprocess_and_scoreop(x, ListOp))

# 确定alpha值
alpha = 0.5# 直接设置为0.5

# 计算CU值
# cu = (df['评论数'] + df['转发数'] + df['点赞数'])
cu = df['评论数']
df['CU'] = np.trunc(cu)
# 计算最终的ScoreInf
df['ScoreInf'] = alpha * df['ScoreImp'] + (1 - alpha) * df['ScoreOp']

# CR = CU/全部用户数
df['CR'] = df['CU']/10019

# 根据ScoreInf找出意见领袖
# opinion_leaders = df.sort_values(by='ScoreInf', ascending=False).\
#     drop_duplicates(subset=['发文/转发用户昵称'], keep='first')
# 首先，根据'ScoreInf'降序排序
df_sorted = df.sort_values(by='ScoreInf', ascending=False)

# 然后，对'发文/转发用户昵称'进行分组，并计算每个组的累计计数
df_sorted['cumcount'] = df_sorted.groupby('发文/转发用户昵称').cumcount()

# 过滤出每个用户昵称出现次数小于3的行
opinion_leaders = df_sorted[df_sorted['cumcount'] < 1]

# 重置索引，如果需要的话
opinion_leaders.reset_index(drop=True, inplace=True)

# 输出结果
# print("-----------------------")
# print(opinion_leaders[['发文/转发用户昵称', 'CU', 'CR']].head())
print("排名前100的用户的CU和CR的和")
ddol_sum_cu = 0
ddol_sum_cr = 0
counter = 0
max_its = 100
ddol_ol = []
print("总数:")
print(len(opinion_leaders))
print(opinion_leaders[['发文/转发用户昵称', 'CU', 'CR']])

for i in opinion_leaders.itertuples():
    if counter < max_its:
        cu_num = i.CU
        ddol_sum_cu += int(cu_num)
        ddol_sum_cr += float(i.CR)
        counter += 1
        ddol_ol.append(i)

print(counter)
print("CU:"+str(ddol_sum_cu)+" CR:"+str(ddol_sum_cr))
# 如果需要，可以将结果保存到文件
data = pd.DataFrame(ddol_ol)
#将前100条数据保存到Excel文件中
data.to_excel('ddol_result.xlsx', index=False, sheet_name='DDOL_OpinionLeaders')
print("写入完成")