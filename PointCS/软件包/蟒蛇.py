from __future__ import annotations
__all__ = ["JSON", "JSON解码器", "JSON解码失败", "不可重写的函数的装饰器", "任意", "值不合法", "值的类型不合法",
           "假", "元组", "列表", "协议", "可调用", "可迭代", "可选", "子进程", "字典", "字符串", "字节串", "字节数组",
           "字面", "字面别名", "布尔值", "常量", "异常", "打印", "打开", "支持的索引", "整数", "文本输入输出包装器", "无",
           "最大值", "最小值", "对象是否是类的实例", "模块", "永不使用", "永不返回", "泛型别名", "浮点数", "真",
           "禁果", "类型", "类方法", "联合", "输入", "输入输出", "重载函数的装饰器", "静态方法", "正则", "对象", "枚举", "线程",
           "全部为真", "任意为真", "长度", "异常基类", "垃圾回收", "异常回溯", "时间", "系统", "属性装饰器", "平台", "套接字",
           "功能未实现", "散列", "网络请求", "基底64", "统一资源定位符", "图像处理", "范围", "求和", "绝对值", "输入输出模块",
           "带索引迭代"]






真 = True
假 = False
无 = None
from builtins import (
    type as 类型,
    BaseException as 异常基类, Exception as 异常, TypeError as 值的类型不合法, ValueError as 值不合法,
    classmethod as 类方法, staticmethod as 静态方法, NotImplementedError as 功能未实现, range as 范围,
)
from typing import (
    Optional as 可选, Union as 联合, Callable as 可调用, Iterable as 可迭代,
    Never as 永不使用, NoReturn as 永不返回, Literal as 字面, Final as 常量, final as 不可重写的函数的装饰器,
    Protocol as 协议, SupportsIndex as 支持的索引, Any as 任意, overload as 重载函数的装饰器,
    _LiteralGenericAlias as 字面别名
)
from types import (GenericAlias as 泛型别名, ModuleType as 模块)
from json import (JSONDecodeError as JSON解码失败, JSONDecoder as JSON解码器)
import io
from io import TextIOWrapper
from typing import BinaryIO, IO
from re import RegexFlag as 正则表达式标志
from enum import Enum, IntFlag
import subprocess
import json
import re
import enum
import gc
import threading, _thread
import time
import sys
import platform
import socket
import hashlib
import traceback
import base64
import urllib.parse

import forbiddenfruit
import requests
import PIL.Image





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
    def 末尾去除字符(
            当前对象: 字符串, __字符: 可选[字符串] = 无
        ) -> 字符串:
        return 当前对象.rstrip(__字符)
    def 开头去除字符(
            当前对象: 字符串, __字符: 可选[字符串] = 无
        ) -> 字符串:
        return 当前对象.lstrip(__字符)
    def 两端去除字符(
            当前对象: 字符串, __字符: 可选[字符串] = 无
        ) -> 字符串:
        return 当前对象.strip(__字符)
    def 拆分(
            当前对象: 字符串, 分隔符: 可选[字符串] = 无, 最大拆分次数: 支持的索引 = -1
        ) -> 列表[字符串]:
        return 当前对象.split(sep = 分隔符, maxsplit = 最大拆分次数)
    def 编码(
            当前对象: 字符串, 编码: 字符串 = "UTF-8", 错误处理方式: 字符串 = "strict"
        ) -> 字节串:
        return 当前对象.encode(encoding = 编码, errors = 错误处理方式)
    def 是否为十进制整数(
            当前对象: 字符串
        ) -> 布尔值:
        return 当前对象.isdecimal()
    def 连接(
            当前对象: 字符串, __可迭代对象: 可迭代[字符串]
        ) -> 字符串:
        return 当前对象.join(__可迭代对象)
    def 大写英文字母小写化(
            当前对象: 字符串
        ) -> 字符串:
        return 当前对象.lower()
    def 小写英文字母大写化(
            当前对象: 字符串
        ) -> 字符串:
        return 当前对象.upper()
