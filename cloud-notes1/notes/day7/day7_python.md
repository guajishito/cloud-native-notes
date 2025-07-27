# Day 7 学习笔记

## Python 部分

### `Map`：地图可视化
```py
from pyecharts.charts import Map
map = Map()

#准备数据
data = [
    ("北京市", 99),
    ("上海市", 199),
    ("湖南省", 299),
    ("台湾省", 399),
    ("广东省", 499)
]
#添加数据
map.add("测试地图", data, "china")

map.render("全国疫情地图.html")
```

### `Bar`：柱状图
柱状图描述的是分类数据，回答的是每一个分类中「有多少?」这个问题，这是柱状图的主要特点
1. 通过`Bar()`构建一个柱状图对象
2. 和折线图一样，通过`add xaxis()`和`add yaxis()`添加x和y轴数据
3. 通过柱状图对象的:`reversal axis()`，反转x和y轴
4. 通过`label opts=LabelOpts(position="right")`设置数值标签在右侧显示

### `Timeline`:时间线柱状图
1. `Timeline()`-时间线
```py
柱状图很难动态的描述个趋势性的数据，这里pyecharts为我们提供了一种解决方案-[时间线]
如果说一个Bar、Line对象是一张图表的话，时间线就是创建一个维的x轴，轴上每一个点就一个图表对象

from pyecharts.charts import Timeline
timeline = Timeline()
```
2. 自动播放
```py
#设置自动播放
timeline.add_schema(
    play_interval=1000,         #自动播放的时间间隔，单位毫秒
    is_timeline_show=True,      #是否在自动播放的时候。显示时间线
    is_auto_play=True,          #是否自动播放
    is_loop_play=True           #是否循环自动播放
)
```
3. 设置主题
```py
from pyecharts.globals import ThemeType
#创建时间线对象
timeline = Timeline({"theme": ThemeType.LIGHT})
```

### [拓展]列表排序
`列表.sort(key=选择排序依据的函数,reverse=True|False)`

1. 参数key：是要求传入一个函数，表示将列表的每一个元素都传入函数中，返回排序的依据
2. 参数reverse：是否反转排序结果，True表示降序，False表示升序




