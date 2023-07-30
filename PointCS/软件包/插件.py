from __future__ import annotations
from .蟒蛇 import *
from .可停止线程 import *

class 点命令异常(异常): pass

@枚举._简单枚举(枚举.整数标志)
class 速建者运行状态:
    未启动 = 0
    正在启动 = 1
    正在运行 = 2

作者: 常量[字符串] = "wangzm5773"
操作系统名称 = 平台.操作系统名称()
位架构 = 平台.架构信息()[0]
if 操作系统名称 not in ["Windows", "Linux"]:
    raise 点命令异常(f"不支持的操作系统 {操作系统名称}")
if 位架构 not in ["64位"]:
    raise 点命令异常(f"不支持的位架构 {位架构}")





def 删除控制台样式字符(文本: 字符串) -> 字符串:
    return 正则.替换(r"\x1b\[[0-9;]*[m|K]", "", 文本)


def 对象是否符合泛型(对象: 任意, 泛型: 联合[泛型别名, 字面别名]) -> 布尔值:
    if 对象是否是类的实例(泛型, 字面别名):
        return 对象 in 泛型.__args__
    if not 对象是否是类的实例(泛型, 泛型别名):
        raise 值的类型不合法(f"检查对象是否符合泛型异常: {类型(泛型)} 不是泛型.")
    泛型的类型 = 泛型.__origin__
    if not 对象是否是类的实例(对象, 泛型的类型):
        return 假
    if 泛型的类型 is 列表:
        元素应该符合的类型 = 泛型.__args__[0]
        检查元素的函数 = 对象是否符合泛型 if 对象是否是类的实例(元素应该符合的类型, (泛型别名, 字面别名)) else 对象是否是类的实例
        if not 全部为真(检查元素的函数(元素, 元素应该符合的类型) for 元素 in 对象):
            return 假
    elif 泛型的类型 is 字典:
        键应该符合的类型, 值应该符合的类型 = 泛型.__args__
        检查键的函数 = 对象是否符合泛型 if 对象是否是类的实例(键应该符合的类型, (泛型别名, 字面别名)) else 对象是否是类的实例
        检查值的函数 = 对象是否符合泛型 if 对象是否是类的实例(值应该符合的类型, (泛型别名, 字面别名)) else 对象是否是类的实例
        if not 全部为真((检查键的函数(键, 键应该符合的类型) and 检查值的函数(值, 值应该符合的类型)) for 键, 值 in 对象.items()):
            return 假
    elif 泛型的类型 is 元组:
        if 长度(对象) != 长度(泛型.__args__):
            return 假
        for 元素, 元素应该符合的类型 in zip(对象, 泛型.__args__):
            检查元素的函数 = 对象是否符合泛型 if 对象是否是类的实例(元素应该符合的类型, (泛型别名, 字面别名)) else 对象是否是类的实例
            if not 检查元素的函数(元素, 元素应该符合的类型):
                return 假
    else:
        raise 值不合法("检查对象是否符合泛型异常: 不支持的泛型.")
    return 真


def 退出() -> 永不返回:
    [租赁服_.停止() for 租赁服_ in 列表(租赁服映射.值())]
    [线程_.停止() for 线程_ in 可停止线程列表[:]]
    系统.退出()


def 暂停执行并检测(总秒数: 联合[整数, 浮点数], 检测间隔秒数: 联合[整数, 浮点数] = 0.1, 检测函数: 可调用[[联合[整数, 浮点数], 联合[整数, 浮点数], 联合[整数, 浮点数]], 布尔值] = (lambda __ = 无, ___ = 无, ____ = 无: 假)) -> 布尔值:
    开始时刻 = 时间.性能计时器()
    if 检测间隔秒数 >= 总秒数:
        raise 值不合法("暂停执行并检测异常: 参数 检测间隔秒数 应该小于 参数 总秒数.")
    while (已过时间 := (时间.性能计时器() -开始时刻)) < 总秒数:
        剩余时间 = 总秒数 -已过时间
        if 检测函数(总秒数, 已过时间, 剩余时间):
            return 真
        时间.暂停执行(检测间隔秒数 if (剩余时间 > 检测间隔秒数) else 剩余时间)
    return 假


