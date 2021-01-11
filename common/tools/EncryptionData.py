'''
@Description:
@Author: michael
@Date: 2020-01-08 11:39:20
LastEditTime: 2020-01-08 20:00:00
LastEditors: michael
'''
# coding=utf-8

import base64


class EncryptionData:


    left_str = '@dash'
    right_str = '$*%&^@#'


    # 加密
    async def encryption(self, ostr):
        ''': ostr 加密前的字符串'''
        mstr = self.left_str + ostr + self.right_str
        #接收bytes入参，返回bytes加密结果
        base_result = base64.b64encode(mstr.encode())
        #返回的bytes数据通过decode()转换为字符串
        new_mstr = base_result.decode()
        # print(new_mstr)
        return new_mstr


    # 解密
    async def decryption(self, mstr):
        ''': mstr 加密后的字符串'''
        base_result = base64.b64decode(mstr)
        ostr = base_result.decode()
        # print(ostr)
        return ostr


    # 创建加密 id 
    async def createEncryptionId(self, start_num, end_num):

        data = []

        for i in range(start_num, end_num):
            encryptionId = await self.encryption(str(i))
            data.append(encryptionId)
            # print(encryptionId)

        return data
        





encryptionData = EncryptionData()