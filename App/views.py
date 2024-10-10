from django.shortcuts import render
from django.http import HttpResponse

def calculate(request):
    if request.method == "POST":
        a = request.POST.get("a")  # Kiritilgan qiymatni olish
        b = request.POST.get("b")
        c = request.POST.get("Amal")
        
        try:
            a = float(a)
            b = float(b)

            if c == "+":
                Natija = a + b
            elif c == "-":
                Natija = a - b
            elif c == "*":
                Natija = a * b
            elif c == "/":
                if b != 0:
                    Natija = a / b
                else:
                    Natija = "Nolga bo'lish mumkin emas!"
            else:
                Natija = "Noto'g'ri amal kiritildi"
        except ValueError:
            Natija = "Noto'g'ri son kiritildi"

        # Natijani to'g'ri formatda qaytarish
        return render(request, "home.html", {'result': Natija})

    # Agar POST so'rovi bo'lmasa
    return render(request, 'home.html')