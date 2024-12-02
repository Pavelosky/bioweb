from django.shortcuts import render
from .models import *
from django.http import HttpResponseRedirect 

# Create your views here.
def index(request):
    master_genes = Gene.objects.all()  
    return render(request, 'genedata/index.html', {'master_genes': master_genes})

def gene(request, pk): 
    gene = Gene.objects.get(pk=pk) 
    gene.access += 1 
    print("Gene record:", pk, "access count:", str(gene.access))
    gene.save()
    master_genes = Gene.objects.all()
    return render(request, 'genedata/gene.html', {'gene': gene, master_genes: 'master_genes'}) 

def list(request, type):
    genes = Gene.objects.filter(entity__exact=type)
    master_genes = Gene.objects.all()   
    return render(request, 'genedata/list.html', {'genes': genes, 'type': type, master_genes: 'master_genes'}) 

def poslist(request): 
    genes = Gene.objects.filter(entity__exact='Chromosome').filter(sense__startswith='+') 
    master_genes = Gene.objects.all()   
    return render(request, 'genedata/list.html', {'genes': genes, 'type': 'PosList', master_genes: 'master_genes'})

def delete(request, pk): 
    GeneAttributeLink.objects.filter(gene_id=pk).delete() 
    Gene.objects.filter(pk=pk).delete() 
    return HttpResponseRedirect("/")  # Redirect to index page
