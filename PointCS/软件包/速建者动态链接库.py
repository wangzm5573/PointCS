# 此文件来源: https://github.com/LNSSPsd/PhoenixBuilder/blob/main/fastbuilder/external/dylib/conn.py
from __future__ import annotations
from .插件 import *
import ctypes
__all__ = ["连接速建者", "关闭速建者连接", "接收数据包", "发送数据包", "发送命令到速建者", "发送无回复命令到服务器", "发送玩家命令到服务器", "发送网络套接字命令到服务器", "数据包字节串到数据包字符串", "数据包字符串到数据包字节串",
           "速建者动态链接库异常", "速建者解码数据包异常"]

去语言整数 = ctypes.c_longlong
去语言字符串 = ctypes.c_char_p
去语言字节串 = ctypes.POINTER(ctypes.c_char)
class 速建者动态链接库异常(异常): pass
class 速建者解码数据包异常(速建者动态链接库异常): pass

class 去语言整数切片(ctypes.Structure):
    _fields_ = [("data", ctypes.POINTER(去语言整数)),
                ("len", 去语言整数),
                ("cap", 去语言整数)]

class 去语言字节切片(ctypes.Structure):
    _fields_ = [("data", 去语言字节串),
                ("len", 去语言整数),
                ("cap", 去语言整数)]

class ConnectFB函数返回类型(ctypes.Structure):
    _fields_ = [("connID", 去语言整数),
                ("err", 去语言字符串)]

class RecvGamePacket函数返回类型(ctypes.Structure):
    _fields_ = [("pktBytes", 去语言字节串),
                ('l', 去语言整数),
                ("err", 去语言字符串)]

class SendWSCommand函数返回类型(ctypes.Structure):
    _fields_ = [("uuid", 去语言字符串),
                ("err", 去语言字符串)]

class SendMCCommand函数返回类型(ctypes.Structure):
    _fields_ = [("uuid", 去语言字符串),
                ("err", 去语言字符串)]

class GamePacketBytesAsIsJsonStr函数返回类型(ctypes.Structure):
    _fields_ = [("jsonStr", 去语言字符串),
                ("err", 去语言字符串)]

class JsonStrAsIsGamePacketBytes函数返回类型(ctypes.Structure):
    _fields_ = [("pktBytes", 去语言字节串),
                ('l', 去语言整数),
                ("err", 去语言字符串)]





def 初始化动态链接库():
    LIB = ctypes.CDLL(f"./程序/速建者/{操作系统名称}_{位架构}.动态链接库")

    LIB.ConnectFB.argtypes = [去语言字符串]
    LIB.ConnectFB.restype = ConnectFB函数返回类型

    LIB.ReleaseConnByID.argtypes = [去语言整数]

    LIB.RecvGamePacket.argtypes = [去语言整数]
    LIB.RecvGamePacket.restype = RecvGamePacket函数返回类型

    LIB.SendGamePacketBytes.argtypes = [去语言整数, 去语言字节切片]
    LIB.SendGamePacketBytes.restype = 去语言字符串

    LIB.SendFBCommand.argtypes = [去语言整数, 去语言字符串]
    LIB.SendFBCommand.restype = 去语言字符串

    LIB.SendWSCommand.argtypes = [去语言整数, 去语言字符串]
    LIB.SendWSCommand.restype = SendWSCommand函数返回类型

    LIB.SendMCCommand.argtypes = [去语言整数, 去语言字符串]
    LIB.SendMCCommand.restype = SendMCCommand函数返回类型

    LIB.SendNoResponseCommand.argtypes = [去语言整数, 去语言字符串]
    LIB.SendNoResponseCommand.restype = 去语言字符串

    LIB.GamePacketBytesAsIsJsonStr.argtypes = [去语言字节切片]
    LIB.GamePacketBytesAsIsJsonStr.restype = GamePacketBytesAsIsJsonStr函数返回类型

    LIB.JsonStrAsIsGamePacketBytes.argtypes = [去语言整数, 去语言字符串]
    LIB.JsonStrAsIsGamePacketBytes.restype = JsonStrAsIsGamePacketBytes函数返回类型

    # LIB.CreatePacketInJsonStrByID.argtypes = [去语言整数]
    # LIB.CreatePacketInJsonStrByID.restype = 去语言字符串

    LIB.FreeMem.argtypes=[ctypes.c_void_p]

    return LIB

动态链接库 = 初始化动态链接库()

def 蟒蛇整数到去语言整数(整数: 整数):
    return 去语言整数(整数)

def 蟒蛇字符串到去语言字符串(字符串: 字符串):
    return 去语言字符串(字节串(字符串, encoding = "UTF-8"))

