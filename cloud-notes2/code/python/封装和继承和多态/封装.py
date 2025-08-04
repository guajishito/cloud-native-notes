"""
演示面向对象封装思想中私有成员的使用
"""

#定义一个类，内含私有成员变量和私有成员方法
class Phone:

    __current_voltage = 0.5        #当前手机运行电压

    def __keep_single_core(self):
        print("让CPU以单核模式运行")

    def call_bt_5g(self):
        if self.__current_voltage >= 1:
            print("5g通话已开启")
        else:
            self.__keep_single_core()
            print("电量不足，无法使用5g通话，并已设置为单核模式运行进行省点。")


phone = Phone()
#phone.__keep_single_core()             #报错
#print(phone.__current_voltage)         #报错

phone.call_bt_5g()
