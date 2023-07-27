from __future__ import annotations
__all__ = ["JSON", "JSON解码器", "JSON解码失败", "不可重写的函数的装饰器", "任意", "值不合法", "值的类型不合法",
           "假", "元组", "列表", "协议", "可调用", "可迭代", "可选", "子进程", "字典", "字符串", "字节串", "字节数组",
           "字面", "字面别名", "布尔值", "常量", "异常", "打印", "打开", "支持的索引", "整数", "文本输入输出包装器", "无",
           "最大值", "最小值", "检查对象是否是类的实例", "模块", "永不使用", "永不返回", "泛型别名", "浮点数", "真",
           "禁果", "类型", "类方法", "联合", "输入", "输入输出", "重载函数的装饰器", "静态方法", "正则", "对象", "枚举", "线程",
           "全部为真", "任意为真", "长度", "异常基类", "垃圾回收", "异常回溯", "时间", "系统", "属性装饰器", "平台"]






真 = True
假 = False
无 = None
from builtins import (
    type as 类型,
    BaseException as 异常基类, Exception as 异常, TypeError as 值的类型不合法, ValueError as 值不合法,
    classmethod as 类方法, staticmethod as 静态方法,
)
from typing import (
    Optional as 可选, Union as 联合, Callable as 可调用, Iterable as 可迭代,
    Never as 永不使用, NoReturn as 永不返回, Literal as 字面, Final as 常量, final as 不可重写的函数的装饰器,
    Protocol as 协议, SupportsIndex as 支持的索引, Any as 任意, overload as 重载函数的装饰器,
    _LiteralGenericAlias as 字面别名
)
from types import (GenericAlias as 泛型别名, ModuleType as 模块)
from json import JSONDecodeError as JSON解码失败, JSONDecoder as JSON解码器
from io import TextIOWrapper
from typing import BinaryIO, IO
from re import RegexFlag as 正则表达式标志
from enum import Enum, IntFlag
import subprocess
import traceback
import forbiddenfruit
import json
import re
import enum
import gc
import threading, _thread
import time
import sys
import platform





def __patchable_builtin(类):
    if isinstance(类, 模块):
        引用列表 = forbiddenfruit.gc.get_referents(类)
    else:
        try:
            getattr(类, "__name__")
            引用列表 = forbiddenfruit.gc.get_referents(类.__dict__)
        except AttributeError:
            引用列表 = forbiddenfruit.gc.get_referents(类.__class__.__dict__)
    if 类 is time:
        引用列表.remove(time.struct_time)
    assert len(引用列表) == 1
    return 引用列表[0]
forbiddenfruit.patchable_builtin = __patchable_builtin ; del __patchable_builtin

class 禁果:
    def __init__(当前对象: 禁果) -> 永不使用:
        raise 值的类型不合法('"模块" 对象不可调用.')
    @静态方法
    def 诅咒(类: 联合[模块, 类型], 属性: 任意, 值: 任意, 隐藏于目录: 布尔值 = 假):
        try:
            return forbiddenfruit.curse(类, 属性, 值, 隐藏于目录)
        except OSError:
            pass





class 字符串(str):
    def 开头是否为(
            当前对象: 字符串, __前缀: 联合[字符串, 元组[字符串, ...]], __起始索引: 可选[支持的索引] = 无, __终止索引: 可选[支持的索引] = 无
        ) -> 布尔值:
        return 当前对象.startswith(__前缀, __起始索引, __终止索引)
    def 末尾是否为(
            当前对象: 字符串, __后缀: 联合[字符串, 元组[字符串, ...]], __起始索引: 可选[支持的索引] = 无, __终止索引: 可选[支持的索引] = 无
        ) -> 布尔值:
        return 当前对象.endswith(__后缀, __起始索引, __终止索引)
    def 替换(
            当前对象: 字符串, __旧字符串: 字符串, __新字符串: 字符串, __最大替换次数: 支持的索引 = -1
        ) -> 字符串:
        return 当前对象.replace(__旧字符串, __新字符串, __最大替换次数)
class 字节串(bytes): pass
class 布尔值: pass
class 整数(int): pass
class 浮点数(float): pass
class 列表(list):
    def 追加(当前对象: 列表, __对象: 任意) -> 无:
        return 当前对象.append(__对象)
    def 移除(当前对象: 列表, __对象: 任意) -> 无:
        return 当前对象.remove(__对象)
class 字典(dict):
    def 键(当前对象: 字典) -> 可迭代[任意]:
        return 当前对象.keys()
    def 值(当前对象: 字典) -> 可迭代[任意]:
        return 当前对象.values()
    def 键值对(当前对象: 字典) -> 可迭代[元组[任意, 任意]]:
        return 当前对象.items()
