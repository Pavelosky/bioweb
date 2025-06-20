from django import forms 
from django.forms import ModelForm
from .models import *

class ECForm(forms.Form): 
    ec_name = forms.CharField(label='EC Name', max_length=100)

    def clean(self): 
        cleaned_data = super(ECForm, self).clean() 
        ec_name = cleaned_data.get("ec_name") 
        if not ec_name.isalpha():
            raise forms.ValidationError("EC Name must contain only alphabetical characters")

class GeneForm(ModelForm): 
    class Meta: 
        model = Gene 
        fields = ['gene_id', 'entity', 'start', 'stop', 'sense', 'start_codon', 'sequencing', 'ec'] 

    def clean(self): 
        cleaned_data = super(GeneForm, self).clean() 
        entity = cleaned_data.get("entity") 
        sense = cleaned_data.get("sense") 
        if not entity == "Chromosome" and not entity == "Plasmid": 
            raise forms.ValidationError("Entity must be 'Chromosome' or 'Plasmid'") 
        if not sense == "+" and not sense == "-": 
            raise forms.ValidationError("Sense must be '+' or '-'") 
        return(cleaned_data)