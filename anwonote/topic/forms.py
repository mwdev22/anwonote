from django import forms

from .models import Topic,Category

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl'

class NewPostForm(forms.ModelForm):
    status = forms.ChoiceField(choices=Topic.STATUS_CHOICES)
    class Meta:
        model = Topic
        fields = ('category', 'name', 'content','status')

        widgets = {
            'category' : forms.Select(attrs={
            'class' : INPUT_CLASSES
            }),
            'name' : forms.TextInput(attrs={
            'class' : INPUT_CLASSES
            }),
            'content' : forms.Textarea(attrs={
            'class' : INPUT_CLASSES
            }),
        }
        labels = {
            'category':'Kategoria',
            'name':'Tytuł posta',
            'content':'Treść posta',
        }

class NewCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)
        widges = {
            'name' : forms.TextInput(attrs={
            'class' : INPUT_CLASSES
            }),
        }
        labels = {
            'name':'Nowa Kategoria',
        }