from django.shortcuts import render, redirect
from .models import Post
from .forms import PostModelForm

# Create your views here.
def create(request):
    if request.method == "POST":
        # modelform을 통해서 Post를 만들어줌.
        form = PostModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("posts:create")
    else:
        # modelform을 전달해서 form을 보여줌.
        form = PostModelForm()
        return render(request, 'posts/create.html', {
            'form' : form
        })