class 元组(tuple): pass
class 字节数组(bytearray): pass
禁果.诅咒(str, "开头是否为", 字符串.开头是否为)
禁果.诅咒(str, "末尾是否为", 字符串.末尾是否为)
禁果.诅咒(str, "替换", 字符串.替换)
禁果.诅咒(list, "追加", 列表.追加)
禁果.诅咒(list, "移除", 列表.移除)
禁果.诅咒(dict, "键", 字典.键)
禁果.诅咒(dict, "值", 字典.值)
禁果.诅咒(dict, "键值对", 字典.键值对)
from builtins import (
    str as 字符串, int as 整数, float as 浮点数, bool as 布尔值,
    list as 列表, dict as 字典, tuple as 元组, bytes as 字节串, bytearray as 字节数组,
    property as 属性装饰器,
    max as 最大值, min as 最小值, print as 打印, input as 输入,
    isinstance as 检查对象是否是类的实例, all as 全部为真, any as 任意为真, len as 长度
)





class 打开:
    def __init__(
        当前对象: 打开,
        文件路径: 字符串, 模式: 字面["r", "w"],
        缓冲大小: 整数 = -1, 编码: 可选[字符串] = 无, 错误处理模式: 可选[字面["strict", "ignore"]] = 无,
        换行符: 可选[字符串] = 无, 是否在文件对象关闭时关闭文件描述符: 布尔值 = True, 文件自定义打开函数: 可调用[[字符串, 整数], 整数] = 无
        ):
        当前对象.文件路径 = 文件路径
        当前对象.模式 = 模式
        当前对象.缓冲大小 = 缓冲大小
        当前对象.编码 = 编码
        当前对象.错误处理模式 = 错误处理模式
        当前对象.换行符 = 换行符
        当前对象.是否在文件对象关闭时关闭文件描述符 = 是否在文件对象关闭时关闭文件描述符
        当前对象.文件自定义打开函数 = 文件自定义打开函数
    def __enter__(当前对象: 打开):
        当前对象.文件 = open(
            当前对象.文件路径, 当前对象.模式,
            当前对象.缓冲大小, 当前对象.编码, 当前对象.错误处理模式,
            当前对象.换行符, 当前对象.是否在文件对象关闭时关闭文件描述符, 当前对象.文件自定义打开函数
        )
        return 当前对象
    def __exit__(当前对象: 打开, 异常类型, 异常值, 异常回溯):
        当前对象.文件.close()
    def 读取(当前对象: 打开, __读取长度: 可选[整数] = None) -> 字符串:
        return 当前对象.文件.read(__读取长度)
    def 写入(当前对象: 打开, __文本: 可选[字符串]) -> 字符串:
        return 当前对象.文件.write(__文本)
    def 关闭(当前对象: 打开) -> None:
        当前对象.文件.close()



class JSON:
    def __init__(当前对象: JSON) -> 永不使用:
        raise 值的类型不合法('"模块" 对象不可调用.')
    @静态方法
    def 加载(
        对象: 联合[字符串, 字节串, 字节数组],
        *,
        JSON解码器: 可选[类型[JSON解码器]] = None,
        对象自定义解码函数: 可选[可调用[[字典[任意, 任意]], 任意]] = None,
        浮点数自定义解码函数: 可选[可调用[[字符串], 任意]] = None,
        整数自定义解码函数: 可选[可调用[[字符串], 任意]] = None,
        常量自定义解码函数: 可选[可调用[[字符串], 任意]] = None,
        对象自定义解码键值函数: 可选[可调用[[可迭代[元组[任意, 任意]]], 任意]] = None,
        **关键字参数
        ) -> 任意:
        return json.loads(对象, cls = JSON解码器, object_hook = 对象自定义解码函数, parse_float = 浮点数自定义解码函数, parse_int = 整数自定义解码函数, parse_constant = 常量自定义解码函数, object_pairs_hook = 对象自定义解码键值函数, **关键字参数)
禁果.诅咒(json, "加载", JSON.加载)
import json as JSON



class 输入输出(IO):
    def 读取一行(当前对象: 输入输出, 读取长度: 整数 = -1) -> 联合[字节串, 字符串]:
        return 当前对象.readline(读取长度)
class 文本输入输出包装器(TextIOWrapper):
    def 读取一行(当前对象: 文本输入输出包装器, 读取长度: 整数 = -1) -> 字符串:
        return 当前对象.readline(读取长度)
