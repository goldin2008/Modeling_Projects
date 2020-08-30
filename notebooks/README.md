## Anomaly Detection, Outlier Analysis, Outlier Detection

> https://zhuanlan.zhihu.com/p/37132428

> https://github.com/waterfeeling/awesome-fraud-detection-literature/wiki/List-of-Papers

## Credit Card Transactions Fraud Detection

> https://www.cnblogs.com/bonelee/p/9089984.html


#### Credit Fraud || Dealing with Imbalanced Datasets

> https://www.kaggle.com/janiobachmann/credit-fraud-dealing-with-imbalanced-datasets

#### 反欺诈模型||处理不平衡数据集

> https://zhuanlan.zhihu.com/p/70602209

> https://zhuanlan.zhihu.com/p/70763004



## 特征缩放（Feature Scaling）
> https://www.cnblogs.com/HuZihu/p/9761161.html

> https://www.cnblogs.com/bjwu/p/8977141.html

### 归一化和标准化的区别：
归一化（normalization）：归一化是将样本的特征值转换到同一量纲下，把数据映射到[0,1]或者[-1, 1]区间内。

标准化（standardization）：标准化是将样本的特征值转换为标准值（z值），每个样本点都对标准化产生影响。

### 为什么要进行特征缩放？
#### 1. 统一特征的权重&提升模型准确性
如果某个特征的取值范围比其他特征大很多，那么数值计算（比如说计算欧式距离）就受该特征的主要支配。但实际上并不一定是这个特征最重要，通常需要把每个特征看成同等重要。归一化/标准化数据可以使不同维度的特征放在一起进行比较，可以大大提高模型的准确性。
#### 2. 提升梯度下降法的收敛速度
在使用梯度下降法求解最优化问题时， 归一化/标准化数据后可以加快梯度下降的求解速度。

### 具体使用哪种方法进行特征缩放？
在需要使用距离来度量相似性的算法中，或者使用PCA技术进行降维的时候，通常使用标准化（standardization）或均值归一化（mean normalization）比较好，但如果数据分布不是正态分布或者标准差非常小，以及需要把数据固定在 [0, 1] 范围内，那么使用最大最小值归一化（min-max normalization）比较好（min-max 常用于归一化图像的灰度值）。但是min-max比较容易受异常值的影响，如果数据集包含较多的异常值，可以考虑使用稳键归一化（robust normalization）。对于已经中心化的数据或稀疏数据的缩放，比较推荐使用最大绝对值归一化（max abs normalization ），因为它会保住数据中的０元素，不会破坏数据的稀疏性（sparsity）。

### 哪些机器学习模型必须进行特征缩放？
通过梯度下降法求解的模型需要进行特征缩放，这包括线性回归（Linear Regression）、逻辑回归（Logistic Regression）、感知机（Perceptron）、支持向量机（SVM）、神经网络（Neural Network）等模型。此外，近邻法（KNN），K均值聚类（K-Means）等需要根据数据间的距离来划分数据的算法也需要进行特征缩放。主成分分析（PCA），线性判别分析（LDA）等需要计算特征的方差的算法也会受到特征缩放的影响。

决策树（Decision Tree），随机森林（Random Forest）等基于树的分类模型不需要进行特征缩放，因为特征缩放不会改变样本在特征上的信息增益。

### 进行特征缩放的注意事项：
需要先把数据拆分成训练集与验证集，在训练集上计算出需要的数值（如均值和标准值），对训练集数据做标准化/归一化处理（不要在整个数据集上做标准化/归一化处理，因为这样会将验证集的信息带入到训练集中，这是一个非常容易犯的错误），然后再用之前计算出的数据（如均值和标准值）对验证集数据做相同的标准化/归一化处理。
