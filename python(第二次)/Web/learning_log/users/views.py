from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def logout_view(request):
	'''注销用户'''
	logout(request)
	return HttpResponseRedirect(reverse('learning_logs:index'))

def register(request):
	'''注册新用户'''
	if request.method != 'POST':
		# 显示空的注册表单
		form = UserCreationForm()
	else:
		# 处理填写好的表单
		form = UserCreationForm(data=request.POST)

		if form.is_valid():
			new_user = form.save()
			new_user.set_password(request.POST['password1'])

			# 让用户自动登录，再重定向到主页
			# authenticated_user = authenticate(request, username=new_user.username, possword=request.POST['password1'])
			login(request, new_user, backend='django.contrib.auth.backends.ModelBackend')
			return HttpResponseRedirect(reverse('learning_logs:index'))

	context = {'form': form}
	return render(request, 'users/register.html', context)

