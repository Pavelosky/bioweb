from django.shortcuts import render
from .models import *
from django.http import HttpResponseRedirect 

# Create your views here.
def index(request):
    genes = Gene.objects.all()  
    return render(request, 'genedata/index.html', {'genes': genes})

def gene(request, pk): 
    gene = Gene.objects.get(pk=pk) 
    gene.access += 1 
    print("Gene record:", pk, "access count:", str(gene.access))
    gene.save()
    return render(request, 'genedata/gene.html', {'gene': gene}) 

def list(request, type):
    gene = Gene.objects.filter(entity__exact=type)
    return render(request, 'genedata/list.html', {'genes': gene, 'type': type}) 

def poslist(request): 
    genes = Gene.objects.filter(entity__exact='Chromosome').filter(sense__startswith='+') 
    return render(request, 'genedata/list.html', {'genes': genes, 'type': 'PosList'})

def delete(request, pk): 
    GeneAttributeLink.objects.filter(gene_id=pk).delete() 
    Gene.objects.filter(pk=pk).delete() 
    return HttpResponseRedirect("/")  # Redirect to index page
