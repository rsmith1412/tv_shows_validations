from django.shortcuts import render, redirect
from apps.tv_shows_app.models import *
from django.contrib import messages

# Create your views here.
def index(request):
    context = {"shows": Show.objects.all()}
    return render(request, "tv_shows_app/index.html", context)

def new_show(request):
    if request.method == "GET":
        return render(request, "tv_shows_app/new_show.html")
    if request.method == "POST":
        errors = Show.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect("/shows/new")
        else:
            title = request.POST["title"]
            network = request.POST["network"]
            rel_date = request.POST["rel_date"]
            desc = request.POST["desc"]
            new_show = Show.objects.create(title=title, network=network, rel_date=rel_date, desc=desc)
            return redirect("/shows/" + str(new_show.id))

def show_show(request, id):
    context = {"show": Show.objects.get(id=id)}
    return render(request, "tv_shows_app/show_show.html", context)

def edit_show(request, id):
    if request.method == "GET":
        context = {"show": Show.objects.get(id=id)}
        return render(request, "tv_shows_app/edit_show.html", context)

    if request.method == "POST":
        errors = Show.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/shows/' + id + '/edit')
        else:
            edited_show = Show.objects.get(id=id)
            edited_show.title = request.POST["title"]
            edited_show.network = request.POST["network"]
            edited_show.rel_date = request.POST["rel_date"]
            edited_show.desc = request.POST["desc"]
            edited_show.save()
            messages.success(request, "Show successfully updated")
            return redirect("/shows/" + str(edited_show.id))

def delete_show(request, id):
    Show.objects.get(id=id).delete()
    return redirect("/shows")