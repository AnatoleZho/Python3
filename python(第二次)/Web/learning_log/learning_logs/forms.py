from django import forms

from .models import Topic, Entry

class TopicForm(forms.ModelForm):
	'''主题表单类'''
	class Meta:
		'''根据主题模型创建表单'''
		model = Topic
		fields = ['text']  # 该表单值包含字段 text
		labels = {'text': ''} # 让 Django 不要为字段 text 生成标签


class EntryForm(forms.ModelForm):
	'''条目表单类'''
	class Meta:
		model = Entry
		fields = ['text']
		labels = {'text': ''}
		widgets = {'text': forms.Textarea(attrs={'cols':80})}

