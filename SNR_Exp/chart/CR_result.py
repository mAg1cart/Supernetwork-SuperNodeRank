import matplotlib.pyplot as plt  # 导入模块
from matplotlib import rcParams

# 设置字体为Times New Roman
config = {
    "font.family": 'Times New Roman',
    # "font.size": 18,
}
fontsize = 13
# 更新字体样式
rcParams.update(config)

# 设置格式
# 显示标签，如果不加这句，即使在plot中加了label='一些数字'的参数，最终还是不会显示标签
plt.figure(figsize=(10, 7), dpi=300)
plt.ylim(0, 1.0)
plt.xlim(10, 100)
# 设置X轴的刻度位置和样式
# plt.xticks(x_axis_data, rotation=0)  # 刻度朝内显示，并旋转45度以便阅读
plt.xticks([10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],
           ['10', '15', '20', '25', '30', '35', '40', '45', '50', '55', '60', '65', '70', '75', '80', '85', '90', '95',
            '100'])
plt.yticks([0.1, 0.3, 0.5, 0.8, 1.0], ['0.1', '0.3', '0.5', '0.8', '1.0'])
# plt.tick_params(axis='x', which='both', direction='in')  # 刻度朝内
# 设置Y轴的刻度位置和样式
# plt.yticks(plt.yaxis.get_major_ticks(), rotation=1)  # 刻度朝内显示
# plt.tick_params(axis='y', which='both', direction='in')  # 刻度朝内
plt.xlabel('Numbers of Opinion Leaders')
plt.ylabel('C R')

# plt.rcParams['font.sans-serif'] = ['SimHei']  # 添加这条可以让图形显示中文
x_axis_data = list(range(10, 101, 5))

y_ddol_data = [0.095, 0.151, 0.196, 0.255, 0.298, 0.389, 0.433, 0.472, 0.508, 0.543, 0.575, 0.597, 0.618, 0.663, 0.695,
               0.728, 0.751, 0.798, 0.835]
# y_uw_data = [0.0339,0.1700,0.32705, 0.4510,0.5637,0.6645,0.7469,0.8068,0.8618,0.9046,0.9420]
y_snr_data = [0.206, 0.278, 0.342, 0.402, 0.456, 0.500, 0.543, 0.584, 0.623, 0.660, 0.693, 0.725, 0.754, 0.781, 0.807,
              0.830, 0.852, 0.868, 0.879]
y_mr_data = [0.054, 0.079, 0.112, 0.139, 0.157, 0.180, 0.210, 0.235, 0.270, 0.322, 0.347, 0.379, 0.400, 0.443, 0.479,
             0.507, 0.572, 0.610, 0.636]
# #00FF00 #00FFFF #DC143C #1E90FF
# plot中参数的含义分别是横轴值，纵轴值，线的形状，颜色，透明度,线的宽度和标签

plt.plot(x_axis_data, y_mr_data, 'g^-', color='blue', alpha=0.5, linewidth=0.3, label='MilestonesRank', markersize=9)
plt.plot(x_axis_data, y_ddol_data, 'o-', color='green', alpha=0.5, linewidth=0.3, label='DDOL', markersize=9)
# plt.plot(x_axis_data, y_uw_data, 'p-', color='orange', alpha=0.95, linewidth=0.3, label='SuperNodeRank', markersize = 9)
plt.plot(x_axis_data, y_snr_data, 'bs-', color='red', alpha=0.9, linewidth=0.3, label='SuperNetwork-SuperNodeRank',
         markersize=9)

plt.legend(loc="best", prop={'size': 12})

plt.show()
