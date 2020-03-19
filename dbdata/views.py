from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from dbdata.models import PG
from .forms import PGForm
from django.contrib.auth.decorators import login_required



@login_required
def insert_pg(request):
    if request.method == 'POST':
        pg=PG()
        pg.name= request.POST.get('pg_name')
        pg.headcount= request.POST.get('pg_hc')
        pg.pgtype= request.POST.get('pg_type')
        pg.city= request.POST.get('pg_city')
        pg.img= request.POST.get('pg_img')
        pg.rent= request.POST.get('pg_rent')
        pg.deposit= request.POST.get('pg_deposit')
        pg.desc= request.POST.get('pg_desc')
        pg.save()
        return HttpResponse('Data Inserted successfully')

    else:
        pg_form = PGForm()
    return render(request, 'insert-pg.html', {'form': pg_form})   


@login_required
def profile(request):
  return render(request, 'profile.html')


def search(request):
    model = PG
    query1 = request.GET.get('hc_q')
    query2 = request.GET.get('city_q')
    results = Post.objects.filter(Q(headcount__icontains=query1) & Q(city__icontains=query2))
    pages = pagination(request, results, num=1)
    context = {
        'items': pages[0],
        'page_range': pages[1],
    }
    return render(request, 'results.html')