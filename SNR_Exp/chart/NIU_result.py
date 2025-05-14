import matplotlib.pyplot as plt			# 导入模块
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
plt.ylim(1000 , 40000)
plt.xlim(10 , 100)
# 设置X轴的刻度位置和样式

#plt.xticks([0, 10, 20, 30, 40, 50], ['1', '5', '10', '15', '20', '25', '30', '35', '40', '45', '50'])

plt.xticks([10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100], ['10', '15', '20', '25', '30', '35', '40', '45', '50', '55', '60', '65', '70', '75', '80', '85', '90', '95', '100'])
plt.yticks([5000, 10000, 20000, 30000, 36608], ['5000', '10000', '20000', '30000', '36608'])
plt.tick_params(axis='x', which='both', direction='in')  # 刻度朝内
# 设置Y轴的刻度位置和样式

plt.tick_params(axis='y', which='both', direction='in')  # 刻度朝内
plt.xlabel('Numbers of Opinion Leaders')
plt.ylabel('NIU')


# plt.rcParams['font.sans-serif'] = ['SimHei']  # 添加这条可以让图形显示中文
x_axis_data = list(range(10, 101, 5))

y_ddol_data = [3489, 5522, 7162, 9334, 10899, 14239, 17292, 18601, 19907, 21036, 21860, 22632, 22632, 24253, 25433, 26663, 27492, 29214, 30555]
               #36631, 38145, 43325, 45605, 48285, 49236]
y_mr_data = [1982, 2907, 4112, 5073, 5073, 6600, 7695, 8616, 9878, 11793, 12686, 13891, 14644, 16244, 17549, 18565, 20959, 22342, 23294]
             #33828, 37136, 41196, 44579, 47839, 49659]
y_uw_data = [1700, 8480, 16360, 22560, 28200, 33240, 37360, 40360, 43111, 45251, 47123]
             #48554,49768,50876,51936,52716,53236]

y_snr_data = [7530, 10162, 12512, 14730, 16687, 18322, 19895, 21377, 22798, 24152, 25359, 26527, 27609, 28604, 29543, 30402, 31180, 31762, 32166]

# #00FF00 #00FFFF #DC143C #1E90FF
# plot中参数的含义分别是横轴值，纵轴值，线的形状，颜色，透明度,线的宽度和标签
plt.plot(x_axis_data, y_mr_data, 'g^-', color='blue', alpha=0.5, linewidth=0.5, label='MilestonesRank', markersize = 9)
plt.plot(x_axis_data, y_ddol_data, 'ro-', color='green', alpha=0.5, linewidth=0.5, label='DDOL', markersize = 9)
# plt.plot(x_axis_data, y_uw_data, 'p-', color='orange', alpha=0.95, linewidth=0.5, label='UserNetwork', markersize = 9)
plt.plot(x_axis_data, y_snr_data, 'bs-', color='#FF0000', alpha=1, linewidth=0.5, label='SuperNetwork-SuperNodeRank', markersize = 9)

plt.legend(loc="upper left", prop={'size': 12})

plt.show()