禁果.诅咒(IO, "读取一行", 输入输出.读取一行)
禁果.诅咒(TextIOWrapper, "读取一行", 文本输入输出包装器.读取一行)
from io import TextIOWrapper as 文本输入输出包装器
from typing import IO as 输入输出






class 正则:
    @静态方法
    def 替换(
        匹配规则: 字符串,
        替换字符: 联合[字符串, 可调用[[字符串], 字符串]],
        被替换字符串: 字符串,
        最大替换次数: 整数 = 0,
        匹配行为标志: 联合[整数, 正则表达式标志] = 0
    ) -> 字符串:
        return re.sub(pattern = 匹配规则, repl = 替换字符, string = 被替换字符串, count = 最大替换次数, flags = 匹配行为标志)
禁果.诅咒(re, "替换", 正则.替换)
import re as 正则


# for 键, 值 in list(__builtins__.items()):
#     if 键 not in ["len", "open", "reversed", "list"]:
#         del __builtins__[键]


class 对象(object):
    def __init__(当前对象, *位置参数, **关键字参数) -> 无:
        return 当前对象.__初始化__(*位置参数, **关键字参数)
    def __str__(当前对象, *位置参数, **关键字参数) -> 字符串:
        return 当前对象.__字符串化__(*位置参数, **关键字参数)



class 枚举:
    class 枚举基类(Enum):
        pass
    class 整数标志(IntFlag):
        pass
    @静态方法
    def 全局枚举(类, 是否使用字符串类型: 布尔值 = 假):
        return enum.global_enum(cls = 类, update_str = 是否使用字符串类型)
    @静态方法
    def _简单枚举(枚举类型 = 枚举基类, *, 枚举值边界: 可选[整数] = 无, 枚举值是否使用参数: 可选[布尔值] = 无):
        return enum._simple_enum(etype = 枚举类型, boundary = 枚举值边界, use_args = 枚举值是否使用参数)
禁果.诅咒(enum, "全局枚举", 枚举.全局枚举)
禁果.诅咒(enum, "_简单枚举", 枚举._简单枚举)
禁果.诅咒(enum, "枚举基类", enum.Enum)
禁果.诅咒(enum, "整数标志", enum.IntFlag)
import enum as 枚举


class 垃圾回收:
    @静态方法
    def 回收(对象代数: 整数 = 2) -> 字符串:
        return gc.collect(generation = 对象代数)
禁果.诅咒(gc, "回收", 垃圾回收.回收)
import gc as 垃圾回收



class 异常回溯:
    @静态方法
    def 格式化异常(最大堆栈帧: 可选[整数] = 无, 是否包括异常链: 布尔值 = 真) -> 字符串:
        return traceback.format_exc(limit = 最大堆栈帧, chain = 是否包括异常链)
禁果.诅咒(traceback, "格式化异常", 异常回溯.格式化异常)
import traceback as 异常回溯



class 时间:
    @静态方法
    def 暂停执行(秒数: 联合[整数, 浮点数]) -> 无:
        return time.sleep(秒数)
    @静态方法
    def 性能计时器() -> 浮点数:
        return time.perf_counter()
禁果.诅咒(time, "暂停执行", 时间.暂停执行)
禁果.诅咒(time, "性能计时器", 时间.性能计时器)
import time as 时间



class 系统:
    @静态方法
    def 退出(__状态码: 可选[联合[字符串, 整数]] = 无) -> 永不返回:
        return sys.exit(__状态码)
禁果.诅咒(sys, "退出", 系统.退出)
import sys as 系统



class 平台:
    @静态方法
    def 操作系统名称() -> 字符串:
        return platform.system()
    @静态方法
    def 架构信息(
        可执行文件: 字符串 = sys.executable,
        位架构默认值: 字符串 = "",
        链接格式默认值: 字符串 = ""
    ) -> 元组[字符串, 字符串]:
        位架构, 链接格式 = platform.architecture(executable = 可执行文件, bits = 位架构默认值, linkage = 链接格式默认值)
        if 位架构.末尾是否为("bit"):
            位架构 = 位架构.替换("bit", "位")
        return (位架构, 链接格式)
禁果.诅咒(platform, "操作系统名称", 平台.操作系统名称)
禁果.诅咒(platform, "架构信息", 平台.架构信息)
import platform as 平台