def 蟒蛇字节串到去语言字节切片(字节串: 字节串):
    字节串长度 = 长度(字节串)
    关键字参数 = {
        'data': (ctypes.c_char * 字节串长度)(*字节串),
        'len': 字节串长度,
        'cap': 字节串长度,
    }
    return 去语言字节切片(**关键字参数)

def 释放内存(地址):
    动态链接库.FreeMem(地址)

def 检查结构中的异常(r):
    if r.err is not 无:
        错误信息 = r.err.解码("UTF-8")
        # freeMem(r.err)
        raise 速建者动态链接库异常(错误信息)

def 检查异常(r: 字节串):
    if r is not 无:
        错误信息 = r.解码("UTF-8")
        # freeMem(r.err)
        raise 速建者动态链接库异常(错误信息)



def 连接速建者(互联网协议地址: 字符串) -> 整数:
    返回数据 = 动态链接库.ConnectFB(蟒蛇字符串到去语言字符串(互联网协议地址))
    检查结构中的异常(返回数据)
    return 返回数据.connID


def 关闭速建者连接(连接标识: 整数) -> 无:
    动态链接库.ReleaseConnByID(蟒蛇整数到去语言整数(连接标识))


def 接收数据包(连接标识: 整数) -> 字节串:
    返回数据 = 动态链接库.RecvGamePacket(蟒蛇整数到去语言整数(连接标识))
    检查结构中的异常(返回数据)
    数据包字节串长度 = 返回数据.l
    数据包字节串 = 返回数据.pktBytes[ : 数据包字节串长度]
    释放内存(返回数据.pktBytes)
    return 数据包字节串


def 发送数据包(连接标识: 整数, 数据包字节串: 字节串) -> 无:
    去语言数据包字节切片 = 蟒蛇字节串到去语言字节切片(数据包字节串)
    返回数据 = 动态链接库.SendGamePacketBytes(连接标识, 去语言数据包字节切片)
    检查异常(返回数据)


def 发送命令到速建者(连接标识: 整数, 命令: 字符串) -> 无:
    返回数据 = 动态链接库.SendFBCommand(蟒蛇整数到去语言整数(连接标识), 蟒蛇字符串到去语言字符串(命令))
    检查异常(返回数据)


def 发送无回复命令到服务器(连接标识: 整数, 命令: 字符串) -> 无:
    返回数据 = 动态链接库.SendNoResponseCommand(蟒蛇整数到去语言整数(连接标识), 蟒蛇字符串到去语言字符串(命令))
    检查异常(返回数据)


def 发送玩家命令到服务器(连接标识: 整数, 命令: 字符串) -> 字符串:
    返回数据 = 动态链接库.SendMCCommand(蟒蛇整数到去语言整数(连接标识), 蟒蛇字符串到去语言字符串(命令))
    检查结构中的异常(返回数据)
    通用唯一标识符 = 返回数据.uuid[:]
    释放内存(返回数据.uuid)
    return 通用唯一标识符


def 发送网络套接字命令到服务器(连接标识: 整数, 命令: 字符串) -> 字符串:
    返回数据 = 动态链接库.SendWSCommand(蟒蛇整数到去语言整数(连接标识), 蟒蛇字符串到去语言字符串(命令))
    检查结构中的异常(返回数据)
    通用唯一标识符 = 返回数据.uuid[:]
    释放内存(返回数据.uuid)
    return 通用唯一标识符


def 数据包字节串到数据包字符串(数据包字节串: 字节串) -> 字符串:
    返回数据 = 动态链接库.GamePacketBytesAsIsJsonStr(蟒蛇字节串到去语言字节切片(数据包字节串))
    数据包标识 = 数据包字节串[0]
    try:
        检查结构中的异常(返回数据)
    except 速建者动态链接库异常 as 异常对象:
        raise 速建者解码数据包异常(f"解码数据包 {数据包标识} 异常: {字符串(异常对象)}") from 异常对象
    数据包字符串 = 返回数据.jsonStr.解码("UTF-8")
    # 释放内存(返回数据.jsonStr)
    return 数据包字符串


def 数据包字符串到数据包字节串(数据包标识: 整数, 数据包字符串: 字符串) -> 字节串:
    返回数据 = 动态链接库.JsonStrAsIsGamePacketBytes(蟒蛇整数到去语言整数(数据包标识), 蟒蛇字符串到去语言字符串(数据包字符串))
    检查结构中的异常(返回数据)
    数据包字节串长度 = 返回数据.l
    数据包字节串 = 返回数据.pktBytes[ : 数据包字节串长度]
    释放内存(返回数据.pktBytes)
    return 数据包字节串
