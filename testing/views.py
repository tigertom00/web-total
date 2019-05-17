from django.shortcuts import render, redirect, reverse, get_object_or_404
from .forms import TestImgForm, TestBlogForm
from . import models


def testimg(request):
    if request.method == 'POST':
        testform = TestImgForm(request.POST, request.FILES)
        if testform.is_valid:
            testform.save()
            return redirect(reverse('testing'))
    testimg = models.TestImg.objects.all()
    testform = TestImgForm()
    context = {
        'testform': testform,
        'testimg': testimg,
    }
    return render(request, 'testimg.html', context)


def testblog_c(request):
    if request.method == 'POST':
        testform = TestBlogForm(request.POST, request.FILES)
        if testform.is_valid:
            testform.save()
            return redirect(reverse('testblog'))
    testform = TestBlogForm()
    context = {
        'testform': testform,
    }
    return render(request, 'testblog_c.html', context)


def testblog_l(request):
    blogs = models.TestBlog.objectes.all()
    context = {
        'blogs': blogs
    }
    return render(request, 'testblog_l.html', cotext)


def testblog(request, blog_id):
    blog = get_object_or_404(models.TestBlog, blog_id=blog_id)
    context = {
        'blog': blog,
    }
    return render(request, 'testblog.html', context)
