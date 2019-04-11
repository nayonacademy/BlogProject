from django.forms import ModelForm,Textarea
from dashboard.models import BlogPost

class BlogPostForm(ModelForm):
    class Meta:
        model = BlogPost
        fields = '__all__'
        widgets = {
            'details': Textarea(attrs={'cols': 20, 'rows': 5}),
        }