from django.shortcuts import render
from django.http import HttpResponse
# from django.utils import simplejson
from .models import Post


def index(request):
    return render(request, 'blog/index.html')

# posts = [
#     {'author': 'Milen',
#      'title': 'Otneseni ot vihara',
#      'content': 'Nema nachin',
#      'date_posted': 'Oct 25, 2019'
#      },
#     {'author': 'Vask',
#      'title': 'Slabost',
#      'content': 'Full text content here',
#      'date_posted': 'Nov 25, 2019'
#     },
#     {'author': 'Poslednia voin',
#      'title': 'Na oryjie',
#      'content': 'Text of the book',
#      'date_posted': 'Nov 25, 2011'
#     }
# ]


def business(request):
    context = {
        # 'posts': posts
        'posts': Post.objects.all()
    }
    return render(request, 'blog/business.html', context)


# def business(request):
#     return render(request, 'blog/business.html')



# def gsonback(request):
#     context = {
#             {'author': 'Milen',
#              'title': 'Otneseni ot vihara',
#              'content': 'Nema nachin',
#              'date_posted': 'Oct 25, 2019'
#              },
#             {'author': 'Vask',
#              'title': 'Slabost',
#              'content': 'Full text content here',
#              'date_posted': 'Nov 25, 2019'
#             },
#             {'author': 'Poslednia voin',
#              'title': 'Na oryjie',
#              'content': 'Text of the book',
#              'date_posted': 'Nov 25, 2011'
#             }
#     }
#     # return HttpResponse(simplejson.dumps(context), mimetype='application/json')
#      return render(request, 'blog/business.html', context)



