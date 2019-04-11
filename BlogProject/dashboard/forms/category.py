from django.forms import ModelForm,Textarea
from dashboard.models import Category

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        widgets = {
            'category_description': Textarea(attrs={'cols': 20, 'rows': 5}),
        }