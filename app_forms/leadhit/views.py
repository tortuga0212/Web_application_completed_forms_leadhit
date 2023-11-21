from django.http import HttpResponse
from django.shortcuts import render

from .forms import *
from .models import *

def main(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data.get("date")
            phone = form.cleaned_data.get("phone")
            email = form.cleaned_data.get("email")
            for id in template_db:
                name = []
                itog = []
                coincidence = 0
                for values in id.values():
                    itog.append(values)
                    if coincidence == 0:
                        for values in itog:
                         if values == str(date):
                            coincidence += 1
                            break
                        else:
                            continue
                    elif coincidence == 1:
                        circle = 0
                        for values in itog:
                            if values == phone:
                                coincidence += 1
                                break
                            elif circle < 1:
                                circle += 1
                                continue
                            else:
                                return render(request, 'get_form.html', {'title': 'Получение формы', 'name': 'Ничего не нашли'})
                    elif coincidence == 2:
                        circle = 0
                        for values in itog:
                            if circle < 3:
                                if values == email:
                                    name.append(list(id.values())[4])
                                    list_name = ''.join(name)
                                    return render(request, 'get_form.html', {'title': 'Получение формы',
                                                                      'name': f'Имя шаблона формы: {list_name}'})
                                else:
                                    circle += 1
                                    continue
                            else:
                                return render(request, 'get_form.html', {'title': 'Получение формы', 'name': 'Ничего не нашли'})
    else:
        form = MyForm()
    return render(request, 'index.html', {'title': 'Главная страница', 'form': form, 'info': 'Сравнение существующих пользователей'})

def get_form(request):
    name = ''
    return render(request, 'get_form.html', {'title': 'Получение формы', 'id': id})