# -*- coding: utf-8 -*-
# @Time    : 2020/12/4 9:21
# @Author  : 十忆九非
# @Email   : shiyijiufei@gmail.com
# @File    : urls.py
# @Software: PyCharm


""" 定义 learning 的 url 模式"""

from django.urls import path
from . import views

app_name = 'website'
urlpatterns = [
    # 主页
    path('', views.index, name='index'),
    # 主题
    path('topics/',views.topics,name='topics'),
    # 特定主题的详细页面
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # 用于添加新主题的网页
    path('new_topic/', views.new_topic, name='new_topic'),
    # 添加新的条目
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry')
]