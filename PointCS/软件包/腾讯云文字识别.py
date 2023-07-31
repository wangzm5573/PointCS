from .蟒蛇 import *
import requests
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException as 腾讯云软件开发套件异常
from tencentcloud.ocr.v20181119 import ocr_client, models
__all__ = ["腾讯云软件开发套件异常", "广告文字识别"]



with 打开("./程序/腾讯云/秘密.json", "r", 编码 = "UTF-8") as 文件:
    秘密 = JSON.解码(文件.读取())
    秘密标识 = 秘密["秘密标识"]
    秘密密钥 = 秘密["秘密密钥"]
凭据 = credential.Credential(秘密标识, 秘密密钥)
httpProfile = HttpProfile()
httpProfile.endpoint = "ocr.tencentcloudapi.com"
clientProfile = ClientProfile()
clientProfile.httpProfile = httpProfile
client = ocr_client.OcrClient(凭据, "ap-shanghai", clientProfile)



def 广告文字识别(图片基底64: 字符串) -> JSON:
    req = models.AdvertiseOCRRequest()
    params = {
        "ImageBase64": 图片基底64
    }
    req.from_json_string(JSON.编码(params))
    resp = client.AdvertiseOCR(req)
    return JSON.解码(resp.to_json_string())
