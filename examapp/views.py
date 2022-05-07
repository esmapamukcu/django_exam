from django.shortcuts import render, HttpResponse
from .models import Ogrenci
import sqlite3
from django.contrib import messages
from django.db import connection


#connection = sqlite3.connect("db.sqlite3",check_same_thread=False)
cursor = connection.cursor()

# Create your views here.
def home(request):
    return render(request,'home.html', {})

def post_create(request):
    return HttpResponse("Post oluşturuluyor")

def form_create(request):
    if request.method == "POST":
        if request.POST.get('fname') and request.POST.get('lname') and request.POST.get('bolum') and request.POST.get('tckn'):
            kayit = Ogrenci()
            kayit.ad = request.POST.get('fname')
            kayit.soyad = request.POST.get('lname')
            kayit.bolum = request.POST.get('bolum')
            kayit.tckn = request.POST.get('tckn')

            try:
                kayit.save()
                messages.success(request, 'Kayıt Başarılı!' + kayit.ad + ' ' + kayit.soyad + ' kaydedildi.')
            except:
                messages.error(request, 'Kayıt işlemi başarısız!')

            return render(request, 'form.html')
    else:
        return render(request, 'form.html')

def not_hesapla(request):
    if request.method == "POST":
        if request.POST.get('tckn') and request.POST.get('vize') and request.POST.get('final'):
            kolon = request.POST.get('tckn')
            kayit = Ogrenci.objects.get(tckn=kolon)


            kayit.vize = float(request.POST.get('vize'))
            kayit.final = float(request.POST.get('final'))

            kayit.ortalama = ortalama_hesapla(kayit.vize,kayit.final)
            kayit.harfnotu = harf_hesapla(kayit.ortalama)

            kayit.save()
            messages.success(request, 'Güncelleme Başarılı!  Ortalamanız: ' + str(kayit.ortalama) + ' Harf notunuz: ' + kayit.harfnotu)
            return render(request, 'nothesaplama.html')
    else:
        return render(request, 'nothesaplama.html')

def ortalama_hesapla(vize, final):
    ortalama = float((vize * 0.4) + (final * 0.6))
    return  ortalama

def harf_hesapla(ortalama):
    if 100 >= ortalama >= 90:
        return 'AA'
    elif ortalama >= 80:
        return 'BB'
    elif ortalama >= 70:
        return 'CC'
    elif ortalama >= 60:
        return 'DD'
    elif 0 <= ortalama >= 50:
        return 'FF'


