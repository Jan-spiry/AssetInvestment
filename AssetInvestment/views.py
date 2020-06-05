from django.shortcuts import render
import csv,json
# Create your views here.
def advantage(request):
    return render(request, 'advantage.html', locals())
def index(request):
    return render(request, 'index.html', locals())
def combination(request):
    return render(request, 'combination.html', locals())



def detail(request):
    with open('static/strategy_data/Follow_Loser.csv', 'r') as f:
        reader = csv.DictReader(f)
        follow_loser = [dict(row) for row in reader]
    with open('static/strategy_data/Follow_Winner.csv', 'r') as f:
        reader = csv.DictReader(f)
        follow_winner= [dict(row) for row in reader]
    with open('static/strategy_data/PG_Dense.csv', 'r') as f:
        reader = csv.DictReader(f)
        pg = [dict(row) for row in reader]
    with open('static/strategy_data/UCRP.csv', 'r') as f:
        reader = csv.DictReader(f)
        # ucpr = [{row['Date']:(float)(row['Pr'])} for row in reader]
        ucpr=[dict(row) for row in reader]
    with open('static/strategy_data/PG_Dense.csv', 'r') as f:
        reader = csv.DictReader(f)
        pg_change = ([dict(row) for row in reader])
        pg_now=pg_change[-1]
    return render(request,"detail.html",locals());