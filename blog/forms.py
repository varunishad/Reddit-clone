from django import forms
from django.db.models import fields
from .models import Comments, Post

class PostForm(forms.ModelForm):
  # edit_post = forms.BooleanField(widget=forms.HiddenInput, initial=True)
  class Meta:
    model = Post
    fields = ['title', 'description', 'image', 'url']
    widgets = {
      'title' : forms.TextInput(attrs={ 'class':'title w-100 py-2 px-3', 'type':"text", 'name':"title", 'placeholder':"Title", 'required': True, 'autofocus': True}),
      'description' : forms.Textarea(attrs={
         'id':"desc", 'class':'description w-100 px-3 py-2', 'placeholder':'Description (Optional)'
      }),
      # 'image' : forms.FileField(attrs={
      #    'required': False
      # }),
      'url' : forms.Textarea(attrs={
        'id':"desc",'class':'link-area w-100 px-3 py-2','placeholder':'Link'
      })
    }

class DeletePost(forms.Form):
  delete_blog = forms.BooleanField(widget=forms.HiddenInput, initial=True)

class PostComment(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['comments']
        widgets = {
      'comments' : forms.Textarea(attrs={
         'id':"desc", 'class':'comment-field w-100 px-3 py-2', 'placeholder':'What are your thoughts?'
      })}

