# from django.shortcuts import render

# # Create your views here.



# from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
# from .models import Tweet

# @login_required
# def home(request):
#     if request.method == 'POST':
#         content = request.POST.get('content')
#         if content:
#             Tweet.objects.create(user=request.user, content=content)
#             return redirect('home')
#     tweets = Tweet.objects.all().order_by('-created_at')
#     return render(request, 'tweets/home.html', {'tweets': tweets})


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Tweet

@login_required
def home(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            Tweet.objects.create(user=request.user, content=content)
            return redirect('home')
    tweets = Tweet.objects.all().order_by('-created_at')
    return render(request, 'tweets/home.html', {'tweets': tweets})
