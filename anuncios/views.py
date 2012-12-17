# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response,  get_object_or_404
from django.core.urlresolvers import reverse
from django.template import RequestContext
from anuncios.models import Foto,Carro





def Reader(request):
  #return HttpResponse('eca')
 
  anuncios = Carro.objects.all()
  
  resposta = render_to_response('carros.eca', locals(), context_instance = RequestContext(request))
  resposta['Content-Type']="application/json"
  return resposta
  