from django.shortcuts import render, redirect
from .models import Board
# Create your views here.
def index(request):
    boards = Board.objects.order_by('-id')
    return render(request, 'boards/index.html', {
        'boards': boards
    })
    
def new(request):
    return render(request, 'boards/new.html')
    
def create(request):
    board = Board()
    board.title = request.POST.get('title')
    board.content = request.POST.get('content')
    board.save()
    return redirect('boards:detail', board.pk)

def detail(request, pk):
    board = Board.objects.get(pk=pk)
    return render(request, 'boards/detail.html', {
        'board': board
    })
    
def delete(request, pk):
    board = Board.objects.get(pk=pk)
    board.delete()
    return redirect('index')

def edit(request, pk):
    board = Board.objects.get(pk=pk)
    return render(request, 'boards/edit.html', {
        'board': board
    })

def update(request, pk):
    board = Board.objects.get(pk=pk)
    board.title = request.POST.get('title')
    board.content = request.POST.get('content')
    board.save()
    return redirect('boards:detail', board.pk)








