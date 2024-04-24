from .models import Constructor
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

#Обработчик форм
class ConstructorForm(ModelForm):
    class Meta:
        #Название класса модели
        model = Constructor
        #Поля из models
        fields = ['title','full_text','date']

        widgets = {
            'title': TextInput(attrs={
                'class':'form-title',
                'placeholder':'Название',
            }),
            'full_text': Textarea(attrs={
                'class': 'form-full-text',
                'placeholder': 'Полный текст',
            }),
            'date': DateTimeInput(attrs={
                'class': 'form-date',
                'placeholder': 'Дата',
            }),
        }