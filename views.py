from django.http import HttpResponse
from execute.forms import InputForm
#import render

def index(request):
    return HttpResponse("<h1> <center> Calculator </center> </h1>")
   #return HttpResponse("<h1> <center> Calculator </center> <form> <input type="text" value="num"> </form> </h1>")

def input(request):
    if request.method == "POST":
        MyInputForm = InputForm(request.POST)

    else:
        MyInputForm = InputForm()

    return render(request,"input.html")
