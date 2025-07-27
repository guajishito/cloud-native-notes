
def str_reverse(s):
    """
    功能是将字符串完成反转
    :param s: 将被反转的函数
    :return:反转后发函数
    """
    reversed_str = s[::-1]
    return reversed_str

def substr(s, x, y):
    """
    功能是按照给定的下标完成给定字符串的切片
    :param s:即将被切片的字符串
    :param x:切片的开始下标
    :param y:切片的结束下标
    :return:切片完成后的字符串
    """
    return_str = s[x:y]
    return return_str

if __name__ == '__main__':
    print(str_reverse("黑马程序员"))