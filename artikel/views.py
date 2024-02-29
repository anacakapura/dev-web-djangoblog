from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Artikel
from .forms import ArtikelForm

# Create your views here.

class ArtikelPerKategori():
    model = Artikel

    def get_latest_artikel(self):
        kategori_list = self.model.objects.values_list('kategori', flat=True).distinct() #Menggunakan values_list untuk mengambil semua data pada field kategori
        queryset = [] #[] digunakan untuk mengabil beberapa data

        for kategori in kategori_list:
            artikel = self.model.objects.filter(kategori=kategori).latest('published')
            queryset.append(artikel) #Memasukan data yang difilter ke queryset        
        
        return queryset


class ArtikelListView(ListView):
    model = Artikel
    template_name = "artikel/artikel_list.html"
    context_object_name = 'artikel_list' #Rename attribute object_list dengan artikel_list
    ordering = ['-published'] #Memberikan '-' akan membuar ordering dari A-Z menjadi Z-A
    paginate_by = 3 #Membuat data yang ditampilkan sebagai 2 per halaman

    def get_queryset(self):
        if self.kwargs['kategori'] == 'kategori':
            self.queryset = self.model.objects.all()
            self.kwargs.update({
                'kategori':self.kwargs['kategori']
            })
        else:
            self.queryset = self.model.objects.filter(kategori__iexact = self.kwargs['kategori']) #Menggunakan filter untuk menampilkan semua data sesuai dengan filter
            self.kwargs.update({
                'kategori':self.kwargs['kategori']
            })
        return super().get_queryset()

    def get_context_data(self, *args, **kwargs):
        kategori_list = self.model.objects.values_list('kategori', flat=True).distinct() #Menggunakan values_list untuk mengambil semua data pada field kategori
        self.kwargs.update({
            'kategori_list':kategori_list #Masukan kategori_list ke kwargs.update
        })
        kwargs = self.kwargs
        return super().get_context_data(**kwargs) #Menampilkan kwargs dari kategori_list yang sudah dibuat


class ArtikelManageListView(ListView):
    model = Artikel
    template_name = "artikel/artikel_manage.html"
    context_object_name = 'artikel_list'


class ArtikelDetailView(DetailView):
    model = Artikel
    template_name = "artikel/artikel_detail.html"
    context_object_name = 'artikel_detail' #Rename attribute object_list dengan artikel_detail

    def get_context_data(self, *args, **kwargs):
        kategori_list = self.model.objects.values_list('kategori', flat=True).distinct() #Menggunakan values_list untuk mengambil semua data pada field kategori
        self.kwargs.update({
            'kategori_list':kategori_list #Masukan kategori_list ke kwargs.update
        })
        
        artikel_serupa = self.model.objects.filter(kategori=self.object.kategori).exclude(id=self.object.id) #exclude digunakan agar tidak tampil di list ketika data di pilih
        self.kwargs.update({
            'artikel_serupa':artikel_serupa #Masukan kategori_list ke kwargs.update
        })

        kwargs = self.kwargs
        return super().get_context_data(**kwargs) #Menampilkan kwargs dari kategori_list yang sudah dibuat


class ArtikelCreateView(CreateView):
    form_class = ArtikelForm
    template_name = "artikel/artikel_create.html"


class ArtikelDeleteView(DeleteView):
    model = Artikel
    template_name = "artikel/artikel_delete_confirmation.html"
    success_url = reverse_lazy('artikel:artikel_manage')


class ArtikelUpdateView(UpdateView):
    form_class = ArtikelForm
    model = Artikel
    template_name = 'artikel/artikel_update.html'
