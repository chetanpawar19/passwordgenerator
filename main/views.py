from django.shortcuts import render
from .passwordgeneratorlogic import passwordgeneration
from django.http import HttpResponse


def index(request):

    if request.method =='POST':
        no_of_passwords = int(request.POST['no_of_passwords'])

        user_combinations = request.POST.getlist('checks[]')

        if request.POST['custom_length'] == '':
            password_length = int(request.POST['dropdown_length'])
        else:
            password_length = int(request.POST['custom_length'])

        if user_combinations == []:
            password_list = passwordgeneration(no_of_passwords,password_length,['uppercase_letters','lowercase_letters','digits','special_characters'])
        else:
            password_list = passwordgeneration(no_of_passwords,password_length,user_combinations)
        return render(request, 'main/index.html', {'passwords':password_list})
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')