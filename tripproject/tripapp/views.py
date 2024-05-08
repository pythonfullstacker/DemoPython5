# from django.http import HttpResponse
# from django.shortcuts import render
#
# from .models import place
# from .models import team
# # Create your views here.
# def demo(request):
#      obj=place.objects.all()
#      return render(request,"index.html",{'result':obj})
#
#      obj1=team.objects.all()
#      return render(request,"index.html",{'result1':obj1})

#   def register(request):
#   return render(request,"register.html")
#
# def contact(request):
#  return  HttpResponse("CONTACT HERE")


from django.shortcuts import render
from .models import place, team # You can import multiple models in one line

# Create your views here.
def demo(request):
# You can pass multiple querysets to the same template
    return render(request, "index.html", {'result': place.objects.all(), 'result1': team.objects.all() })