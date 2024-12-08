from django.shortcuts import render,redirect
from cineMagic.models import Movie
# Create your views here.
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
# def homepage(request):
#    m=Movie.objects.all()
#    context={'movie':m}
#    return render(request,'home.html',context)


class HomeView(ListView):
   model=Movie
   context_object_name="movie"
   template_name = "home.html"

   def get_queryset(self):
       queryset=super().get_queryset().filter(title__startswith='V')
       return queryset



#get_queryset()


#getcontext






# def add_movie(request):
#    if (request.method == "POST"):
#       t = request.POST['t']
#       d = request.POST['d']
#       l = request.POST['l']
#       y = request.POST['y']
#       i = request.FILES['i']
#
#       m = Movie.objects.create(title=t, description=d, language=l, year=y, image=i)
#       m.save()
#       return redirect('home')
#    return render(request,'addmovies.html')

from cineMagic.form import MovieForm
# def add_movie(request):
#    if(request.method=="POST"):
#       form=MovieForm(request.POST)
#        if form.is_valid():
#           form.save()
#        return redirect('home')
# form=MovieForm()
# context={'form':form}
# return render(request,'add1.html',context)

from django.urls import reverse_lazy

class AddMovie(CreateView):
   model=Movie
   form_class = MovieForm
   template_name = "add1.html"
   success_url = reverse_lazy('home')






def details(request,p):
   m=Movie.objects.get(id=p)
   context={'display':m}

   return render(request, 'details.html',context)


class MovieDetail(DetailView):
   model=Movie
   context_object_name = "display"
   template_name = "details.html"

# def edit(request, p):
#    k = Movie.objects.get(id=p)
#    if (request.method == "POST"):
#       k.title = request.POST['t']
#       k.description = request.POST['d']
#       k.language = request.POST['l']
#       k.year = request.POST['y']
#
#       if (request.FILES.get('i') == None):
#          k.save()
#       else:
#          k.image = request.FILES.get('i')
#
#
#
#       k.save()
#       return redirect('home')
#
#    context = {'edit': k}
#    return render(request, 'edit.html', context)



class UpdateMovie(UpdateView):
   model=Movie
   form_class = MovieForm
   template_name = "add1.html"
   success_url = reverse_lazy('home')





from django.db.models import Q
# Create your views here.
def search_movie(request):
    if(request.method=="POST"):
        query=request.POST['q']
        if query:
            result=Movie.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))
            context={'res':result,'query':query}
    return render(request,'search.html',context)



# def delete(request,p):
#    k=Movie.objects.get(id=p)
#    k.delete()
#    return redirect('home')


class Moviedelete(DeleteView):
    template_name = "delete.html"
    model=Movie
    success_url = reverse_lazy('home')