from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .forms import CertificationForm, ArchiveForm
from .models import Record
from .serializers import WalkDataSerializer

class WalkDataViewSet(viewsets.ModelViewSet):
    serializer_class = WalkDataSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Record.objects.filter(user=self.request.user)

@login_required
def index(request):
    user = request.user
    # 사용자의 가장 최근 Record 객체 가져오기
    latest_record = Record.objects.filter(user=user).order_by('-create_at').first()

    if latest_record:
        record_id = latest_record.id
    else:
        record_id = None  # 기록이 없을 경우를 대비

    return render(request, 'Countapp/index.html', {
        'username': request.user.username,
        'record_id': record_id
    })


# def stop_tracking(request):
#     # 걷기 기록을 종료하고 인증샷 업로드 페이지로 리디렉션
#     latest_record = Record.objects.latest('id')
#     return redirect('countapp:upload_certification', record_id=latest_record.id)


def upload_walk_certification(request,record_id):
    record = get_object_or_404(Record, pk=(record_id+1))

    if request.method == 'POST':
        form = CertificationForm(request.POST, request.FILES)
        if form.is_valid():
            # Save CertificationForm and associate it with Record
            certification = form.save(commit=False)
            certification.record = record
            certification.save()
            return redirect('countapp:upload_archive', record_id=record_id)
    else:
        form = CertificationForm()

    # Calculate elapsed time in a readable format (hours, minutes, seconds)
    elapsed_seconds = record.msec / 1000
    # elapsed_time_formatted = format_time(elapsed_seconds)
    hours = int(elapsed_seconds // 3600)
    minutes = int((elapsed_seconds % 3600) // 60)
    seconds = int(elapsed_seconds % 60)

    # HTML에 시, 분, 초 형식의 걸은 시간을 전달
    return render(request, 'Countapp/upload_certification.html', {
        'form': form,
        'record': record,
        'hours': hours,
        'minutes': minutes,
        'seconds': seconds,
    })


def format_time(total_seconds):
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    return f"{int(hours)}:{int(minutes)}:{int(seconds)}"


def upload_success(request, record_id):
    record = get_object_or_404(Record, pk=record_id)
    return render(request, 'Countapp/upload_success.html', {'record': record})
@login_required
def upload_archive(request, record_id):
    record = get_object_or_404(Record, pk=record_id)
    if request.method == 'POST':
        form = ArchiveForm(request.POST, request.FILES)
        if form.is_valid():
            certification = form.save(commit=False)
            certification.record = record
            certification.user = request.user
            certification.save()
            return redirect('homeapp:home')
    else:
        form = CertificationForm()
    return render(request, 'Countapp/upload_archive.html', {
        'form': form,
        'record': record
    })