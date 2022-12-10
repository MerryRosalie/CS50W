from django.shortcuts import render, redirect
from markdown import markdown
from django.http import HttpResponseRedirect
from django.urls import reverse
from random import randint

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, name):
    entry = util.get_entry(name)
    if entry == None:
        entry = None
    else:
        entry = markdown(entry)
    return render(request, "encyclopedia/entry.html", {
        "name" : name,
        "entry" : entry
    })

def search(request):
    if request.method == "GET":
        return redirect("encyclopedia:index")
    else:
        q = request.POST.get('q').lower()
        similar = []
        for entry in util.list_entries():
            if q == entry.lower():
                return redirect("encyclopedia:entry", name = q)
            if q in entry.lower():
                similar.append(entry)
        return render(request, "encyclopedia/search.html", {
            "entries" : similar,
            "q": q
        })

def create(request):
    if request.method == "GET":
        return render(request, "encyclopedia/create.html")
    else:
        title = request.POST.get("title").strip()
        content = request.POST.get("content").strip()
        if title == "" or content == "":
            return render(request, "encyclopedia/create.html", {
                "message" : "Please insert content to the empty field"
            })
        for entry in util.list_entries():
            if title.lower() == entry.lower():
                return render(request, "encyclopedia/create.html", {
                    "message" : "The content has already exist."
                })
        util.save_entry(title, content)
        return redirect("encyclopedia:entry", name = title)

def edit(request, name):
    content = util.get_entry(name.strip())
    if content == None:
        return render(request, "encyclopedia/edit.html", {
            'message': "404 Not Found"
        })

    if request.method == "POST":
        title = request.POST.get("title").strip()
        content = request.POST.get("content").strip()
        if title == "" or content == "":
            return render(request, "encyclopedia/create.html", {
                "message" : "Please insert content to the empty field"
            })
        util.save_entry(title, content)
        return redirect("encyclopedia:entry", name = title)
    
    return render(request, "encyclopedia/edit.html", {
        "name" : name,
        "content" : content
    })

def random(request):
    entries = util.list_entries()
    name = entries[randint(0, len(entries)-1)]
    return redirect("encyclopedia:entry", name = name)