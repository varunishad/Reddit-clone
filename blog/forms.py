from django import forms
from django.db.models import fields
from .models import Post

class PostForm(forms.ModelForm):
  # edit_post = forms.BooleanField(widget=forms.HiddenInput, initial=True)
  class Meta:
    model = Post
    fields = ['title', 'description', 'image', 'url']
    # widgets = {
    #   'title' : forms.CharField (attrs = { 'placeholder':"Title", 'required': True}),
    #   'description' : forms.Textarea(attrs = {
    #      'id':"desc", 'class':'description w-100 px-3 py-2', 'placeholder':'Description (Optional)'
    #   }),
    #   'image' : forms.ImageField(attrs = {
    #     'type':"file",'accept':"image/*", 'id':"fileupload"
    #   }),
    #   'url' : forms.CharField(attrs = {
    #     'id':"desc",'class':'link-area w-100 px-3 py-2','placeholder':'Link'
    #   })
    # }

class DeletePost(forms.Form):
  delete_blog = forms.BooleanField(widget=forms.HiddenInput, initial=True)


