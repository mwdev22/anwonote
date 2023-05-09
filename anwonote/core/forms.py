from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from topic.models import Category

class LoginForm(AuthenticationForm):
    username = forms.CharField(min_length=5, max_length=20, widget=forms.TextInput(attrs={
        'placeholder':'Nazwa Użytkownika',
        'class': 'w-full py-4 px-6 rounded-xl'
    }),help_text = 'Nazwa użytkownika powinna mieścić między 5 a 20 znakami.'
    )
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Hasło',
        'class': 'w-full py-4 px-6 rounded-xl',
    }))

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Nazwa Użytkownika',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder':'Email',
        'class': 'w-full py-4 px-6 rounded-xl',
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Hasło',
        'class': 'w-full py-4 px-6 rounded-xl',
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Powtórz hasło',
        'class': 'w-full py-4 px-6 rounded-xl',
    }))
'''
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()

        Category.objects.create(
            name=f"Kategoria użytkownika {user.username}",
            created_by=user
        )

        return user
'''