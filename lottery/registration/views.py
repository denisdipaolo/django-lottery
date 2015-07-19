from django.shortcuts import render

from .forms import UserForm

# Create your views here.
def registration(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            registered = True
    else:
        user_form = UserForm()

    return render(request, 'registration/registration.html', {
        'user_form': user_form, 
        'registered': registered
    })