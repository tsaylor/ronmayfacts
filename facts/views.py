from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from facts.models import Fact
from facts.forms import NewFactForm
import random
from datetime import datetime


def onepage(request):           # one page, one fact.  There can be only one.
    factoid = randomfact()
    return render_to_response('onepage.html', {'fact':factoid})

def main(request):              # site homepage
    factoid = randomfact()
    return render_to_response('home.html', context_instance=RequestContext(request, {'fact':factoid}))

def autoreload(request):
    factoid = randomfact()
    return render_to_response('autoreload.html', context_instance=RequestContext(request, {'fact':factoid}))
    

#def thanks(request):            # thanks page, confirmation for submitting facts, pics, or even comments?
#    return render_to_response('kthxbai.html', {})

# This one overloaded the random module.  It needs to be renamed.
#def random(request):            # display a random fact
#    return render_to_response('detail.html', {'factId':1})

def detail(request, fact_id):   # display a specified fact
    factoid = Fact.objects.get(id=fact_id)
    form = NewFactForm()
    return render_to_response('home.html', context_instance=RequestContext(request, {'fact':factoid, 'form':form}))

#def add(request):               # display form to add a fact
#    return render_to_response('add.html', {})

def submit(request):            # submission landing page, redirect back to their new content (with page anchors)
    if request.method == "POST":
        form = NewFactForm(request.POST)
        if form.is_valid():
            # insert fact in db
            newfactoid = Fact()
            newfactoid.name=request.POST['name']
            newfactoid.email=request.POST['email']
            newfactoid.factoid=request.POST['factoid']
            newfactoid.date_added= datetime.strftime(datetime.now(), "%Y-%m-%d %I:%M:%S")
            newfactoid.save()
            # Send them back to their fact on the homepage (this means fact permalinks)
            return HttpResponseRedirect('/facts/%d' % newfactoid.id)
            #return HttpResponseRedirect('/')
    else:
        form = NewFactForm()
    return render_to_response('submit.html', context_instance=RequestContext(request, {'form': form}))
        


#### helper functions
def randomfact():
    """Return a random fact object"""
    factlist = Fact.objects.all()
    factoid = factlist[random.randint(0, len(factlist)-1)]
    return factoid
