import logging

from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages

from .forms import CommentCreateForm
from .models import Result
from .chat import *
from .clip import *

logger = logging.getLogger(__name__)


# Create your views here.
def index(request):
    return render(request, "index.html")


def result(request):
    return render(request, "result.html")


# ホームページのビュークラス
class IndexView(generic.FormView):
    template_name = "index.html"
    form_class = CommentCreateForm
    success_url = reverse_lazy("MainApp:result")

    def form_valid(self, form):
        form.save()
        # input = form["nanka"]
        # img -> clip
        # context = clip

        # for
        # context -> chat
        # responses = chat

        # responses -> result
        # セッションにresponsesを保存する
        messages.success(self.request, "解説を生成しました")
        return super().form_valid(form)


class ResultView(generic.TemplateView):
    model = Result
    template_name = "result.html"
    success_url = reverse_lazy("MainApp:index")

    # indexからresponsesを受け取る
    # セッションから取り出す
    # responses -> template
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["my_variable"] = "Hello, World!"
        return context