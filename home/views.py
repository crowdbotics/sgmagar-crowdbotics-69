from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

def home(request):
    packages = [
	{'name':'djangoshop-paypal', 'url': 'http://pypi.python.org/pypi/djangoshop-paypal/0.2.1'},
    ]
    context = {
        'title': 'sgmagar-crowdbotics-69',
        'packages': packages
    }
    return render(request, 'home/index.html', context)
