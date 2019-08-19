# Parameter_Optimization
这里采用的参数优化算法有梯度下降法(Gradient Desent),粒子数算法(PSO)，模拟退火(Simulated Annealing)，蒙特卡罗全局模拟(Monte Carlo)。
问题的背景是华为开发者大赛第三题https://developer.huaweicloud.com/competition/competitions/1000000101/test  这个问题用单一的方法很难优化，所以采取多种方法结合的方法。每一种算法的全局搜索能力与局部搜索能力都不同。后面陆续会有其它的方法以及例子。
# 梯度下降算法
（剩下的两种方法以后补充其它的例子，来源于https://github.com/GaoBoYu599/Optimization_Algorithm）
* 梯度下降算法速度较慢、迭代次数较大，并且最后的结果是近似值；
* 牛顿法利用函数的二阶泰勒展开近似，可以一步到位（收敛很快）！并且结果的精度很高！缺点是需要用到海森矩阵，即函数的二阶导！
* 共轭梯度法是介于梯度下降和牛顿法之间的折中方法，既有牛顿法的收敛速度，又不需要用到函数的二阶导！推荐这种方法！
# 粒子数算法
$$  x = \dfrac{-b \pm \sqrt{b^2 - 4ac}}{2a} $$
