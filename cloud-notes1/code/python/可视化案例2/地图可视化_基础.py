
from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts, TitleOpts

#准备地图对象
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

#设置全局选项
map.set_global_opts(
    title_opts=TitleOpts(title="全国疫情地图"),
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min": 1, "max": 9, "label": "1-9", "color": "#CCFFFF"},
            {"min": 10, "max": 99, "label": "10-99", "color": "FF6666"},
            {"min": 100, "max": 499, "label": "99-499", "color": "#CCCFFF"}
        ]
    )
)

#绘图
map.render("全国疫情地图.html")
