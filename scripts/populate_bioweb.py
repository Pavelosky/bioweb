import os
import sys
import django
import csv
from collections import defaultdict

sys.path.append("C:/Users/pawel/OneDrive/Documenten/BSc CS UoL/level 6/AWD/mid-term/topic2_files/topic2/bioweb")  # Add bioweb project to Python path
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bioweb.settings")  # Set Django settings module
django.setup()  # Setup Django

from genedata.models import *  # Import all models from genedata app

data_file = "C:/Users/pawel/OneDrive/Documenten/BSc CS UoL/level 6/AWD/mid-term/topic2_files/topic2/example_data_to_load.csv"  # Path to data file
genes = defaultdict(list)  # Create a dictionary to store genes
sequencing = set()  # Create a set to store sequencing factories
ec = set()  # Create a set to store EC names
products = defaultdict(dict)  # Create a dictionary to store products
attributes = defaultdict(dict)  # Create a dictionary to store attributes

with open(data_file) as csv_file: 
    csv_reader = csv.reader(csv_file, delimiter=',') 
    header = csv_reader.__next__() 
    for row in csv_reader: 
        product_pairs = row[9].split(';') 
        attribute_pairs = row[10].split(';') 
        for pair in product_pairs: 
            tupple = pair.split(":") 
            products[row[0]][tupple[0]] = tupple[1] 
        for pair in attribute_pairs: 
            tupple = pair.split(":") 
            attributes[row[0]][tupple[0]] = tupple[1] 
        ec.add(row[8]) 
        sequencing.add((row[4], row[5])) 
        genes[row[0]] = row[1:4]+row[6:9] 

GeneAttributeLink.objects.all().delete()  # Delete all GeneAttributeLink objects
Gene.objects.all().delete()  # Delete all Gene objects
EC.objects.all().delete()  # Delete all EC objects
Sequencing.objects.all().delete()  # Delete all Sequencing objects
Product.objects.all().delete()  # Delete all Product objects
Attribute.objects.all().delete()  # Delete all Attribute objects

ec_rows = {}
sequencing_rows = {}
gene_rows = {}

for entry in ec: 
    row = EC.objects.create(ec_name=entry)
    row.save()
    ec_rows[entry] = row

for seq_centre in sequencing: 
    row = Sequencing.objects.create(sequencing_factory=seq_centre[0], factory_location=seq_centre[1])
    row.save()
    sequencing_rows[seq_centre[0]] = row

for gene_id, data in genes.items(): 
    row = Gene.objects.create(gene_id=gene_id, entity=data[0], start=data[1], 
                              stop=data[2], sense=data[3], start_codon=data[4], 
                              sequencing=sequencing_rows['Sanger'], ec=ec_rows[data[5]])
    row.save()
    gene_rows[gene_id] = row

for gene_id, data in products.items():
    for key in data.keys():
        row = Product.objects.create(type=key, product=data[key], gene=gene_rows[gene_id])
        row.save()

for gene_id, data in attributes.items():
    for key in data.keys():
        row = Attribute.objects.create(key=key, value=data[key])
        row.gene.add(gene_rows[gene_id])
        row.save()