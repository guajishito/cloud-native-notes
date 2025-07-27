# Day 6 学习笔记

## Python 部分

### json概念:
是一种轻量级的数据交互格式,采用完全独立于编程语言的文本格式来存储和表示数据(就是字符串)Python语言使用JSON有很大优势，因为:JSON无非就是一个单独的字典或一个内部元素都是字典的列表，所以JSON可以直接和Python的字典或列表进行无缝转换

### json格式数据转化
**转化**
1. 把python数据转化为了json数据:`json.dumps(data)`
json_str = json.dumps(data)

如果有中文可以带上:ensure ascii=False：
`json.dumps(data,ensure_ascii=False)`  #参数来确保中文正常转换

2. 把josn数据转化为了 python列表或字典:`json.loads(data)`
l = json.loads(data)

### pyecharts概念
1. pyecharts模块中有很多的配置选项,常用到三个类别的选项:
全局配置选项
系列配置选项
2. 全局配置项能做什么?
配置图表的标题
配置图例
配置鼠标移动效果
配置工具栏
等整体配置项

### 案例
1. 
```json
#json数据的格式可以是:
{"name":"admin","age":18}
#也可以是:
[{"name":"admin","age":18},{"name":"root","age":16},{"name":"张三","age":20}]
```

2. 
```python
#导包，导入Line功能构建折线图对象
from pyecharts.charts import Line
#得到折线图对象
line = Line()
# 添加x轴数据
line.add_xaxis(["中国"，“美国”，“英国”])
# 添加y轴数据
line.add_yaxis('GDp"，[30，20 ,10])
#设置全局配置项set_global_opts来设置Line.set_global_opts(
line.set_global_opts(
    title_opts=TitleOpts(title="GDP展示", pos_left="center", pos_bottom="1%"),           #配置图表的标题
    legend_opts=LegendOpts(is_show=True),
    toolbox_opts=ToolboxOpts(is_show=True),                                              #配置工具栏
    visualmap_opts=VisualMapOpts(is_show=True)
)
#生成图表
line.render()
```