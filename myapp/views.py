from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.urls import reverse_lazy
from .models import Announcement


def index(request):
    """Главная"""
    return render(request, 'index.html')


class AnnouncementList(ListView):
    """Все объявления"""
    model = Announcement
    template_name = 'announcements.html'
    ordering = 'date_create'
    context_object_name = 'announcements'


class AnnouncementDetail(DetailView):
    """Объявление"""
    model = Announcement
    template_name = 'announcement.html'
    context_object_name = 'announcement'


class AnnouncementCreate(CreateView):
    """Создание объявления"""
    model = Announcement
    template_name = 'create.html'
    fields = ['author', 'header', 'category', 'content']
    success_url = reverse_lazy('announcements')


class AnnouncementDelete(DeleteView):
    """Удаление объявления"""
    model = Announcement
    template_name = 'delete.html'
    success_url = reverse_lazy('announcements.html')


def work_room(request):
    context = {
        'posts': Announcement.objects.filter(author=request.user)
    }
    return render(request, 'work_room.html', context)
