'''
@Description:
@Author: michael
@Date: 2020-01-11 16:39:20
LastEditTime: 2020-01-11 20:00:00
LastEditors: michael
'''
# coding=utf-8

import requests
from views.third_party.ThirdPartyServerApi import serverApi
from common.tools.EncryptionData import encryptionData

class ThirdParty:
    
    

    async def returnCreateAccount(self):

        # 使用示例
        # 网易云信分配的账号，请替换你在管理后台应用下申请的Appkey
        AppKey = 'bde4bb6f88743573d47066e3042b2136'

        # 网易云信分配的账号，请替换你在管理后台应用下申请的appSecret
        AppSecret = '4d5ddc48819d'

        await serverApi.construct(AppKey, AppSecret)

        id_list = await encryptionData.createEncryptionId(1, 100)
        result = await serverApi.manyEncryptionId(id_list)
        return result
        # 创建用户
        # result = await serverApi.createAccid('12333')
        
        # 刷新用户 TOKEN
        # result = await serverApi.updateToken('123', '45eda68a16c3f6f128471801987b6f2d')

        # 重置用户 TOKEN
        # result = await serverApi.refreshToken('123')

        # 重置用户 TOKEN
        # result = await serverApi.refreshToken('123')

        # 重置用户 TOKEN
        # result = await serverApi.refreshToken('123')

        # result = await encryptionData.encryption('123123')
        # result = await encryptionData.decryption(result)

        

        # return result

        
            
            










thirdParty = ThirdParty()