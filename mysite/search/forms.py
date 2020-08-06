from django import forms
from captcha.fields import CaptchaField

class UserForm(forms.Form):
	email = forms.CharField(label="邮箱",max_length=128,widget=forms.TextInput)
	password = forms.CharField(label="密码",max_length=256,widget=forms.PasswordInput)
	captcha = CaptchaField(label='验证码')

class RegisterForm(forms.Form):
	email = forms.CharField(label="邮箱", max_length=128, widget=forms.TextInput)
	password = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput)
	password_repeat = forms.CharField(label="确认密码", max_length=256, widget=forms.PasswordInput)
	captcha = CaptchaField(label='验证码')
