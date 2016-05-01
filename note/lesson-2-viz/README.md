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
```
cwh@home:graphviz$ ldd /home/cwh/anaconda2/pkgs/graphviz-2.38.0-1/lib/graphviz/libgvplugin_pango.so.6
	linux-vdso.so.1 =>  (0x00007fffd25ef000)
	libgvc.so.6 => /home/cwh/anaconda2/pkgs/graphviz-2.38.0-1/lib/graphviz/../libgvc.so.6 (0x00007f539f5e0000)
	libltdl.so.7 => /usr/lib/x86_64-linux-gnu/libltdl.so.7 (0x00007f539f3b7000)
	libxdot.so.4 => /home/cwh/anaconda2/pkgs/graphviz-2.38.0-1/lib/graphviz/../libxdot.so.4 (0x00007f539f1b2000)
	libcgraph.so.6 => /home/cwh/anaconda2/pkgs/graphviz-2.38.0-1/lib/graphviz/../libcgraph.so.6 (0x00007f539ef9d000)
	libcdt.so.5 => /home/cwh/anaconda2/pkgs/graphviz-2.38.0-1/lib/graphviz/../libcdt.so.5 (0x00007f539ed98000)
	libpathplan.so.4 => /home/cwh/anaconda2/pkgs/graphviz-2.38.0-1/lib/graphviz/../libpathplan.so.4 (0x00007f539eb8f000)
	libpangocairo-1.0.so.0 => /usr/lib/x86_64-linux-gnu/libpangocairo-1.0.so.0 (0x00007f539e982000)
	libcairo.so.2 => /usr/lib/x86_64-linux-gnu/libcairo.so.2 (0x00007f539e677000)
	libpixman-1.so.0 => /usr/lib/x86_64-linux-gnu/libpixman-1.so.0 (0x00007f539e3ce000)
	libpng16.so.16 => not found
	libXrender.so.1 => /usr/lib/x86_64-linux-gnu/libXrender.so.1 (0x00007f539e1c4000)
	libX11.so.6 => /usr/lib/x86_64-linux-gnu/libX11.so.6 (0x00007f539de8e000)
	libXext.so.6 => /usr/lib/x86_64-linux-gnu/libXext.so.6 (0x00007f539dc7c000)
	libpangoft2-1.0.so.0 => /usr/lib/x86_64-linux-gnu/libpangoft2-1.0.so.0 (0x00007f539da67000)
	libharfbuzz.so.0 => /usr/lib/x86_64-linux-gnu/libharfbuzz.so.0 (0x00007f539d811000)
	libpango-1.0.so.0 => /usr/lib/x86_64-linux-gnu/libpango-1.0.so.0 (0x00007f539d5c4000)
	libgthread-2.0.so.0 => /usr/lib/x86_64-linux-gnu/libgthread-2.0.so.0 (0x00007f539d3c2000)
	libfontconfig.so.1 => /usr/lib/x86_64-linux-gnu/libfontconfig.so.1 (0x00007f539d185000)
	libxml2.so.2 => /usr/lib/x86_64-linux-gnu/libxml2.so.2 (0x00007f539ce1e000)
	libdl.so.2 => /lib/x86_64-linux-gnu/libdl.so.2 (0x00007f539cc1a000)
	libz.so.1 => /lib/x86_64-linux-gnu/libz.so.1 (0x00007f539ca00000)
	libgobject-2.0.so.0 => /usr/lib/x86_64-linux-gnu/libgobject-2.0.so.0 (0x00007f539c7af000)
	libffi.so.6 => /usr/lib/x86_64-linux-gnu/libffi.so.6 (0x00007f539c5a7000)
	libglib-2.0.so.0 => /lib/x86_64-linux-gnu/libglib-2.0.so.0 (0x00007f539c29e000)
	libpthread.so.0 => /lib/x86_64-linux-gnu/libpthread.so.0 (0x00007f539c080000)
	librt.so.1 => /lib/x86_64-linux-gnu/librt.so.1 (0x00007f539be78000)
	libfreetype.so.6 => /usr/lib/x86_64-linux-gnu/libfreetype.so.6 (0x00007f539bbd4000)
	libm.so.6 => /lib/x86_64-linux-gnu/libm.so.6 (0x00007f539b8ce000)
	libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007f539b509000)
	libpng12.so.0 => /lib/x86_64-linux-gnu/libpng12.so.0 (0x00007f539b2e2000)
	libxcb-shm.so.0 => /usr/lib/x86_64-linux-gnu/libxcb-shm.so.0 (0x00007f539b0df000)
	libxcb-render.so.0 => /usr/lib/x86_64-linux-gnu/libxcb-render.so.0 (0x00007f539aed6000)
	libxcb.so.1 => /usr/lib/x86_64-linux-gnu/libxcb.so.1 (0x00007f539acb6000)
	/lib64/ld-linux-x86-64.so.2 (0x00007f539fa85000)
	libgraphite2.so.3 => /usr/lib/x86_64-linux-gnu/libgraphite2.so.3 (0x00007f539aa90000)
	libgmodule-2.0.so.0 => /usr/lib/x86_64-linux-gnu/libgmodule-2.0.so.0 (0x00007f539a88b000)
	libthai.so.0 => /usr/lib/x86_64-linux-gnu/libthai.so.0 (0x00007f539a682000)
	libexpat.so.1 => /lib/x86_64-linux-gnu/libexpat.so.1 (0x00007f539a458000)
	liblzma.so.5 => /lib/x86_64-linux-gnu/liblzma.so.5 (0x00007f539a235000)
	libpcre.so.3 => /lib/x86_64-linux-gnu/libpcre.so.3 (0x00007f5399ff7000)
	libXau.so.6 => /usr/lib/x86_64-linux-gnu/libXau.so.6 (0x00007f5399df2000)
	libXdmcp.so.6 => /usr/lib/x86_64-linux-gnu/libXdmcp.so.6 (0x00007f5399bec000)
	libdatrie.so.1 => /usr/lib/x86_64-linux-gnu/libdatrie.so.1 (0x00007f53999e5000)
```
于是安装libpng16，在[这里](https://sourceforge.net/projects/libpng/?source=directory)下载，然后安装，
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