class 字节串(bytes):
    def 解码(
            当前对象: 字节串, 编码: 字符串 = "UTF-8", 错误处理方式: 字符串 = "strict"
        ) -> 字符串:
        return 当前对象.decode(encoding = 编码, errors = 错误处理方式)
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
禁果.诅咒(str, "末尾去除字符", 字符串.末尾去除字符)
禁果.诅咒(str, "开头去除字符", 字符串.开头去除字符)
禁果.诅咒(str, "两端去除字符", 字符串.两端去除字符)
禁果.诅咒(str, "拆分", 字符串.拆分)
禁果.诅咒(str, "编码", 字符串.编码)
禁果.诅咒(str, "是否为十进制整数", 字符串.是否为十进制整数)
禁果.诅咒(str, "连接", 字符串.连接)
禁果.诅咒(str, "大写英文字母小写化", 字符串.大写英文字母小写化)
禁果.诅咒(str, "小写英文字母大写化", 字符串.小写英文字母大写化)
禁果.诅咒(bytes, "解码", 字节串.解码)
禁果.诅咒(list, "追加", 列表.追加)
禁果.诅咒(list, "移除", 列表.移除)
禁果.诅咒(dict, "键", 字典.键)
禁果.诅咒(dict, "值", 字典.值)
禁果.诅咒(dict, "键值对", 字典.键值对)
from builtins import (
    str as 字符串, int as 整数, float as 浮点数, bool as 布尔值,
    list as 列表, dict as 字典, tuple as 元组, bytes as 字节串, bytearray as 字节数组,
    property as 属性装饰器, enumerate as 带索引迭代,
    max as 最大值, min as 最小值, print as 打印, input as 输入,
    isinstance as 对象是否是类的实例, all as 全部为真, any as 任意为真, len as 长度, sum as 求和, abs as 绝对值,
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
    def __enter__(当前对象: 打开) -> 打开:
        当前对象.文件 = open(
            当前对象.文件路径, 当前对象.模式,
            当前对象.缓冲大小, 当前对象.编码, 当前对象.错误处理模式,
            当前对象.换行符, 当前对象.是否在文件对象关闭时关闭文件描述符, 当前对象.文件自定义打开函数
        )
        return 当前对象
    def __exit__(当前对象: 打开, 异常类型, 异常值, 异常回溯):
        当前对象.文件.close()
    def 读取(当前对象: 打开, __读取长度: 可选[整数] = 无) -> 字符串:
        return 当前对象.文件.read(__读取长度)
    def 写入(当前对象: 打开, __文本: 可选[字符串]) -> 字符串:
        return 当前对象.文件.write(__文本)
    def 关闭(当前对象: 打开) -> 无:
        当前对象.文件.close()



class JSON:
    def __init__(当前对象: JSON) -> 永不使用:
        raise 值的类型不合法('"模块" 对象不可调用.')
    @静态方法
    def 解码(
        对象: 联合[字符串, 字节串, 字节数组],
        *,
        JSON解码器: 可选[类型[JSON解码器]] = 无,
        对象自定义解码函数: 可选[可调用[[字典[任意, 任意]], 任意]] = 无,
        浮点数自定义解码函数: 可选[可调用[[字符串], 任意]] = 无,
        整数自定义解码函数: 可选[可调用[[字符串], 任意]] = 无,
        常量自定义解码函数: 可选[可调用[[字符串], 任意]] = 无,
        对象自定义解码键值函数: 可选[可调用[[可迭代[元组[任意, 任意]]], 任意]] = 无,
        **关键字参数
        ) -> 任意:
        return json.loads(对象, cls = JSON解码器, object_hook = 对象自定义解码函数, parse_float = 浮点数自定义解码函数, parse_int = 整数自定义解码函数, parse_constant = 常量自定义解码函数, object_pairs_hook = 对象自定义解码键值函数, **关键字参数)
    @静态方法
    def 编码(
        对象: 任意,
        *,
        是否忽略非基本类型键: 可选[布尔值] = 假,
        是否转为美国信息互换标准代码: 可选[布尔值] = 真,
        是否检查循环引用: 可选[布尔值] = 真,
        是否允许不是一个数字的浮点数: 可选[布尔值] = 真,
        # cls
        缩进级别: 可选[联合[整数, 字符串]] = 无,
        值键分隔符: 可选[元组[字符串, 字符串]] = 无,
        # default
        是否排序键: 可选[布尔值] = 假,
        **关键字参数
        ) -> 字符串:
        return json.dumps(对象, skipkeys = 是否忽略非基本类型键, ensure_ascii = 是否转为美国信息互换标准代码, check_circular = 是否检查循环引用, allow_nan = 是否允许不是一个数字的浮点数, indent = 缩进级别, separators = 值键分隔符, sort_keys = 是否排序键, **关键字参数)
禁果.诅咒(json, "解码", JSON.解码)
禁果.诅咒(json, "编码", JSON.编码)
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



class 输入输出模块:
    class 字节流(io.BytesIO):
        def __init__(当前对象: 输入输出模块.字节流, 初始化字节串: 可选[字节串] = 无) -> 无:
            io.BytesIO.__init__(当前对象, initial_bytes = 初始化字节串)
        def 移动指针位置(当前对象: 输入输出模块.字节流, __偏移量: 整数, __偏移量参考位置标识: 整数 = 0) -> 整数:
            return 当前对象.seek(__偏移量, __偏移量参考位置标识)
        def 读取(当前对象: 输入输出模块.字节流, __读取长度: 可选[整数] = 无) -> 字节串:
            return 当前对象.read(__读取长度)
禁果.诅咒(io, "字节流", 输入输出模块.字节流)
import io as 输入输出模块




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
    @静态方法
    def 找出所有(
        匹配规则: 字符串,
        字符串: 字符串,
        匹配行为标志: 联合[整数, 正则表达式标志] = 0
    ) -> 列表[任意]:
        return re.findall(pattern = 匹配规则, string = 字符串, flags = 匹配行为标志)
禁果.诅咒(re, "替换", 正则.替换)
禁果.诅咒(re, "找出所有", 正则.找出所有)
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
    @静态方法
    def 时间() -> 浮点数:
        return time.time()
禁果.诅咒(time, "暂停执行", 时间.暂停执行)
禁果.诅咒(time, "性能计时器", 时间.性能计时器)
禁果.诅咒(time, "时间", 时间.时间)
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
    @静态方法
    def 处理器架构() -> 字符串:
        return platform.machine()
禁果.诅咒(platform, "操作系统名称", 平台.操作系统名称)
禁果.诅咒(platform, "架构信息", 平台.架构信息)
禁果.诅咒(platform, "处理器架构", 平台.处理器架构)
import platform as 平台




from _hashlib import HASH
class 散列:
    @静态方法
    def 安全散列算法256位(文本: 字节串, *, 是否用于安全环境: 布尔值 = 真) -> 散列对象:
        return hashlib.sha256(string = 文本, usedforsecurity = 是否用于安全环境)
class 散列对象(HASH):
    def 十六进制值(当前对象) -> 字符串:
        return 当前对象.hexdigest()
禁果.诅咒(hashlib, "安全散列算法256位", 散列.安全散列算法256位)
禁果.诅咒(HASH, "十六进制值", 散列对象.十六进制值)
import hashlib as 散列



class 基底64:
    @静态方法
    def 基底64编码(字符串: 字符串, 替代字符: 可选[字符串] = 无) -> 字节串:
        return base64.b64encode(s = 字符串, altchars = 替代字符)
禁果.诅咒(base64, "基底64编码", 基底64.基底64编码)
import base64 as 基底64





class 统一资源定位符:
    class 解析:
        @静态方法
        def 编码(
            字符串: 字符串,
            跳过编码的字符集: 联合[字符串, 可迭代[整数]] = "/",
            编码: 可选[字符串] = 无,
            错误处理模式: 可选[字符串] = 无
        ):
            return urllib.parse.quote(string = 字符串, safe = 跳过编码的字符集, encoding = 编码, errors = 错误处理模式)
    禁果.诅咒(urllib.parse, "编码", 解析.编码)
    禁果.诅咒(urllib, "解析", 解析)
    import urllib.parse as 解析




class 图像处理:
    class 图像:
        def 打开(位置: 联合[字符串, 字节串], 模式: 字面["r"] = "r", 格式: 可选[联合[列表[字符串], 元组[字符串, ...]]] = 无) -> 图像处理.图像.图像:
            return PIL.Image.open(fp = 位置, mode = 模式, formats = 格式)
        class 图像(PIL.Image.Image):
            def 加载像素数据(当前对象: PIL.Image.Image):
                return 当前对象.load()
            def 字节串化(当前对象: PIL.Image.Image, 编码器名称: 字符串 = "raw", *位置参数) -> 字节串:
                return 当前对象.tobytes(encoder_name = 编码器名称, *位置参数)
            def 保存(
                当前对象: PIL.Image.Image,
                位置: 联合[字符串, 字节串],
                格式: 可选[字符串] = 无,
                *,
                是否保存全部: 布尔值 = 真,
                # 位图图像格式: 字面["bmp", "png"] = 无,
                # 是否优化: 布尔值 = 无,
                **关键字参数):
                return 当前对象.save(fp = 位置, format = 格式, save_all = 是否保存全部, **关键字参数)
            @属性装饰器
            def 宽高(当前对象) -> 元组[整数, 整数]:
                return 当前对象.size
        禁果.诅咒(PIL.Image.Image, "加载像素数据", 图像.加载像素数据)
        禁果.诅咒(PIL.Image.Image, "字节串化", 图像.字节串化)
        禁果.诅咒(PIL.Image.Image, "保存", 图像.保存)
        禁果.诅咒(PIL.Image.Image, "宽高", 图像.宽高)
        from PIL.Image import Image as 图像
    禁果.诅咒(PIL.Image, "打开", 图像.打开)
    禁果.诅咒(PIL.Image, "图像", 图像.图像)
    import PIL.Image as 图像





class 网络请求:
    @静态方法
    def 获取(
            统一资源定位符: 联合[字符串, 字节串],
            查询参数: 可选[字典] = 无,
            *,
            表单数据: 可选[任意] = 无,
            请求头: 可选[字典] = 无,
            魔饼: 可选[字典] = 无,
            文件: 可选[字典[字符串, 任意]] = 无,
            认证: 可选[联合[元组[字符串, 字符串], 可调用]] = 无,
            超时: 可选[联合[联合[整数, 浮点数], 元组[联合[整数, 浮点数], 可选[联合[整数, 浮点数]]]]] = 无,
            是否允许重定向: 布尔值 = 真,
            # proxies: _TextMapping | None = ...,
            # hooks: _HooksInput | None = ...,
            是否逐步下载: 可选[布尔值] = 无,
            是否验证服务器证书: 可选[联合[布尔值, 字符串]] = 无,
            证书: 可选[联合[字符串, 元组[字符串, 字符串]]] = 无,
            JSON数据: 可选[任意] = 无
        ) -> 网络请求.响应:
        return requests.get(url = 统一资源定位符, params = 查询参数, data = 表单数据, headers = 请求头, cookies = 魔饼, files = 文件, auth = 认证, timeout = 超时, allow_redirects = 是否允许重定向, stream = 是否逐步下载, verify = 是否验证服务器证书, cert = 证书, json = JSON数据)
    @静态方法
    def 提交(
            统一资源定位符: 联合[字符串, 字节串],
            表单数据: 可选[任意] = 无,
            JSON数据: 可选[任意] = 无,
            *,
            查询参数: 可选[字典] = 无,
            请求头: 可选[字典] = 无,
            魔饼: 可选[字典] = 无,
            文件: 可选[字典[字符串, 任意]] = 无,
            认证: 可选[联合[元组[字符串, 字符串], 可调用]] = 无,
            超时: 可选[联合[联合[整数, 浮点数], 元组[联合[整数, 浮点数], 可选[联合[整数, 浮点数]]]]] = 无,
            是否允许重定向: 布尔值 = 真,
            # proxies: _TextMapping | None = ...,
            # hooks: _HooksInput | None = ...,
            是否逐步下载: 可选[布尔值] = 无,
            是否验证服务器证书: 可选[联合[布尔值, 字符串]] = 无,
            证书: 可选[联合[字符串, 元组[字符串, 字符串]]] = 无,
        ) -> 网络请求.响应:
        return requests.post(url = 统一资源定位符, data = 表单数据, json = JSON数据, params = 查询参数, headers = 请求头, cookies = 魔饼, files = 文件, auth = 认证, timeout = 超时, allow_redirects = 是否允许重定向, stream = 是否逐步下载, verify = 是否验证服务器证书, cert = 证书)
    class 会话(requests.Session):
        def 获取(
                当前对象: requests.Session,
                统一资源定位符: 联合[字符串, 字节串],
                查询参数: 可选[字典] = 无,
                *,
                表单数据: 可选[任意] = 无,
                请求头: 可选[字典] = 无,
                魔饼: 可选[字典] = 无,
                文件: 可选[字典[字符串, 任意]] = 无,
                认证: 可选[联合[元组[字符串, 字符串], 可调用]] = 无,
                超时: 可选[联合[联合[整数, 浮点数], 元组[联合[整数, 浮点数], 可选[联合[整数, 浮点数]]]]] = 无,
                是否允许重定向: 布尔值 = 真,
                # proxies: _TextMapping | None = ...,
                # hooks: _HooksInput | None = ...,
                是否逐步下载: 可选[布尔值] = 无,
                是否验证服务器证书: 可选[联合[布尔值, 字符串]] = 无,
                证书: 可选[联合[字符串, 元组[字符串, 字符串]]] = 无,
                JSON数据: 可选[任意] = 无
            ) -> 网络请求.响应:
            return 当前对象.get(url = 统一资源定位符, params = 查询参数, data = 表单数据, headers = 请求头, cookies = 魔饼, files = 文件, auth = 认证, timeout = 超时, allow_redirects = 是否允许重定向, stream = 是否逐步下载, verify = 是否验证服务器证书, cert = 证书, json = JSON数据)
        def 提交(
                当前对象: requests.Session,
                统一资源定位符: 联合[字符串, 字节串],
                表单数据: 可选[任意] = 无,
                JSON数据: 可选[任意] = 无,
                *,
                查询参数: 可选[字典] = 无,
                请求头: 可选[字典] = 无,
                魔饼: 可选[字典] = 无,
                文件: 可选[字典[字符串, 任意]] = 无,
                认证: 可选[联合[元组[字符串, 字符串], 可调用]] = 无,
                超时: 可选[联合[联合[整数, 浮点数], 元组[联合[整数, 浮点数], 可选[联合[整数, 浮点数]]]]] = 无,
                是否允许重定向: 布尔值 = 真,
                # proxies: _TextMapping | None = ...,
                # hooks: _HooksInput | None = ...,
                是否逐步下载: 可选[布尔值] = 无,
                是否验证服务器证书: 可选[联合[布尔值, 字符串]] = 无,
                证书: 可选[联合[字符串, 元组[字符串, 字符串]]] = 无,
            ) -> 网络请求.响应:
            return 当前对象.post(url = 统一资源定位符, data = 表单数据, json = JSON数据, params = 查询参数, headers = 请求头, cookies = 魔饼, files = 文件, auth = 认证, timeout = 超时, allow_redirects = 是否允许重定向, stream = 是否逐步下载, verify = 是否验证服务器证书, cert = 证书)
        @属性装饰器
        def 请求头(当前对象: requests.Session) -> 字典[字符串, 联合[字符串, 字节串]]:
            return 当前对象.headers
        禁果.诅咒(requests.Session, "获取", 获取)
        禁果.诅咒(requests.Session, "提交", 提交)
        禁果.诅咒(requests.Session, "请求头", 请求头)
    会话 = requests.Session
    class 响应(requests.Response):
        def JSON内容(
                当前对象: requests.Response,
                *,
                JSON解码器: 可选[类型[JSON解码器]] = 无,
                对象自定义解码函数: 可选[可调用[[字典[任意, 任意]], 任意]] = 无,
                浮点数自定义解码函数: 可选[可调用[[字符串], 任意]] = 无,
                整数自定义解码函数: 可选[可调用[[字符串], 任意]] = 无,
                常量自定义解码函数: 可选[可调用[[字符串], 任意]] = 无,
                对象自定义解码键值函数: 可选[可调用[[可迭代[元组[任意, 任意]]], 任意]] = 无,
                **关键字参数
            ) -> 任意:
            return 当前对象.json(cls = JSON解码器, object_hook = 对象自定义解码函数, parse_float = 浮点数自定义解码函数, parse_int = 整数自定义解码函数, parse_constant = 常量自定义解码函数, object_pairs_hook = 对象自定义解码键值函数, **关键字参数)
        @属性装饰器
        def 状态码(当前对象: requests.Response) -> 整数:
            return 当前对象.status_code
        @属性装饰器
        def 文本内容(当前对象: requests.Response) -> 字符串:
            return 当前对象.text
        @属性装饰器
        def 原始内容(当前对象: requests.Response) -> 字节串:
            return 当前对象.content
        禁果.诅咒(requests.Response, "JSON内容", JSON内容)
        禁果.诅咒(requests.Response, "状态码", 状态码)
        禁果.诅咒(requests.Response, "文本内容", 文本内容)
        禁果.诅咒(requests.Response, "原始内容", 原始内容)
    响应 = requests.Response
禁果.诅咒(requests, "获取", 网络请求.获取)
禁果.诅咒(requests, "提交", 网络请求.提交)
禁果.诅咒(requests, "会话", 网络请求.会话)
禁果.诅咒(requests, "响应", 网络请求.响应)
import requests as 网络请求





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
    可重入锁 = threading.RLock
    class 可重入锁:
        def 获取(当前对象: threading.RLock, 是否阻塞: 可选[布尔值] = 真, 超时秒数: 联合[整数, 浮点数] = -1) -> 布尔值:
            return 当前对象.acquire(blocking = 是否阻塞, timeout = 超时秒数)
        def 释放(当前对象: threading.RLock) -> 无:
            return 当前对象.release()
    禁果.诅咒(threading._RLock, "获取", 可重入锁.获取)
    禁果.诅咒(threading._RLock, "释放", 可重入锁.释放)
    可重入锁 = threading.RLock
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
禁果.诅咒(threading, "可重入锁", 线程.可重入锁)
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
            # user: str | int | 无 = 无,
            # group: str | int | 无 = 无,
            # extra_groups: Iterable[str | int] | 无 = 无,
            编码: 可选[字符串] = 无,
            输出解码错误处理模式: 可选[字面["strict", "ignore", "replace"]] = 无,
            是否以文本模式返回输出: 可选[布尔值] = 无,
            # umask: int = -1,
            # pipesize: int = -1,
            # process_group: int | 无 = 无
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
        def 等待终止(当前对象: 子进程.启动进程, 超时秒数: 可选[联合[整数, 浮点数]] = 无) -> 整数:
            return 当前对象.wait(timeout = 超时秒数)
        @属性装饰器
        def 标准输出(当前对象: 子进程.启动进程) -> 输入输出:
            return 当前对象.stdout
        @属性装饰器
        def 标准错误输出(当前对象: 子进程.启动进程) -> 输入输出:
            return 当前对象.stderr
        @属性装饰器
        def 标准输入(当前对象: 子进程.启动进程) -> 输入输出:
            return 当前对象.stdin
禁果.诅咒(subprocess, "管道", 子进程.管道)
禁果.诅咒(subprocess, "标准输出", 子进程.标准输出)
禁果.诅咒(subprocess, "启动进程", 子进程.启动进程)
import subprocess as 子进程



class 套接字:
    地址族_互联网协议版本四 = socket.AF_INET
    地址族_互联网协议版本六 = socket.AF_INET6
    传输类型_流式 = socket.SOCK_STREAM
    传输类型_数据报 = socket.SOCK_DGRAM
    def __init__(当前对象) -> 永不使用:
        raise 值的类型不合法('"模块" 对象不可调用.')
    class 套接字(socket.socket):
        def __init__(
            当前对象: 套接字.套接字,
            地址族: 整数 = -1,
            传输类型: 整数 = -1,
            传输协议: 整数 = -1,
            文件描述符: 可选[整数] = 无
        ) -> 无:
            super().__init__(family = 地址族, type = 传输类型, proto = 传输协议, fileno = 文件描述符)
        def 设置超时时间(当前对象: 套接字.套接字, 秒数: 联合[整数, 浮点数]) -> 无:
            return 当前对象.settimeout(秒数)
        def 绑定地址(当前对象: 套接字.套接字, 地址: 元组[字符串, 整数]) -> 无:
            return 当前对象.bind(地址)
        def 关闭(当前对象: 套接字.套接字) -> 无:
            return 当前对象.close()
        def 连接_不引发异常(当前对象: 套接字.套接字, 地址: 元组[字符串, 整数]) -> 整数:
            return 当前对象.connect_ex(地址)
禁果.诅咒(socket, "地址族_互联网协议版本四", 套接字.地址族_互联网协议版本四)
禁果.诅咒(socket, "地址族_互联网协议版本六", 套接字.地址族_互联网协议版本六)
禁果.诅咒(socket, "传输类型_流式", 套接字.传输类型_流式)
禁果.诅咒(socket, "传输类型_数据报", 套接字.传输类型_数据报)
禁果.诅咒(socket, "套接字", 套接字.套接字)
import socket as 套接字
