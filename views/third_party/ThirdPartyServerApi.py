'''
@Description:
@Author: michael
@Date: 2020-01-08 11:39:20
LastEditTime: 2020-01-08 20:00:00
LastEditors: michael
'''
# coding=utf-8

import requests
import datetime
import time
import random
from hashlib import sha1
import json

class ThirdPartyServerApi:

    AppKey = ''                    # 开发者平台分配的AppKey
    AppSecret = ''                 # 开发者平台分配的AppSecret,可刷新
    Nonce = ''                     # 随机数（最大长度128个字符）
    CurTime = ''                   # 当前UTC时间戳，从1970年1月1日0点0 分0 秒开始到现在的秒数(String)
    CheckSum = ''                  # SHA1(AppSecret + Nonce + CurTime),三个参数拼接的字符串，进行SHA1哈希计算，转化成16进制字符(String，小写)
    randStr = '0123456789abcdef'   # 随机字符串可选字符


    # 测试接口
    async def test(self):
        await self.checkSumBuilder()
        return 11111


    # 参数初始化
    async def construct(self, AppKey, AppSecret):
        '''
        : param $AppKey
        : param $AppSecret
        : param $RequestType [选择 python 请求方式，requests 或 curl, 若为curl方式，请检查 python 配置是否开启]
        '''

        self.AppKey = AppKey
        self.AppSecret = AppSecret

    # 创建云信id
    async def createAccid(self, accid, name=''):
        '''
        : param  accid    网易云通信ID
        : param  name     云通信ID昵称
        '''

        url = 'https://api.netease.im/nimserver/user/create.action'
        data = {
            'accid':accid,
            'name':name
        }

        result = await self.postDataRequests(url, data)
        
        return result

    # 更新用户 token 过期时间
    async def updateToken(self, accid, token):
        '''
        : param  accid    网易云通信ID
        : param  token    用户 toke
        '''

        url = 'https://api.netease.im/nimserver/user/update.action'
        data = {
            'accid':accid,
            'token':token
        }

        result = await self.postDataRequests(url, data)
        
        return result


    # 重置用户 token
    async def refreshToken(self, accid):
        '''
        : param  accid    网易云通信ID
        '''
        url = 'https://api.netease.im/nimserver/user/refreshToken.action'
        data = {
            'accid':accid
        }

        result = await self.postDataRequests(url, data)
        
        return result


    # 封禁用户
    async def userBlock(self, accid):
        '''
        : param  accid    网易云通信ID
        '''

        url = 'https://api.netease.im/nimserver/user/block.action'
        data = {
            'accid':accid
        }

        result = await self.postDataRequests(url, data)
        
        return result


    # 解禁用户
    async def userUnBlock(self, accid):
        '''
        : param  accid    网易云通信ID
        '''

        url = 'https://api.netease.im/nimserver/user/unblock.action'
        data = {
            'accid':accid
        }

        result = await self.postDataRequests(url, data)
        
        return result


    # 批量创建用户
    async def manyEncryptionId(self, id_list):
        ''': param id_list id的list列表'''
        data = {
            "code": 200,
            "info": {
                "name": "",
                "accid": "12333",
                "token": "443963ad5a2216dc3061e3bc961471bd"
            }
        }
        test = []
        for id in id_list:
            test.append(data)
            # print(id)

        print(test)
        # return test
        



    # 使用REQUESTS方式发送post请求
    async def postDataRequests(self, url, data):
        '''
        : param  url     [请求地址]
        : param  data    [array格式数据]
        : return 请求返回结果(dict)
        '''

        await self.checkSumBuilder();       # 发送请求前需先生成checkSum

        http_header = {
            'AppKey': self.AppKey,
            'Nonce': self.Nonce,
            'CurTime': self.CurTime,
            'CheckSum': self.CheckSum,
            'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8'
        }

        result = requests.post(url, headers=http_header, data=data)
        # print(111111111111)
        # print(http_header)
        # print(result)
        return result.json()
        # print(data)
        # print(111111111111)
        
        
    # API checksum校验生成
    async def checkSumBuilder(self):
        '''
        : param  void
        : return CheckSum(对象私有属性)
        '''

        # 此部分生成随机字符串
        hex_digits = self.randStr

        for i in range(0, 128):               
            '''随机字符串最大128个字符，也可以小于该数'''
            self.Nonce += random.choice(hex_digits)

        self.CurTime = str(self.getTime())         
        '''当前时间戳，以秒为单位'''

        join_string = self.AppSecret + self.Nonce + self.CurTime
        sha = sha1()
        sha.update(join_string.encode("utf-8"))
        encrypts = sha.hexdigest()
        self.CheckSum = encrypts
        # print(self.CheckSum)
    

    # 获取时间戳
    def getTime(self):

        '''注释掉的代码为 - 时间戳转换为 - 年-月-日 时:分:秒'''
        # last_hour = datetime.fromtimestamp(self.getTime()+10*60)
        # print('last_hour = ',last_hour)

        da_1 = datetime.datetime.now()
        da_2 = datetime.datetime.timetuple(da_1)
        return int(time.mktime(da_2))







serverApi = ThirdPartyServerApi()