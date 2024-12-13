from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from .models import Event
from .forms import CommentForm

# Create your views here.

class EventList(generic.ListView):
    queryset = Event.objects.filter(status=1).order_by('date')
    template_name = "event_list.html"
    paginate_by = 6


def event_detail(request, slug):
    """
    Display an individual :model:`events.Event`.

    **Context**

    ``event``
        An instance of :model:`events.Event`.

    **Template:**

    :template:`events/event_detail.html`
    """

    queryset = Event.objects.filter(status=1)
    event = get_object_or_404(queryset, slug=slug)
    comments = event.comments.all().order_by("-created_on")
    comment_count = event.comments.filter(approved=True).count()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.event = event
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
    )

    comment_form = CommentForm()

    return render(
        request,
        "events/event_detail.html",
        {
            "event": event,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        },
    )