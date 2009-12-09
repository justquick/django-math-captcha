from django.shortcuts import render_to_response
from forms import Form

def form(request):
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            return render_to_response('form.html',{'m':'woo hoo'})
    else:
        form = Form()

    return render_to_response('form.html', {
        'form': form,
    })
