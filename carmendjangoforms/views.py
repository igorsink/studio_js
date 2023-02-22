from django.shortcuts import render
from .forms import userReg
from .forms import members_Reg


def Reg(request):
    submit_button = request.POST.get("carmen")
    name = ''
    email = ''
    password = ''

    reg_form = userReg(request.POST or None)
    if reg_form.is_valid():
        name = reg_form.cleaned_data.get("name")
        email = reg_form.cleaned_data.get("email")
        password = reg_form.cleaned_data.get("password")

    context = {'reg_form': reg_form, 'name': name, 'email': email, 'submit_button': submit_button}
    return render(request, 'register.html', context)


def members(request):
    submit_button = request.POST.get("members")
    name = ''
    age = ''
    phone = ''
    city = ''
    country = ''

    reg_members_form = members_Reg(request.POST or None)
    if reg_members_form.is_valid():
        name = reg_members_form.cleaned_data.get("name")
        age = reg_members_form.cleaned_data.get("age")
        phone = reg_members_form.cleaned_data.get("phone")
        city = reg_members_form.cleaned_data.get("city")
        country = reg_members_form.cleaned_data.get("country")

    context = {'reg_members_form': reg_members_form,
               'name': name,
               'age': age,
               'phone': phone,
               'city': city,
               'country': country,
               'submit_button': submit_button}
    return render(request, 'members.html', context)
