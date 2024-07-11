from django.http import HttpResponse

def handler404(request,exception):
    return HttpResponse("<b>404: Page not Found!<b> <br><br><button onclick='' href='';> Go to Home page")