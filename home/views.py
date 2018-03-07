from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

def home(request):
    packages = [
	{'name':'dj-paypal', 'url': 'http://pypi.python.org/pypi/dj-paypal/0.6.0'},
	{'name':'aa_stripe', 'url': 'http://pypi.python.org/pypi/aa_stripe/0.4.1'},
	{'name':'django-paypal2', 'url': 'http://pypi.python.org/pypi/django-paypal2/1.0.2'},
	{'name':'django-shop-paypal', 'url': 'http://pypi.python.org/pypi/django-shop-paypal/0.0.1'},
	{'name':'djangoshop-paypal', 'url': 'http://pypi.python.org/pypi/djangoshop-paypal/0.2.1'},
    ]
    context = {
        'title': 'sgmagar-crowdbotics-69',
        'packages': packages
    }
    return render(request, 'home/index.html', context)
