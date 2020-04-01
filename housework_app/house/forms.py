from django import forms
from .models import User, Housework, Workreport, Day_rank


class User(forms.ModelForm):
    class Meta:
        model = User
        fields = ["user_id", "username", "password"]


class Housework(forms.ModelForm):
    class Meta:
        model = Housework
        fields = ["housework_id", "housework_name", "point"]


class Workreport(forms.ModelForm):
    class Meta:
        model = Workreport
        fields = ["workreport_id", "user_id", "housework_id", "rep_date"]


class Day_rank(forms.ModelForm):
    class Meta:
        model = Day_rank
        fields = ["date_id", "date", "user_id", "total_point"]


class UsernameForm(forms.Form):
    username = forms.CharField(max_length=50,
                               required=True,
                               label="",
                               widget=forms.TextInput(
                                attrs={
                                    'placeholder': 'ユーザ名を入力してください．'
                                }
                                ))


class PasswordForm(forms.Form):
    password = forms.CharField(max_length=50, required=True, label="",
                               widget=forms.TextInput(
                                attrs={
                                    'placeholder': 'パスワードを入力してください．'
                                }
                                ))


class HouseworkNameForm(forms.Form):
    housework_name = forms.CharField(max_length=50, required=True, label="家事名")


class HouseworkPointForm(forms.Form):
    point = forms.IntegerField(min_value=0, required=True, label="家事ポイント")


class HouseworkCheckForm(forms.Form):
    def __init__(self, housework_name=[], *args, **kwargs):
        super(HouseworkCheckForm, self).__init__(*args, **kwargs)
        # このフォームの変数はhousework_check_name
        self.fields["housework_check_name"] = forms.MultipleChoiceField(
            choices=[(item.housework_name, item.housework_name+" "+str(item.point)) for item in housework_name],
            widget=forms.CheckboxSelectMultiple(),
            label=""
        )
