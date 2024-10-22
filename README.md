# Parameter_Optimization
这里采用的参数优化算法有梯度下降法(Gradient Desent),粒子数算法(PSO)，模拟退火(Simulated Annealing)，蒙特卡罗全局模拟(Monte Carlo)。
问题的背景是华为开发者大赛第三题https://developer.huaweicloud.com/competition/competitions/1000000101/test  。这个问题用单一的方法很难优化，所以采取多种方法结合。每一种算法的全局搜索能力与局部搜索能力都不同，后面陆续会有其它的方法以及例子。https://www.jianshu.com/p/eead09fa9347 给出了优化算法核心的思想以及程序（github）。

# 梯度下降算法
剩下的两种方法以后补充其它的例子，来源于https://github.com/GaoBoYu599/Optimization_Algorithm
* 梯度下降算法速度较慢、迭代次数较大，并且最后的结果是近似值。给定随机扰动结果好则接受反之不接受。
* 牛顿法利用函数的二阶泰勒展开近似，可以一步到位（收敛很快）！并且结果的精度很高！缺点是需要用到海森矩阵，即函数的二阶导！
* 共轭梯度法是介于梯度下降和牛顿法之间的折中方法，既有牛顿法的收敛速度，又不需要用到函数的二阶导！推荐这种方法！

# 粒子数算法
## 原始的粒子数算法
PSO算法的核心是利用鸟类再谷场寻找食物的思想，设想这样一个场景：一群鸟在谷场随机搜索食物，但是这个区域只有一堆谷物，所有的鸟都不知道食物在哪里，但是知道他们离它有多远。一个最简单有效的策略十搜索离谷物最近的鸟的附近区域。在实际问题中每一个临时的解都是一只鸟，称之为“粒子”，所有粒子都有一个由被优化函数决定的适应值(fitness value),每个粒子还有速度决定飞行的方向和距离。然后在空间随机搜索。速度

$y=x^2$
<img src="https://latex.codecogs.com/gif.latex?v_{i&plus;1}=w*v_i&plus;c1*rand()*(Gbest1-theta_i)&plus;c2*rand()*(Gbest2-theta_i)&plus;c3*rand()*(Pbest-theta_i)" title="v_{i+1}=w*v_i+c1*rand()*(Gbest1-theta_i)+c2*rand()*(Gbest2-theta_i)+c3*rand()*(Pbest-theta_i)" />  
其中Gbest1，Gbest2是全局最优和次全局最优，Pbest是当前循环的最优，也可以只保留全局最优。  
<img src="https://latex.codecogs.com/gif.latex?theta_{i&plus;1}=theta_i&plus;v" title="theta_{i+1}=theta_i+v" />  
更多的信息可以参照：https://www.cnblogs.com/qw-blog/p/10338477.html 里面有更加相信的讲解。

### 说明
* 一般weight取值0.8全局搜索能力强，取值0.4局部搜索较强。
* c1,c3之和3到5，c1=1.4，c3=1.4是一个典型的取值。
* v还应该有一个上下界，保证速度不会太大。
* 粒子数一般20-30，可以迭代很多次，知道收敛。

## 改进后的粒子数算法
它的思想与PSO算法类似，只是我们的迭代公式不同。保证最优解不动，其余的解向最优解靠近，但是这种算法的全局搜索能力不如PSO。更新公式为  
<img src="https://latex.codecogs.com/gif.latex?theta_i=p*theta_i&plus;(1-p)*theta\_g_i" title="theta_i=p*theta_i+(1-p)*theta\_g_i" />  
其中p是概率可以按照  
<img src="https://latex.codecogs.com/gif.latex?p=p_{min}&plus;(p_{max}-p_{min})*\frac{\log_{10}{k&plus;1}}{\log_{10}{times}}" title="p=p_{min}+(p_{max}-p_{min})*\frac{\log_{10}{k+1}}{\log_{10}{times}}" />  
更新。使得最开始向最优解前进快，逐渐变慢，避免漏掉最优解。选取log10函数是为了步长小的时候迭代次数更多。这一种方法类似捕鱼收网，后面我叫这种方法为捕鱼算法。

# 模拟退火算法
模拟退火算法是从一个较高的温度出发，温度逐渐降低，降低按照公式T_max=0.95*T_max。在每一个温度迭代L次，在每一次执行如下过程。给定参数以随机的扰动，如果当前结果更好，则接受，如果当前结果相比上一次不是很好，那么以概率  
<img src="https://latex.codecogs.com/gif.latex?p=e^{-\frac{valueLast-valueNow}{T_{max}}}" title="p=e^{-\frac{valueLast-valueNow}{T_{max}}}" />  
接受结果（ rand()<p ） 。https://www.luogu.org/blog/m-sea/qian-tan-SA 有张图很好的说明了模拟退火的过程，表现了模拟退火具有跳出局部最优解的能力。




# 算法的比较
MC，SA，PSO都具有全局搜索能力。但是全局搜索能力十逐渐上升的。捕鱼算法和梯度下降都具有局部搜索能力，但是捕鱼算法的效率高很多。更容易找到最优解，也有一定的几率跳出局部最优。这里有一些结果————[4.7238,5.4404,1.5461,5.0168,5.2693]结果是0.0216:[4.7231,5.4567,1.5493,5.0330,5.2683]结果是0.0230:[4.6957,4.8711,4.7271,5.04375.6928]结果是0.0186;[4.7107,4.4941,4.6916,3.0778,2.1222]结果是0.0181;[1.5763,3.5455,4.7141,3.9661,3.2147]结果是0.0180。效果最好的是模拟退火算法，仅仅用单一的方法就可以得到想要的结果，而且概率超过70%(实际两次都成功了)，可能这种算法最不容易陷入局部最优，因为它不止搜索局部最优附近的区域。相比于适合所有方法的MC，它的效率高很多。[3.1405,3.1926,3.3749,-0.2023,3.0708]结果是0.020;[-4.7501,-1.0291,1.6055,0.5677,0.2289]结果是0.0185;[1.5723,4.0052,4.7063,1.5185,14.0457]结果是0.0225;[4.7269,1.6153,4.6922,0.6664,1.4218]结果是0.022;[1.5712,1.6153,1.5599,5.5817]结果是0.021.
* MC+newPSO一定程度上可以实现想要的功能。但是只有在MC选择的数据很多的时候才有用。一般2000，3000，需要花费很多的时间。实际上运行时间也没有比第二种慢。
* oldPSO+newPSO可以满足需要oldPSO选择30个粒子，迭代100次。newPSO用第一种方法中好的结果加上边界值。迭代次数一般几次到几十次不等，但是也不是每次都有效,这些方法里面都会有引入随机数。
* SA+newPSo在实验的过程中，仅仅SA就完成了准确率大于0.018的任务，表明在许多的极值的情况下SA算法表现优异。可能这种算法最不容易陷入局部最优，因为它不止搜索局部最优附近的区域。相比于适合所有方法的MC，它的效率高很多。如果想要得到更高的效率可以考虑将两种方法结合，改进后的PSO算法拥有更加高效的局部搜索能力，这一点从算法的原理可以看出来。

ubuntu上面github的使用https://blog.csdn.net/godop/article/details/80500704
