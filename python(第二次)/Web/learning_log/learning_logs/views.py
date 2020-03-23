from django.shortcuts import render  # 导入函数 render()
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import TopicForm, EntryForm

from .models import Topic, Entry
from django.contrib.auth.decorators import login_required

from django.shortcuts import get_object_or_404
from django.http import Http404

# Create your views here.
def index(request):
	'''学习笔记的主页'''
	return render(request, 'learning_logs/index.html')

@login_required # 將 login_required() 作为装饰器(decorator)用于视图函数topics() 在其前面加上@，让Python在运行topics()之前先运行login_required()代码
def topics(request):
	'''显示所有的主题'''
	topics = Topic.objects.filter(owner=request.user).order_by('date_added') # 查询数据库---请求提供Topic对象，并按属行date_added 对它们进行排序
	context = {'topics': topics} # 要发送给模板的上下文
	return render(request, 'learning_logs/topics.html', context)

@login_required
def topic(request, topic_id):
	'''显示单个主题及其所有的条目'''
	# topic = Topic.objects.get(id=topic_id)
	topic = get_object_or_404(Topic, id=topic_id)
	# 确认请求的主题属于当前用户
	if topic.owner != request.user:
		raise Http404
	entries = topic.entry_set.order_by('-date_added') # 降序排列
	context = {'topic': topic, 'entries': entries}
	return render(request, 'learning_logs/topic.html', context)

@login_required
def new_topic(request):
	'''添加新主题'''
	if request.method != 'POST':
		# 未提交数据：创建一个新表单
		form = TopicForm()
	else:
		# POST 提交的数据，对数据进行处理
		form = TopicForm(request.POST)
		if form.is_valid():
			new_topic = form.save(commit=False) # 先修改主题再将其保存至数据库中
			new_topic.owner = request.user
			new_topic.save()
			return HttpResponseRedirect(reverse('learning_logs:topics'))
	context = {'form': form}

	return render(request, 'learning_logs/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
	'''在特定的主题中添加新条目'''
	topic = Topic.objects.get(id=topic_id)

	if request.method != 'POST':
		# 未提交数据，创建一个控表单
		form = EntryForm()
	else:
		# POST 提交的数据，对数据进行处理
		form = EntryForm(data=request.POST)
		if form.is_valid():
			new_entry = form.save(commit=False)  #创建一个新条目对象，并将其保存在new_entry中，但不将其保存在数据库中
			new_entry.topic = topic
			new_entry.save()
			return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic_id]))
	context = {'topic': topic, 'form': form}
	return render(request, 'learning_logs/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
	'''编辑既有条目'''
	entry = Entry.objects.get(id=entry_id)
	topic = entry.topic
	if topic.owner != request.user:
		raise Http404
	if request.method != 'POST':
	    # 初次请求，使用当前条目填充表单
	    form = EntryForm(instance=entry)
	else:
		# POST 提交的数据，对数据进行处理
		form = EntryForm(instance=entry, data=request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic.id]))
	context = {'entry':entry, 'topic': topic, 'form': form}
	return render(request, 'learning_logs/edit_entry.html', context)


