def 端口是否被占用(端口: 整数, 协议: 字面["传输控制协议", "用户数据报协议"]) -> 布尔值:
    if 协议 == "传输控制协议":
        传输类型 = 套接字.传输类型_流式
    elif 协议 == "用户数据报协议":
        传输类型 = 套接字.传输类型_数据报
        raise 功能未实现
    else:
        raise 值不合法("检查端口是否被占用异常: 参数 协议 应该是 传输控制协议 或 用户数据报协议.")

    with 套接字.套接字(套接字.地址族_互联网协议版本四, 传输类型) as 套接字对象:
        套接字对象.设置超时时间(秒数 = 0.1)
        连接结果 = 套接字对象.连接_不引发异常(("localhost", 端口))
        套接字对象.关闭()
    if 连接结果 == 0:
        return 真
    return 假





租赁服操作锁 = 线程.锁()
速建者启动锁 = 线程.锁()
租赁服映射: 字典 = {}
class 速建者异常(异常): pass
class 速建者启动时异常(速建者异常): pass
class 速建者启动过于频繁异常(速建者启动时异常): pass
class 速建者租赁服未授权异常(速建者启动时异常): pass
class 速建者租赁服未找到异常(速建者启动时异常): pass
class 速建者租赁服连接异常(速建者启动时异常): pass
class 速建者官方服务器连接异常(速建者启动时异常): pass
class 速建者端口监听异常(速建者启动时异常): pass
class 速建者运行时异常(速建者异常): pass
class 租赁服异常(异常): pass
class 租赁服对象创建异常(租赁服异常): pass
class 租赁服(对象):
    def __字符串化__(当前对象: 租赁服) -> 字符串:
        return f"租赁服_{当前对象.租赁服号}"


    def __初始化__(当前对象: 租赁服, 租赁服号: 字符串, 租赁服密码: 可选[字符串] = 无) -> 无:
        with 租赁服操作锁:
            if 租赁服号 in 租赁服映射:
                raise 租赁服对象创建异常("不能重复创建相同的租赁服对象.")
            当前对象.租赁服号 = 租赁服号
            当前对象.租赁服密码 = 租赁服密码 if 租赁服密码 is not 无 else 作者
            当前对象.速建者连接标识 = 无
            当前对象.速建者运行状态 = 速建者运行状态.未启动
            当前对象._设置速建者监听端口()
            当前对象._启动速建者()
            可停止线程(函数对象 = 当前对象._循环启动速建者, 线程名称 = f"{当前对象}_循环启动速建者", 数据 = {"": ""})
            租赁服映射[当前对象.租赁服号] = 当前对象


    def _设置速建者监听端口(当前对象: 租赁服) -> 无:
        端口 = 5700
        while 端口是否被占用(端口 = 端口, 协议 = "传输控制协议"):
            端口 += 10
        当前对象.速建者监听端口 = 端口


    def _启动速建者(当前对象: 租赁服) -> 无:
        with 速建者启动锁:
            当前对象.速建者进程 = 子进程.启动进程(
                程序路径 = f"./程序/速建者/{操作系统名称}_{位架构}.可执行文件",
                工作目录 = "./程序/速建者/",
                启动参数 = [
                    "--token", "./程序/速建者/令牌",
                    "--code", 当前对象.租赁服号,
                    "--password", 当前对象.租赁服密码,
                    "--listen-external", f"0.0.0.0:{当前对象.速建者监听端口}",
                    "--no-update-check", "--no-readline",
                    "--debug" if (当前对象.租赁服号 == "调试") else ""
                ],
                编码 = "UTF-8", 标准输出 = 子进程.管道, 标准错误输出 = 子进程.管道, 是否使用通用换行符 = 真
            )
            当前对象.速建者运行状态 = 速建者运行状态.正在启动
            当前对象._读取速建者输出("成功验证 CheckNum." if (当前对象.租赁服号 != "调试") else "成功连接到服务器")
            当前对象.速建者运行状态 = 速建者运行状态.正在运行
            可停止线程(函数对象 = 当前对象._读取速建者输出, 线程名称 = f"{当前对象}_读取速建者输出", 数据 = {"": ""})


    def _循环启动速建者(当前对象: 租赁服, 可停止线程对象: 可停止线程) -> 无:
        线程是否正在停止 = (lambda __ = 无, ___ = 无, ____ = 无: 可停止线程对象.正在停止)
        while not 线程是否正在停止():
            if 当前对象.速建者运行状态 != 速建者运行状态.未启动:
                时间.暂停执行(秒数 = 1)
                continue
            try:
                暂停执行并检测(总秒数 = 5, 检测间隔秒数 = 1, 检测函数 = 线程是否正在停止)
                当前对象._启动速建者()
            except 速建者启动时异常 as 异常:
                打印(字符串(异常))
                暂停执行并检测(总秒数 = 55, 检测间隔秒数 = 1, 检测函数 = 线程是否正在停止)


    def 重启速建者(当前对象: 租赁服) -> 无:
        if 当前对象.速建者运行状态 != 速建者运行状态.正在运行:
            raise 租赁服异常("重启速建者异常: 速建者不在运行.")
        当前对象._终止速建者()


    def _终止速建者(当前对象: 租赁服) -> 无:
        当前对象.速建者运行状态 = 速建者运行状态.未启动
        当前对象._关闭速建者连接()
        当前对象.速建者进程.终止()


    def _连接速建者(当前对象: 租赁服) -> 无:
        当前对象.速建者连接标识 = 速建者动态链接库.连接速建者(f"localhost:{当前对象.速建者监听端口}")


    def _关闭速建者连接(当前对象: 租赁服) -> 无:
        if 当前对象.速建者连接标识 is not 无:
            速建者动态链接库.关闭速建者连接(当前对象.速建者连接标识)


    def 停止(当前对象: 租赁服) -> 无:
        with 租赁服操作锁:
            当前对象._终止速建者()
            [线程.停止() for 线程 in 可停止线程列表[:] if 线程.线程名称.开头是否为(字符串(当前对象))]
            del 租赁服映射[当前对象.租赁服号]


    def _读取速建者输出(当前对象: 租赁服, 读到此字符串时退出: 可选[字符串] = 无, 崩溃重启: 布尔值 = 假, 可停止线程对象: 可选[可停止线程] = 无) -> 无:
        线程是否正在停止 = (lambda __ = 无, ___ = 无, ____ = 无: (假 if (可停止线程对象 is None) else 可停止线程对象.正在停止))
        错误信息 = 字符串("")
        异常类型 = 速建者启动时异常
        while not 线程是否正在停止():
            if (速建者进程返回码 := 当前对象.速建者进程.是否终止()) is not 无:
                当前对象.速建者运行状态 = 速建者运行状态.未启动
                raise 异常类型("速建者退出." if (not 错误信息) else 错误信息)

            原始输出 = 当前对象.速建者进程.标准输出.读取一行()
            去色输出 = 删除控制台样式字符(原始输出)
            打印(原始输出, end = "")

            if 去色输出.开头是否为(" ERROR  "):
                去色输出 = 去色输出.替换(" ERROR  ", "", 1)

                if 去色输出.开头是否为("按ENTER（回车）键来退出程序。"):
                    错误信息 = 错误信息.末尾去除字符("\n")
                    当前对象._终止速建者()
                    raise 异常类型(错误信息)

                if (去色输出 not in ["FastBuilder Phoenix 运行过程遇到问题\n", "Stack dump 于上方显示。错误为：\n"]) \
                    and (去色输出 not in 错误信息):
                    错误信息 += 去色输出
                if 去色输出.开头是否为("[RATE LIMIT]"):
                    异常类型 = 速建者启动过于频繁异常
                if 去色输出.开头是否为("对应租赁服号尚未授权"):
                    异常类型 = 速建者租赁服未授权异常
                if 去色输出.开头是否为("租赁服未找到"):
                    异常类型 = 速建者租赁服未找到异常
                if 去色输出.开头是否为("dial "):
                    异常类型 = 速建者租赁服连接异常
                if 去色输出.开头是否为("Failed to contact with API"):
                    异常类型 = 速建者官方服务器连接异常

            if 去色输出.开头是否为("Failed to listen on address"):
                异常类型 = 速建者端口监听异常
                错误信息 = 去色输出.末尾去除字符("\n")
                当前对象._终止速建者()
                raise 异常类型(去色输出)

            if 去色输出.开头是否为("Listening for external connection"):
                当前对象._连接速建者()

            if 去色输出.开头是否为("成功连接到服务器。"):
                异常类型 = 速建者运行时异常

            if 读到此字符串时退出 and 去色输出.开头是否为(读到此字符串时退出):
                return


from . import 速建者动态链接库
from 软件包.速建者动态链接库 import 速建者动态链接库异常, 速建者解码数据包异常
租赁服("调试").停止()
