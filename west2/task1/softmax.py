import numpy as np

def softmax(x):
    # 计算指数函数
    exp_x = np.exp(x)
    # 计算每个元素的softmax值
    softmax_x = exp_x / np.sum(exp_x)
    return softmax_x


x = np.array([1.0, 2.0, 3.0])
softmax_x = softmax(x)
print(softmax_x)
