from django.shortcuts import render

def classroom(request):
    return render(request, 'classroom.html',{'Banner' : "HomePage", 'BannerHref' : ""})

def details_classroom(request, idClasse = 0):
    return render(request, 'details_classroom.html',{'Banner' : "HomePage", 'BannerHref' : ""})