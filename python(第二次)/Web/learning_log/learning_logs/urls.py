'''定义learning_logs的URL模式'''

from django.urls import path # 导入函数 path，需要使用它来将 URL 映射到视图
from django.conf.urls import url
from . import views # 句点让 Python 从前的 urls.py 模块所在的文件夹中导入视图

app_name = 'learning_logs'

urlpatterns = [ # 包含可在应用程序 learning_logs 中请求的网页
	# 主页
	url(r'^$', views.index, name='index'),

	# 显示所有的主题
	url(r'topics/$', views.topics, name='topics'),

    # 特定主题的详细页面
    url(r'topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),

    # 用于添加新主题的网页
    url(r'^new_topic/$', views.new_topic, name='new_topic'),

    # 用于添加新条目的页面
    url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),

    # 用于编辑条目的页面
    url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),
    

]