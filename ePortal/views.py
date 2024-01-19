from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Notification, PhoneNumber, Address, JobTitle, PersonalInfo, EtatInfo, PayList


def test_index(request):
    return render(request, 'index.html')

#def test_login(request):
#    return render(request, 'login.html')

# @login_required
# def test_profile(request):
#     return render(request, 'profile.html')
@login_required
def test_form(request):
    return render(request, 'form.html')

@login_required
def get_notifications(request):
    user = request.user
    notifications = Notification.objects.filter(user=user)
    notifications_data = [{'content': notification.content} for notification in notifications]
    return JsonResponse({'notifications': notifications_data})

@login_required
def test_profile(request):
    phone_number = PhoneNumber.objects.filter(user=request.user).first()
    address = Address.objects.filter(user=request.user).first()
    job_title = JobTitle.objects.filter(user=request.user).first()
    personal_info = PersonalInfo.objects.filter(user=request.user).first()

    pesel = personal_info.pesel if personal_info else None
    birth_date = personal_info.birth_date if personal_info else None

    etat_info = EtatInfo.objects.filter(user=request.user).first()

    etat = etat_info.etat if etat_info else None
    etat_to = etat_info.etat_to if etat_info else None
    etat_form = etat_info.etat_form if etat_info else None

    pay_list = PayList.objects.filter(user=request.user).first()
    second_pay_list_info = PayList.objects.filter(user=request.user).exclude(id=pay_list.id).first()

    korekta = pay_list.korekta if pay_list else None
    kwota = pay_list.kwota if pay_list else None
    data_wyp = pay_list.data_wyp if pay_list else None

    # Debugowanie: Wyświetl w konsoli, co jest przekazywane do szablonu2
    print("DEBUG: phone_number w widoku:", phone_number)
    print("DEBUG: address w widoku:", address)
    print("DEBUG: job_title w widoku:", job_title)
    print("DEBUG: pesel w widoku:", pesel)
    print("DEBUG: birth_date w widoku:", birth_date)
    print("DEBUG: etat w widoku:", etat)
    print("DEBUG: etat_to w widoku:", etat_to)
    print("DEBUG: etat_form w widoku:", etat_form)
    print("DEBUG: korekta w widoku:", korekta)
    print("DEBUG: kwota w widoku:", kwota)
    print("DEBUG: data_wyp w widoku:", data_wyp)
    print("DEBUG: second_pay_list_info.korekta - dla kazdej wartosci zadziala/ w widoku:", second_pay_list_info.korekta)

    return render(request, 'profile.html', {'phone_number': phone_number, 'address': address, 'job_title': job_title, 'pesel': pesel, 'birth_date': birth_date, 'etat': etat, 'etat_to': etat_to, 'etat_form': etat_form, 'korekta': korekta, 'kwota': kwota, 'data_wyp': data_wyp, 'second_korekta': second_pay_list_info.korekta, 'second_kwota': second_pay_list_info.kwota, 'second_data_wyp': second_pay_list_info.data_wyp})