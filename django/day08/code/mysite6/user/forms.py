from django import forms

class MyRegFrom(forms.Form):
    #限定username 必须大于等于6个字符
    username=forms.CharField(label='用户名',initial='请填写合适的用户名！',required=False)
    password=forms.CharField(label='密码',widget=forms.PasswordInput)
    password2=forms.CharField(label='重复密码')
    age=forms.IntegerField(label='年龄')
    def clean_username(self):
        '''此方法限定username必须为大于等于6个字符'''
        uname=self.cleaned_data['username']
        if len(uname)<6:
            raise forms.ValidationError('用户名太短')
        return uname