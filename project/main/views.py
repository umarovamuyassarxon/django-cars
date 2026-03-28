from django.shortcuts import render

from django.http import HttpRequest, HttpResponse



cars = [
    {'id':1, 'name': 'BMW', 'price':'55.0000$', 'year': 2025},
    {'id':2, 'name': 'Tesla Model 3', 'price':'35.0000$', 'year': 2024},
    {'id':3, 'name': 'Kia K5', 'price':'30.0000$', 'year': 2022},
    {'id':4, 'name': 'L9', 'price':'70.0000$', 'year': 2025},

]

def home(request:HttpRequest):
    context = {
        'cars': cars
    }
    return render(request, 'main/index.html', context)




def car_detail(request, car_id: int):
    for car in cars:
        if car.get('id') == car_id:
            context = {'car': car}
            return render(request, 'main/detail.html', context)
    return HttpResponse('Car Not Found', status=404)





def about(request:HttpRequest):
    return render(request, 'main/about.html')



