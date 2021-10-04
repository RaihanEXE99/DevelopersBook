from django.shortcuts import render,redirect
from .models import SDiscussion,DComment

# Create your views here.
def discussionList(request):
    all_discussion = SDiscussion.objects.filter()
    return render(request, 'discussion/discussionList.html',{
        'd' : all_discussion
    })

def inDiscussion(request,that_discussion_id):
    # print(that_discussion_id)
    that_discussion = SDiscussion.objects.get(id = that_discussion_id)
    comments = DComment.objects.filter(Tdiscussion = that_discussion)
    # print(that_discussion,comments)
    return render(request, 'discussion/inDiscussion.html',{
        'that_discussion' : that_discussion,
        'comments' : comments
    })

def replyDiscussion(request,that_discussion_id):
    if request.method == "POST":
        myComment = request.POST['myComment']
        Tdiscussion = SDiscussion.objects.get(id=that_discussion_id)
        ComUser = request.user
        done = DComment(Tdiscussion=Tdiscussion, ComUser=ComUser, myComment=myComment)
        done.save()
        print(Tdiscussion)
        return redirect('discussion:inDiscussion',that_discussion_id=that_discussion_id)
