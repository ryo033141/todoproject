from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import TodoModel
from django.urls import reverse_lazy

class Todolist(ListView):
    # テンプレートのHTMLを指定
    template_name = 'list.html'
    # モデルを指定
    model = TodoModel

class TodoDetail(DetailView):
    # テンプレートのHTMLを指定
    template_name = 'detail.html'
    # モデルを指定
    model = TodoModel

class TodoCreate(CreateView):
    # テンプレートのHTMLを指定
    template_name = 'create.html'
    # モデルを指定
    model = TodoModel
    # 表示させるフィールドを指定
    fields = ('title','memo','priority','duedate')
    # 新規登録が完了すると、リスト画面に遷移する
    success_url = reverse_lazy('list')

class TodoDelete(DeleteView):
    # テンプレートのHTMLを指定
    template_name = 'delete.html'
    # モデルを指定
    model = TodoModel
    # 削除が完了すると、リスト画面に遷移する
    success_url = reverse_lazy('list')

class TodoUpdate(UpdateView):
    # テンプレートのHTMLを指定
    template_name = 'update.html'
    # モデルを指定
    model = TodoModel
    # 表示させるフィールドを指定
    fields = ('title','memo','priority','duedate')
    # 更新が完了すると、リスト画面に遷移する
    success_url = reverse_lazy('list')