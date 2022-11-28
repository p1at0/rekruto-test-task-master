from django.http import HttpResponse
from django.shortcuts import redirect

def home(request):
    name = request.GET.get('name')
    message = request.GET.get('message')
    if name is None or message is None:
        return redirect('/?name=Rekruto&message=Давай дружить!')
    else:
        output = "<h2>Hello {0}! {1}</h2>".format(name, message)
        return HttpResponse(output)