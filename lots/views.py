from django.shortcuts import render
from .models import Lots

def lot_list(request):
    lots_list=Lots.objects.all()
    context={'lots':lots_list}
    return render(request,'lots/liste_lots.html',context )


def lot_detail(request,id):
    lot_list=Lots.objects.get(id=id)
    context={'lots':lot_list}
    return render(request,'lots/detail_lot.html',context )

  
