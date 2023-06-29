from django import forms
from .forms import *
from django.shortcuts import render, redirect
import json
from django.contrib import messages
# import pyttsx3

# import gtts  
# from playsound import playsound  


with open("web/static/web/data.json","r") as file:
    data = json.load(file)

eng = json.load(open("web/static/web/english.json"))

search = None

def find_matching_keys(dict, value):
    matching_keys = []
    for key in dict:
        if value in key.capitalize():
            matching_keys.append(key)
        elif value.capitalize() in key:
            matching_keys.append(key)

    if not matching_keys == []:
        if len(matching_keys) == 1:
            return matching_keys[0]
        else:
            return matching_keys[0],matching_keys[1]
    else:
        return None

def translateh(word):
    word = word.capitalize()
    if word in data:
        return data[word]
    elif word.lower() in data:
        return data[word.lower()]
    elif word.upper() in data:
        return data[word.upper()]
    else:
        return None

def index(request):
    if request.method == "POST":
        form = getform(request.POST)
        if form.is_valid():
            word = form.cleaned_data["word"]
            search = translateh(word)
            if search is None:
                suggested = find_matching_keys(data, word)
                messages.info(request, f"{word} is not Present in Hinglish Dictionary")   
                return render(request, "web/index.html", {
                    "form": getform(),
                    "result" : search,
                    "word":word,
                    "suggest":suggested,
                })  

            return render(request, "web/index.html", {
                "form": getform(),
                "result" : search,
                "word":word
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
        return None

def english(request):
    if request.method == "POST":
        form = getform(request.POST)
        if form.is_valid():
            word = form.cleaned_data["word"]
            search = engtranslate(word)
            if search is None:
                suggested = find_matching_keys(eng, word)
                messages.info(request, f"{word} is not Present in English Dictionary") 
                return render(request, "web/index.html", {
                    "form": getform(),
                    "result" : search,
                    "word":word,
                    "suggest":suggested,
                })  
            return render(request, "web/english.html", {
                "form": getform(),
                "result" : search,
                "word":word
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

def error_404(request):
    path = request.path
    return render(request, "web/404.html",{
        "path":path
    })


def suggestion(request):
    if request.method == "POST":
        form = suggest_form(request.POST)
        form.save()
        return redirect("hinglish")
    else:
        suggestform = suggest_form()
        return render(request, "web/suggestion.html", {
            "suggest":suggestform
        })
    
def feedback(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        subject = request.POST["subject"]
        message = request.POST["message"]
        feedback = Feedback(Name = name, Email = email, Subject = subject, Message = message)
        feedback.save()
        return redirect("hinglish")
    return render(request, "web/feedback.html")