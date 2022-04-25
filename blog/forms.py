from django import forms
from .models import Post, Comments, Tags

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image']


class CreateCommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
                'rows': 6,
                 'cols': 40
                 }))
    
    class Meta:
        model = Comments
        fields = ['content']
    
    def __init__(self, *args, **kwargs):
        super(CreateCommentForm, self).__init__(*args, **kwargs)
        self.fields['content'].label = ''
        self.fields['content'].widget.attrs.update({
            'placeholder': 'Write a comment...',
            'class': 'form-control'
        })