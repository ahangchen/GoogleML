# 什么造就好的Feature
> Feature越好，分类器也就越好

- 好的feature能有力地说明两个类别的不同
> 简化问题
- 单个feature往往不完美，所以需要多个feature
- 假如由人来做分类器，会需要什么信息？（找好的feature）
- 对于一个feature，如果不同的label中，这个feature的值分布越均匀，则这个feature的分类作用越弱
> 在同一种眼睛颜色中，不同狗的数量差不多，说明眼的颜色的分类作用弱，这样的feature会降低分类器的准确性
- 好的feature应该是相互独立的，能够提供更多有效信息，
- 每个feature在分类器中都占一定的重要性，而如果feature间不独立，重要性的比重也会与原本的计划有偏差
- feature应当预处理地尽可能与结果直接相关
- 有好的feature还不够，还要有好的feature之间的好的组合

##总结
- Informative 
- Independent
- Simple
