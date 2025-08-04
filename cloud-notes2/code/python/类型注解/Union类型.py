"""
演示Union联合类型注解
"""
#使用Union类型，必须先导包
from typing import Union

my_list: list[Union[int, str]] = [1, 2, "itheima", "itcast"]
my_dict: dict[str, Union[str, int]] ={"name":"周杰轮", "age": 31}

def func(data: Union[int, str]) -> Union[int, str]:
    pass