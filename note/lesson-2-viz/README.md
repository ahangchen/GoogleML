# Visualizing a Decision Tree 
> Google Machine Learning Recipes 2

> 官方中文博客 http://chinagdg.org/2016/03/machine-learning-recipes-for-new-developers/

> 视频地址 http://v.youku.com/v_show/id_XMTUzNDE5Mzg0MA==.html?f=26979872&from=y1.2-3.4.3

> Github工程地址 https://github.com/ahangchen/GoogleML

> 欢迎Star，也欢迎到[Issue区讨论](https://github.com/ahangchen/GoogleML/issues)

我们从Iris问题，学习决策树可视化，了解决策树工作过程。

## Why decision Tree

有很多分类器
- Artificial neural network
- Support Vector Machine
- Lions
- Tigers
- Bears

> 为啥有这么多动物……

### 决策树好处
- Easy to read and understand
- 仅有的可解释的几种模型之一（能理解分类器做决策的过程）

决策树就是一系列关于feature的判断作为结点，以label为叶子的一棵树。因此feature越好，结果也越好。

## Iris
经典机器学习问题：[识别三种Iris](https://en.wikipedia.org/wiki/Iris_flower_data_set)

可以在维基看到这个数据集的详细信息，共 50 * ３ = 150 条记录

四个feature：Sepal length, Sepal width, Petal length, Petal width

三个label：setosa, versicolor, virginica。

可以从sklearn中直接导入。

**组成**
- metadata: feature_names, target_names(这个其实就是label names)，描述数据用
- data: 具体feature数据，是一个数组，数组中的每个元素是dataset中的一条数据
- target: 具体label数据，是一个数组

## 目标
1. 导入数据
2. 训练分类器
3. 预测新的花的label
4. 查看决策树

## 测试数据
- 非训练数据的真实数据，测试分类器的准确度，
- 这里从dataset中抽出第0，第50，第100条作为测试数据
- numpy是一个Python的数据处理库，查看官方[Tutorial](https://docs.scipy.org/doc/numpy-dev/user/quickstart.html)学习更多
- 测试有很多内容，后面还会有。

## 环境
可视化使用了pydot，但Pycharm会升级anaconda中的包，导致找不到，我执行了
```
sudo /home/cwh/anaconda2/bin/conda install -p /home/cwh/anaconda2 pydot -y
```
重新安装pydot修复pydot找不到的问题；

另外pydot会找不到Graphviz，需要再安装
```
sudo /home/cwh/anaconda2/bin/conda install -p /home/cwh/anaconda2 Graphviz -y
```
然后将Graphviz添加到环境变量中，修改/etc/environment为以下内容，重启系统（我的系统是Ubuntu14.04LTS）：
```
PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/home/cwh/android-sdk-linux/ndk-bundle:/home/cwh/android-sdk-linux/platform-tools:/home/cwh/anaconda2/pkgs/graphviz-2.38.0-1/bin"
```

然后又会有Graphviz中找不到libgvplugin_pango.so.6的问题，根据[官网Issue的解答](http://www.graphviz.org/content/issue-warning-could-not-load-usrlibgraphvizlibgvpluginrsvgso6)，应该是少了依赖库
```
ldd /home/cwh/anaconda2/pkgs/graphviz-2.38.0-1/lib/graphviz/libgvplugin_pango.so.6
```

发现libpng16 not found，于是安装libpng16，在[这里](https://sourceforge.net/projects/libpng/?source=directory)下载，然后安装，

```
./configure
make
sudo make install
sudo ldconfig
```
再运行代码即可。


##代码
[Viz](../../src/viz.py)：以Iris为例，导入数据，训练分类器，预测，查看决策树

> 如果觉得我的文章对您有帮助，请随意打赏～

<img src="../../res/wxmoney.jpg" width = "400" height = "400" alt="图片名称" align=center />