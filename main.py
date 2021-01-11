'''
@Description:
@Author: michael
@Date: 2020-12-09 19:48:20
LastEditTime: 2020-12-29 20:00:00
LastEditors: michael
'''

# coding=utf-8

import uvicorn
from fastapi import FastAPI
from routers import VideoLinkRouter
from routers import ThirdPartyRouter

app = FastAPI()

# 本地 - 测试路由
app.include_router(VideoLinkRouter.router)

# 第三方 - 测试路由
app.include_router(ThirdPartyRouter.router)

