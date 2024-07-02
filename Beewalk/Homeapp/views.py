# from datetime import timedelta, datetime
#
# from django.db.models import Sum
# from django.shortcuts import render
#
# # Create your views here.
# # homeapp/views.py
# from django.shortcuts import render
# from django.contrib.auth.decorators import login_required
# from django.utils import timezone
#
# from Countapp import models
# from Countapp.models import Record
# from Accountapp.models import Member
#
# @login_required
# def home(request):
#     user = request.user
#     end_date = timezone.now()
#     start_date = end_date - timedelta(days=30)
#
#     # 30일 동안의 기록을 가져와서 합산
#     records = Record.objects.filter(user=user, create_at__range=(start_date, end_date))
#     total_distance = records.aggregate(total_distance=Sum('distance'))['total_distance'] or 0
#
#     year = request.GET.get('year', end_date.year)
#     month = request.GET.get('month', end_date.month)
#
#     start1_date = datetime(year=int(year), month=int(month), day=1)
#     if int(month) == 12:
#         end1_date = datetime(year=int(year) + 1, month=1, day=1)
#     else:
#         end1_date = datetime(year=int(year), month=int(month) + 1, day=1)
#
#     # 선택한 월의 기록을 필터링
#     records1 = Record.objects.filter(user=user, create_at__range=(start1_date, end1_date))
#     records_by_date = {}
#     for record in records1:
#         date = record.create_at.date()
#         if date not in records_by_date:
#             records_by_date[date] = 0
#         records_by_date[date] += round(record.distance,1)
#     print(records_by_date)
#
#     context = {
#         'user': user,
#         'records': records,
#         'records_by_date': records_by_date,
#         'total_distance': round(total_distance, 1),
#         'year': year,
#         'month': month,
#     }
#     return render(request, 'homeapp/home.html', context)
# homeapp/views.py
from datetime import datetime, timedelta
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.db.models import Sum
from Countapp.models import Record
from Accountapp.models import Member


@login_required
def home(request):
    user = request.user
    end_date = timezone.now()
    start_date = end_date - timedelta(days=30)

    # 30일 동안의 기록을 가져와서 합산
    records = Record.objects.filter(user=user, create_at__range=(start_date, end_date))
    total_distance = records.aggregate(total_distance=Sum('distance'))['total_distance'] or 0

    year = request.GET.get('year', end_date.year)
    month = request.GET.get('month', end_date.month)

    start1_date = datetime(year=int(year), month=int(month), day=1)
    if int(month) == 12:
        end1_date = datetime(year=int(year) + 1, month=1, day=1)
    else:
        end1_date = datetime(year=int(year), month=int(month) + 1, day=1)

    # 선택한 월의 기록을 필터링
    records1 = Record.objects.filter(user=user, create_at__range=(start1_date, end1_date))
    records_by_date = {}
    for record in records1:
        date = record.create_at.date().day
        if date not in records_by_date:
            records_by_date[date] = 0
        records_by_date[date] += round(record.distance, 1)

    # 이번 달의 첫 번째 날짜의 요일을 계산
    first_day_of_month = start1_date.weekday()

    # 이번 달의 일수를 계산
    days_in_month = (end1_date - start1_date).days
    # 빈 칸의 수 계산
    empty_cells = first_day_of_month
    context = {
        'user': user,
        'records': records,
        'records_by_date': records_by_date,
        'total_distance': round(total_distance, 1),
        'year': year,
        'month': month,
        'empty_cells': range(empty_cells),
        'days_in_month': range(1, days_in_month + 1),
    }
    return render(request, 'homeapp/home.html', context)