class 线程:
    class 锁:
        def 获取(当前对象: threading.Lock, 是否阻塞: 可选[布尔值] = 真, 超时秒数: 联合[整数, 浮点数] = -1) -> 布尔值:
            return 当前对象.acquire(blocking = 是否阻塞, timeout = 超时秒数)
        def 释放(当前对象: threading.Lock) -> 无:
            return 当前对象.release()
        def 是否锁定(当前对象: threading.Lock) -> 布尔值:
            return 当前对象.locked()
    禁果.诅咒(_thread.LockType, "获取", 锁.获取)
    禁果.诅咒(_thread.LockType, "释放", 锁.释放)
    禁果.诅咒(_thread.LockType, "是否锁定", 锁.是否锁定)
    锁 = threading.Lock
    class 线程(threading.Thread):
        def __init__(
                当前对象: 线程,
                线程组: 无 = 无,
                函数对象: 可选[可调用] = 无,
                线程名称: 可选[字符串] = 无,
                位置参数: 元组[任意, ...] = (),
                关键字参数: 可选[字典[字符串, 任意]] = 无,
                *,
                是否为守护线程: 可选[布尔值] = 无,
            ) -> 无:
            threading.Thread.__init__(当前对象, 线程组, 函数对象, 线程名称, 位置参数, 关键字参数, daemon = 是否为守护线程)
        def 阻塞(当前对象: 线程, 超时秒数: 可选[联合[整数, 浮点数]] = 无):
            return 当前对象.join(timeout = 超时秒数)
        def 是否在运行(当前对象: 线程):
            return 当前对象.is_alive()
        def 启动(当前对象: 线程):
            return 当前对象.start()
        def 运行(当前对象: 线程):
            return
        def run(当前对象: 线程):
            return 当前对象.运行()
        @属性装饰器
        def 函数对象(当前对象: 线程):
            return 当前对象._target
        @属性装饰器
        def 线程ID(当前对象: 线程):
            return 当前对象._ident
        @属性装饰器
        def 位置参数(当前对象: 线程):
            return 当前对象._args
        @属性装饰器
        def 关键字参数(当前对象: 线程):
            return 当前对象._kwargs
        @属性装饰器
        def 线程名称(当前对象: 线程):
            return 当前对象._name
禁果.诅咒(threading, "锁", 线程.锁)
禁果.诅咒(threading, "线程", 线程.线程)
import threading as 线程




class 子进程:
    管道 = subprocess.PIPE
    标准输出 = subprocess.STDOUT
    def __init__(当前对象) -> 永不使用:
        raise 值的类型不合法('"模块" 对象不可调用.')
    class 启动进程(subprocess.Popen):
        def __init__(
            当前对象: 子进程.启动进程,
            启动参数: 列表[任意],
            缓冲区大小: 整数 = -1,
            程序路径: 可选[字符串] = 无,
            标准输入: 可选[任意] = 无,
            标准输出: 可选[任意] = 无,
            标准错误输出: 可选[任意] = 无,
            预执行函数: 可选[可调用] = 无,
            是否关闭父进程打开的文件描述符: 布尔值 = 真,
            是否使用控制台启动程序: 布尔值 = 假,
            工作目录: 可选[字符串] = 无,
            环境变量: 可选[字典[字符串, 任意]] = 无,
            是否使用通用换行符: 可选[布尔值] = 无,
            启动信息_仅Windows: 可选[任意] = 无,
            创建标志: 整数 = 0,
            # restore_signals: bool = True,
            # start_new_session: bool = False,
            # pass_fds: Collection[int] = (),
            *,
            # user: str | int | None = None,
            # group: str | int | None = None,
            # extra_groups: Iterable[str | int] | None = None,
            编码: 可选[字符串] = 无,
            输出解码错误处理模式: 可选[字面["strict", "ignore", "replace"]] = 无,
            是否以文本模式返回输出: 可选[布尔值] = 无,
            # umask: int = -1,
            # pipesize: int = -1,
            # process_group: int | None = None
        ):
            super().__init__(
                args = 启动参数, bufsize = 缓冲区大小, executable = 程序路径,
                stdin = 标准输入, stdout = 标准输出, stderr = 标准错误输出, preexec_fn = 预执行函数,
                close_fds = 是否关闭父进程打开的文件描述符, shell = 是否使用控制台启动程序, cwd = 工作目录,
                env = 环境变量, universal_newlines = 是否使用通用换行符, startupinfo = 启动信息_仅Windows,
                creationflags = 创建标志, encoding = 编码, errors = 输出解码错误处理模式, text = 是否以文本模式返回输出
            )
        def 终止(当前对象: 子进程.启动进程):
            return 当前对象.terminate()
        def 是否终止(当前对象: 子进程.启动进程):
            return 当前对象.poll()
        @属性装饰器
        def 标准输出(当前对象: 子进程.启动进程) -> 输入输出:
            return 当前对象.stdout