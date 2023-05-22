from django import forms
from django.http import request
from django.shortcuts import render
import json

import pyttsx3
 

# # converter.say("How Was Your Day?")
# # converter.runAndWait()


with open("web/static/web/data.json","r") as file:
    data = json.load(file)

eng = json.load(open("web/static/web/english.json"))

search = None

class getform(forms.Form):
    word = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Word', 'style': 'width: 400px;','class': 'form-input'}), label="Word")

def translateh(word):
    word = word.capitalize()
    if word in data:
        return data[word]
    elif word.lower() in data:
        return data[word.lower()]
    elif word.upper() in data:
        return data[word.upper()]
    else:
        return f"{word} is not Present in Dictionary"

def index(request):
    if request.method == "POST":
        ex = True
        form = getform(request.POST)
        if form.is_valid():
            word = form.cleaned_data["word"]
            search = translateh(word)
            pyttsx3.speak(search)

            if type(search) == list:
                    return render(request, "web/index.html", {
                    "form": getform(),
                    "result" : search,
                    "list" : ex
                })    
            else:
                return render(request, "web/index.html", {
                    "form": getform(),
                    "result" : search
                })
        else:
            return render(request, "web/index.html", {
                "form": form
            })
    else:
        return render(request , "web/index.html",{
            "form": getform()
        })


def engtranslate(word):
    word = word.lower()
    if word in eng:
        return eng[word]
    elif word.title() in eng:
        return eng[word.title()]
    elif word.upper() in eng:
        return eng[word.upper()]
    else:
        ex = word + " is not avaialable in the Dictionary"
        return ex

def english(request):
    if request.method == "POST":
        ex = True
        form = getform(request.POST)
        if form.is_valid():
            word = form.cleaned_data["word"]
            search = engtranslate(word)
            pyttsx3.speak(search)
            if type(search) == list:
                    return render(request, "web/english.html", {
                    "form": getform(),
                    "result" : search,
                    "list" : ex
                })
                    
            else:
                return render(request, "web/english.html", {
                    "form": getform(),
                    "result" : search
                })

        else:
            return render(request, "web/english.html", {
                "form": form
            })
    else:
        return render(request , "web/english.html",{
            "form": getform()
        })
    

def about(request):
    return render(request, "web/about.html")


