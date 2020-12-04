from django.shortcuts import render, redirect
from . models import Topic
from . forms import TopicForm, EntryForm

# Create your views here.


def index(request):
    """学习笔记的主页"""
    return render(request, 'website/index.html')


def topics(request):
    """显示所有主题"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'website/topics.html', context)


def topic(request, topic_id):
    """显示单一主题"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'website/topic.html', context)


def new_topic(request):
    """添加一个新主题"""
    if request.method != 'POST':
        form = TopicForm()
        # 未提交数据：创建一个新表单
    else:
        # POST提交的数据，对数据进行处理
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('website:topics')
    # 显示空白或者不可用表单
    context = {'form': form}
    return render(request, 'website/new_topic.html', context)


def new_entry(request, topic_id):
    """添加一个新的条目"""
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        # 创建空表单
        form = EntryForm()
    else:
        # 提交数据
        form =EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('website:topic', topic_id=topic_id)
    context = {'topic':topic,'form':form}
    return render(request, 'website/new_entry.html', context)