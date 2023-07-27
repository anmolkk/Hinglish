from .forms import *
from django.shortcuts import render, redirect
import json
from django.contrib import messages
from .methods import *
from django.http import HttpResponse


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
    recent = getrecentHinglish(request)
    if request.method == "POST":
        form = getform(request.POST)
        if form.is_valid():
            word = form.cleaned_data["word"]
            search = translateh(word)
            if search is None:
                suggested = find_matching_keys(data, word)
                messages.info(request, f"{word} is not Present in Hinglish Dictionary")   
                html = render(request, "web/index.html", {
                    "form": getform(),
                    "result" : search,
                    "word":word,
                    "suggest":suggested,
                    "recent":recent
                })
                setrecentHinglish(request,html,word.capitalize())
                return html
            
            html =  render(request, "web/index.html", {
                "form": getform(),
                "result" : search,
                "word":word,
                "recent":recent
            })
            setrecentHinglish(request,html,word.capitalize())
            return html
        else:
            return render(request, "web/index.html", {
                "form": form,
                "recent":recent
            })
    else:
        return render(request , "web/index.html",{
            "form": getform(),
            "recent":recent,
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
    recent = getrecentEnglish(request)
    if request.method == "POST":
        form = getform(request.POST)
        if form.is_valid():
            word = form.cleaned_data["word"]
            search = engtranslate(word)
            if search is None:
                suggested = find_matching_keys(eng, word.capitalize())
                messages.info(request, f"{word} is not Present in English Dictionary") 
                html = render(request, "web/index.html", {
                    "form": getform(),
                    "result" : search,
                    "word":word,
                    "suggest":suggested,
                    "recent":recent
                })
                setrecentEnglish(request,html,word.capitalize())
                return html
            html = render(request, "web/english.html", {
                "form": getform(),
                "result" : search,
                "word":word,
                "recent":recent
            })
            setrecentEnglish(request,html,word)
            return html
        
        else:
            return render(request, "web/english.html", {
                "form": form,
                "recent":recent
            })
    else:
        return render(request , "web/english.html",{
            "form": getform(),
            "recent":recent
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
        subject = 'Thank you For Sharing Your feedback at Hinglish Dictionary'
        message = f'Hi {name}, Thank you for Sharing You Valuable Feedback About Hinglish Dictionary with US. Please Stay Connect With US on Our Website. Hope You are Having a Great Time. You can Visit Our Website from Following Link. Hinglish Dictionary - https://hinglish.pythonanywhere.com'
        sendmail(subject, message, email)
        return redirect("hinglish")
    return render(request, "web/feedback.html")


# def AddHinglishWord(request):
#     with open("web/static/web/exmp.json",'r') as file:
#         ex = json.load(file)
#     if request.method == "POST":
#         form = suggest_form(request.POST)
#         word = form["word"]
#         meaning = form["meaning"]
#         ex[word] = meaning
#         with open("web/static/web/exmp.json", 'a') as js:
#             js.write(ex)
#             js.close()
#         return redirect("hinglish")
#     else:
#         suggestform = suggest_form()
#         return render(request, "web/suggestion.html", {
#             "suggest":suggestform
#         })