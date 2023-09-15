from django.shortcuts import render,redirect
from .models import Blogpost,Blogcomment
from django.contrib.auth.models import User
from django.contrib import messages
from blog.templatetags import extras
# Create your views here.
def bloghome(request,slug):
    # fetching all blogposts form the database
    myposts = Blogpost.objects.all().order_by('-time_stamp')
    
    return render(request,'blogtemps/index.html',{'mypost':myposts})
def blogpost(request,id):
    # geting the selected post from the list
    post = Blogpost.objects.filter(post_id = id)[0]
    post.blog_views = post.blog_views + 1
    post.save()
    comments = Blogcomment.objects.filter(post=post,parent = None)
    replies = Blogcomment.objects.filter(post=post).exclude(parent = None)
    repDict={}
    for comreply in replies:
        if comreply.parent.com_id not in repDict.keys():
            repDict[comreply.parent.com_id] = [comreply] 
        else:
            repDict[comreply.parent.com_id].append(comreply)
    Context = {'post':post,'comments':comments,'user':request.user,'repDict':repDict}
    return render(request,'blogtemps/blogpost.html',Context)

# Defining view for Comment API
def postComment(request):
    if request.method == 'POST':
        comment = request.POST.get('comment')
        user = request.user
        postid = request.POST.get('postid')
        commentid = request.POST.get('commentid')
        post = Blogpost.objects.get(post_id = postid)
        if commentid == "":
            comments = Blogcomment(comment = comment,user = user,post = post)
            comments.save()
            messages.success(request,'Your comment has been posted successfully')
        else:
            parent = Blogcomment.objects.get(com_id= commentid)
            comments = Blogcomment(comment = comment,user = user,post = post,parent = parent)
            comments.save()
            messages.success(request,'Your repl has been posted successfully')
        
    
    return redirect(f"/blog/blogpost/{post.post_id}")
    