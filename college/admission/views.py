from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
'''def welcome(request):
    return HttpResponse("welcome")'''
'''def colleges(request,clg):
    msg=""
    if clg=="1":
        msg="Welcome Pujitha"
    elif clg=="2":
        msg="Welcome Teja Sree"
    else:
        msg="Sorry you entered wrong number"
    return HttpResponse(msg)'''
'''def home1(request):
    return render(request,"admission/home1.html")'''
'''def home2(request):
    return render(request,"admission/home2.html")'''

'''def home3(request):
    colleges_list = ['SVEW', 'VIT', 'BVRICE']
    return render(request, 'admission/home3.html', {'colleges': colleges_list})'''
'''def home4(request):
    students_data = [
        {"s_no": 1, "name": "Pujitha", "branch": "IT", "age": 20},
        {"s_no": 2, "name": "Sai", "branch": "CSE", "age": 17},
        {"s_no": 3, "name": "Venkat", "branch": "AGRITECH", "age":15 },
    ]
    return render(request, 'admission/home4.html', {'students': students_data})
def home5(request):
    return render(request,"admission/home5.html")
'''


