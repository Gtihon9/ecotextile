from django.shortcuts import render, get_object_or_404
from .models import Document
from django.http import FileResponse

def docs_list(request):
    object_list = Document.objects.all()
    return render(request,'docs/post/list.html', {'docs': object_list})

def doc_view(request, pk):
    doc = get_object_or_404(Document, pk=pk)
    return FileResponse(doc.file.open(mode='rb'))
