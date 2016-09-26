from django.shortcuts import render
from .models import Article
from form import MyModelForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.template.context_processors import csrf


from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.template import RequestContext


# from .workday import *
# from .forms import *
import datetime
from .models import *
from django.template import RequestContext

@csrf_exempt
def home_page(request):
   args = {}
   args.update(csrf(request))
   print "outsideeeeeeeeeeee"
   print "view executed"
   if request.method == 'POST':
       print"post method gets executed"
       form = MyModelForm(request.POST)
       if form.is_valid():
           data = form.save(commit=False)
           data.save()
           #return HttpResponseRedirect('/myidea/')
           my_articles = Article.objects.all()
           return render_to_response('new/hello.html', {'my_data': form, 'my_articles':my_articles})
           #return render_to_response("hello.html", args)


       else:

           print form.errors
   else:
       print "elseeeeeeeeeeeeee"
       form = MyModelForm()
       my_articles = Article.objects.all()
       #return render(request, 'hello.html', {'form': form})
       # return render_to_response('new/hello.html', {'my_data': form})
       return render_to_response('new/hello.html', {'my_data': form, 'my_articles':my_articles})