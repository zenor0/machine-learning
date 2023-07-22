import torch

# 创建一个目标张量
target = torch.zeros(5, 3, dtype=torch.float)  # 指定目标张量的数据类型为torch.float
print("目标张量：\n", target)

# 创建一个源张量
source = torch.tensor([2, 4, 6], dtype=torch.float)  # 指定源张量的数据类型为torch.float

# 定义索引
index = torch.tensor([1, 3, 0])

# 将索引张量扩展为与目标张量相同的维度
index = index.unsqueeze(1).expand(-1, target.size(1))

# 在第0维度上按照索引进行赋值操作
target.scatter_(dim=0, index=index, src=source)
print("赋值后的目标张量：\n", target)
import matplotlib
