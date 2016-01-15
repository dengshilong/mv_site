from .models import Post

def get_page(request):
    page = request.GET.get('page', '') 
    if not page:
        page = 1 
    return page
