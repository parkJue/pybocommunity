from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from ..forms import FileUploadForm
from ..models import FileUpload


@login_required(login_url='common:login')
def fileUpload(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        img = request.FILES["imgfile"]
        fileupload = FileUpload(
            title=title,
            content=content,
            imgfile=img,
        )
        fileupload.save()
        return redirect('pybo:index')
    else:
        fileuploadForm = FileUploadForm
        context = {
            'fileuploadForm': fileuploadForm,
        }
        return render(request, 'pybo/fileupload_form.html', context)