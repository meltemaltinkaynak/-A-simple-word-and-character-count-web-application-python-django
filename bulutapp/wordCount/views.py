# from django.http.response import HttpResponse

from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, "wordCount/index.html")


def wordtxt(request):
    return render(request, "wordCount/wordtxt.html")


def wc(request):
    return render(request, "wordCount/wc.html")


# wordcounter
from django.http import JsonResponse

def count(request):
    if request.method == 'POST':
        text = request.POST.get('text', '')
        char_count = len(text)
        word_count = len(text.strip().split())
        return JsonResponse({'char_count': char_count, 'word_count': word_count})
    return JsonResponse({'error': 'Invalid request method'}, status=400)


#file word count
from django.shortcuts import render, redirect
from .forms import FileUploadForm
from .models import UploadedFile
import docx

def wordcount_details(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Dosya yüklendikten sonra kelime sayısını hesaplamak için count_words fonksiyonunu çağır
            return count_words(request)
    else:
        form = FileUploadForm()
    return render(request, 'wordCount/filewordCounter.html', {'form': form})


def count_words(request):
    last_file = UploadedFile.objects.latest('uploaded_at')
    file_path = last_file.file.path

    print("File path:", file_path)  # Dosya yolunu kontrol et

    if file_path.endswith('.txt'):
        with open(file_path, 'r') as file:
            text = file.read()
        print("Text content:", text)  # Metni kontrol et
    elif file_path.endswith('.docx'):
        doc = docx.Document(file_path)
        text = '\n'.join([para.text for para in doc.paragraphs])
        print("Text content:", text)  # Metni kontrol et
    else:
        return render(request, 'wordCount/error.html', {'error_message': 'Unsupported file format'})
    
    word_count = len(text.split())
    print("Word count:", word_count)  # Kelime sayısını kontrol et

    return render(request, 'wordCount/wc.html', {'word_count': word_count})
