电动车数据分析
概述
本项目使用Python进行电动车数据的分析和可视化。分析的数据集包含电动车的多种属性，如品牌、型号、电动续航里程等。

数据集
数据集包含以下主要字段：

Model Year: 车辆型号年份
Make: 车辆品牌
Electric Vehicle Type: 电动车类型（纯电动或插电式混合动力）
Electric Range: 电动续航里程
主要功能
数据预处理：删除不相关的字段，例如 VIN、DOL Vehicle ID 等。
抽样分析：由于数据量较大，使用随机抽样方法提取1000条数据进行进一步分析。
年份数据转换：将 Model Year 车辆型号年份字段从数字转换为字符串类型，以便于进行后续操作。
数据分组与可视化：根据年份和电动车类型对数据进行分组，并绘制线图来比较不同年份电动车类型的变化。
市场份额分析：计算每年前10大品牌的市场份额，并绘制相关图表。
经验累积分布函数（ECDF）：对 Model Year 和 Electric Range 进行ECDF分析。
小提琴图：使用小提琴图分析车辆型号年份与CAFV（清洁替代燃料车辆）资格之间的分布关系。
电动车续航里程分析：分析纯电动车（BEV）和插电式混合动力车（PHEV）的电动续航里程。
热力图：绘制热力图来分析不同变量之间的关系和模式。
使用说明
要运行此脚本，需要安装以下Python库：

pandas
matplotlib
seaborn
numpy
运行脚本前，确保电动车数据文件位于指定路径。