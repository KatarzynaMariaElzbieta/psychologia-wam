from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.models import User
from django_summernote.widgets import SummernoteWidget

from articles.models import Article, Tags


class SignUpForm(forms.Form):
    user_name = forms.CharField(label="Login", max_length=50)
    first_name = forms.CharField(label="Imię", max_length=50)
    last_name = forms.CharField(label="Nazwisko", max_length=50)
    password = forms.CharField(label="Hasło", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Powtórz hasło", widget=forms.PasswordInput)

    def clean_user_name(self):
        user_name = self.cleaned_data['user_name']
        if User.objects.filter(username=user_name).exists():
            raise forms.ValidationError("Nazwa użytkownika jest już zajęta.")
        return user_name

    def clean_password(self):
        password = self.cleaned_data.get("password")
        errors = dict()
        try:
            password_validation.validate_password(password)
        except forms.ValidationError as e:
            errors["password"] = list(e.messages)
        if errors:
            raise forms.ValidationError("Hasło za krótkie.")


class LoginForm(forms.Form):
    login = forms.CharField(label="Login", max_length=50)
    password = forms.CharField(label="Hasło", widget=forms.PasswordInput)


class ArticleForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(queryset=Tags.objects.all(),
                                          widget=forms.SelectMultiple(attrs={'class': 'name'}))

    class Meta:
        model = Article
        exclude = ['create_date', 'update_date', 'user_author', 'tags_article']
        widgets = {
            'body': SummernoteWidget(),
        }
