import matplotlib.pyplot as plt
import numpy as np

# 设置中文字体支持
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']  # 替换为你系统中支持的中文字体
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

def plot_feature_importance(feature_importance_dict, save_path, title='特征重要性排序', fig_size=(10, 6)):
    """
    绘制特征重要性排序图
    
    Args:
        feature_importance_dict (dict): 字典，键为特征名，值为特征重要性分数（浮点数）
        save_path (str): 图表保存路径
        title (str): 图表标题
        fig_size (tuple): 图表尺寸
    """
    # 将字典按特征重要性排序
    sorted_features = sorted(feature_importance_dict.items(), key=lambda x: x[1], reverse=False)
    
    # 分离特征名称和重要性分数
    feature_names = [item[0] for item in sorted_features]
    feature_scores = [item[1] for item in sorted_features]
    
    # 创建图表
    plt.figure(figsize=fig_size)
    
    # 创建水平柱状图
    y_pos = np.arange(len(feature_names))
    plt.barh(y_pos, feature_scores, color='skyblue', edgecolor='black')
    
    # 设置图表标题和轴标签
    plt.title(title)
    plt.xlabel('特征重要性分数')
    plt.ylabel('特征')
    
    # 设置y轴刻度标签
    plt.yticks(y_pos, feature_names)
    
    # 添加数值标签
    for i, v in enumerate(feature_scores):
        plt.text(v + 0.05, i, f'{v:.2f}', va='center', ha='left', fontsize=9)
    
    # 美化图表
    plt.tight_layout()
    plt.grid(axis='x', linestyle='--', alpha=0.7)
    
    # 保存图表
    plt.savefig(save_path)
    plt.close()  # 关闭图表释放内存

# 示例用法
if __name__ == "__main__":
    # 示例特征重要性字典
    feature_importance = {
        "可行驶里程": 2.1,
        "维修状态": 1.8,
        "上次维修时间": 1.2,
        "故障次数": 0.9,
        "历史故障类型": 0.6,
        "总行驶里程": 0.4,
        "车辆寿命": 0.3,
        "工作环境": 0.2,
        "运行条件": 0.1
    }
    
    # 保存路径
    save_path = "feature_importance.png"
    
    # 绘制图表
    plot_feature_importance(feature_importance, save_path, title='特征重要性排序')
    
    print(f"图表已保存到: {save_path}")