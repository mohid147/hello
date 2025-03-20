from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from hello.models import LogMessage
from hello.forms import LogMessageForm

# 🔹 Class-Based View with Login Required
@method_decorator(login_required, name='dispatch')
class HomeListView(ListView):
    model = LogMessage
    template_name = "hello/home.html"  # Ensure this template exists

# 🔹 Function-Based Views with Login Required
@login_required
def about(request):
    return render(request, "hello/about.html")

@login_required
def log_message(request):
    if request.method == "POST":
        form = LogMessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.log_date = timezone.now()
            message.save()
            return redirect("home")
    else:
        form = LogMessageForm()
    return render(request, "hello/log_message.html", {"form": form})

@login_required
def edit_message(request, pk):
    message = get_object_or_404(LogMessage, pk=pk)
    if request.method == "POST":
        form = LogMessageForm(request.POST, instance=message)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = LogMessageForm(instance=message)
    return render(request, "hello/edit_message.html", {"form": form})

@login_required
def delete_message(request, pk):
    message = get_object_or_404(LogMessage, pk=pk)
    if request.method == "POST":
        message.delete()
        return redirect("home")
    return render(request, "hello/delete_message.html", {"message": message})
