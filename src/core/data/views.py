from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('<h1>Ona Api Consumption coming up</h1>')
