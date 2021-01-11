
'''
@Description:
@Author: michael
@Date: 2020-01-07 14:48:20
LastEditTime: 2020-01-07 20:00:00
LastEditors: michael
'''
# coding=utf-8

# 第三方包
from fastapi import APIRouter
from views.ThirdParty import thirdParty

# 创建 APIRouter 实例
router = APIRouter()

# 第三方 - 发送请求测试
@router.get('/api/thirdParty/createAccount')
async def createAccountRouter():
    '''创建第三方账号'''

    return await thirdParty.returnCreateAccount()