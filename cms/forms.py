from django.forms import ModelForm
from cms.models import Anken, Sintyoku
from django import forms
from django.contrib.auth import forms as auth_forms


class LoginForm(auth_forms.AuthenticationForm):
    '''ログインフォーム'''
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        for field in self.fields.values():
            field.widget.attrs['placeholder'] = field.label

class AnkenForm(ModelForm):
    """案件のフォーム"""
    class Meta:
        model = Anken
        fields = ('enduser', 'hansha', 'product', 'sbkk', 'hansui', 'sisuisin', 'hitouch', 'donyusien', 'jutyu', 'donyu', 'kakudo', 'kyougou', 'mitumorigaku', 'arari',)
        """日付の入力をプルダウンで。"""
        widgets = {
            'jutyu': forms.SelectDateWidget(years=[x for x in range(2019, 2030)]),
            'donyu': forms.SelectDateWidget(years=[x for x in range(2019, 2030)])
        }


class SintyokuForm(ModelForm):
    """進捗のフォーム"""
    class Meta:
        model = Sintyoku
        fields = ('kinyubi', 'shosai', )






