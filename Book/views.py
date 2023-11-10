
# from django.db.models import Q
# from .models import BookModel, Book_genres
# from django.core.paginator import Paginator
# from django.contrib import messages
# from django.shortcuts import render, redirect


# def bookinfo(request):
#     # Truy vấn dữ liệu từ mô hình 'BookModel'
#     books = BookModel.objects.all()
    
#     # Tạo một danh sách để lưu thông tin về sách và thể loại
#     book_info = []

#     for book in books:
#         # Truy vấn danh sách thể loại cho từng cuốn sách
#         genres = Book_genres.objects.filter(book=book)
        
#         # Tạo danh sách chứa tên các thể loại
#         genre_names = [genre.genre.name for genre in genres]

#         # Thêm thông tin về sách và thể loại vào danh sách 'book_info'
#         book_info.append({
#             'book': book,
#             'genres': genre_names,
#         })
    

#     # Trả về một trang web hiển thị dữ liệu
#     return render(request, 'bookinfo.html', {'book_info': book_info})

# def search(request):
#     search_query = request.POST.get('search_query', '')
#     results = []

#     if search_query:
#         results = BookModel.objects.filter(
#             Q(Title__icontains=search_query) |
#             Q(Authors__icontains=search_query) |
#             Q(Publisher__icontains=search_query) |
#             Q(book_genres__genre__name__icontains=search_query)
#         ).distinct()

#     if not results:
#         messages.info(request, 'Không tìm thấy kết quả.')
#         return redirect('bookinfo')
    
#     # Tạo một danh sách để lưu thông tin về sách và thể loại
#     book_info = []

#     for book in results:
#         # Truy vấn danh sách thể loại cho từng cuốn sách
#         genres = Book_genres.objects.filter(book=book)
        
#         # Tạo danh sách chứa tên các thể loại
#         genre_names = [genre.genre.name for genre in genres]

#         # Thêm thông tin về sách và thể loại vào danh sách 'book_info'
#         book_info.append({
#             'book': book,
#             'genres': genre_names,
#         })
        

#     return render(request, 'search.html', {'results': book_info, 'search_query': search_query})




# def book_filter(request):
#     author = request.POST.get('author', '')
#     publisher = request.POST.get('publisher', '')
#     language = request.POST.get('language', '')
    

#     books = BookModel.objects.all()

#     if author:
#         # Lọc dữ liệu gần đúng cho tác giả
#         books = books.filter(Q(Authors__icontains=author) | Q(Authors__icontains=author))

#     if publisher:
#         # Lọc dữ liệu gần đúng cho nhà xuất bản
#         books = books.filter(Q(Publisher__icontains=publisher) | Q(Publisher__icontains=publisher))

#     if language:
#         # Lọc dữ liệu gần đúng cho ngôn ngữ
#         books = books.filter(Q(Language__icontains=language) | Q(Language__icontains=language))

    
#     book_info = []

#     for book in books:
#         genres = Book_genres.objects.filter(book=book)
#         genre_names = [genre.genre.name for genre in genres]

#         book_info.append({
#             'book': book,
#             'genres': genre_names,
#         })

#     return render(request, 'filter.html', {'book_info': book_info})

# import local data
from rest_framework import viewsets, status
from rest_framework.pagination import PageNumberPagination
from .serializers import BookSerializer, GenresSerializer
from .models import Book, Genres, BookGenres
from django_filters import rest_framework as filters

class BookPagination(PageNumberPagination):
    page_size = 9
    page_size_query_param = 'page_size'
    max_page_size = 1000

class BookFilter(filters.FilterSet):
    class Meta:
        model = Book
        fields = ['id', 'title', 'subtitle', 'publisher', 'publication_date']

# create a viewset
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = BookPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = BookFilter
    
    def get_queryset(self):
        genre_id = self.request.query_params.get('genre_id', None)
        if genre_id is not None:
            book_id = BookGenres.objects.filter(genresid = genre_id)
            data = [obj.__dict__ for obj in book_id]
            data = [book['bookid'] for book in data]
            qs =  Book.objects.filter(id__in=data)
            return qs
        return Book.objects.all()
    

class GenresViewSet(viewsets.ModelViewSet):
    # define queryset
    queryset = Genres.objects.all()

    # specify serializer to be used
    serializer_class = GenresSerializer
    
    