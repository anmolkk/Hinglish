# import json

# with open("data.json","r") as file:
#     data = json.load(file)

# search = None

# word = input("Enter Hinglish Word: ")
# word = word.capitalize()
# if word in data:
#     search = data[word]
#     print(search)
# else:
#     print("Error in Code")

from django import forms
from .models import *

class suggest_form(forms.ModelForm):
    class Meta:
        model = suggest
        fields = "__all__"
        
class getform(forms.Form):
    word = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Word', 'style': 'width: 400px;','class': 'form-input'}),label="Word")