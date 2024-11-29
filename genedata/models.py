from django.db import models  # Import Django's model module

class EC(models.Model):  # Define a model for EC
    ec_name = models.CharField(max_length=256, null=False, blank=False)  # EC name, required field

    def __str__(self): 
        return self.ec_name


class Sequencing(models.Model):  # Define a model for Sequencing
    sequencing_factory = models.CharField(max_length=256, null=False, blank=False)  # Sequencing factory name, required field
    factory_location = models.CharField(max_length=256, null=False, blank=False)  # Factory location, required field

    def __str__(self):
        return self.sequencing_factory


# Create your models here.
class Gene(models.Model):  # Define a model for Gene
    gene_id = models.CharField(max_length=256, null=False, blank=False, db_index=True)  # Gene identifier, required field
    entity = models.CharField(max_length=256, null=False, blank=False)  # Entity name, required field
    start = models.IntegerField(null=False, blank=True)  # Start position, required field but can be blank
    stop = models.IntegerField(null=False, blank=True)  # Stop position, required field but can be blank
    sense = models.CharField(max_length=1)  # Sense strand, single character
    start_codon = models.CharField(max_length=1, default="M")  # Start codon, default is "M"
    sequencing = models.ForeignKey(Sequencing, on_delete=models.DO_NOTHING)  # Foreign key to Sequencing, no action on delete
    ec = models.ForeignKey(EC, on_delete=models.DO_NOTHING)  # Foreign key to EC, no action on delete
    access = models.IntegerField(null=False, blank=False, default=0)  # Access count, required field, default is 0

    def __str__(self): 
        return self.gene_id # Return gene_id as string representation



class Product(models.Model):  # Define a model for Product
    type = models.CharField(max_length=256, null=False, blank=False)  # Product type, required field
    product = models.CharField(max_length=256, null=False, blank=False)  # Product name, required field
    gene = models.ForeignKey(Gene, on_delete=models.CASCADE)  # Foreign key to Gene, cascade delete



class Attribute(models.Model):  # Define a model for Attribute
    key = models.CharField(max_length=256, null=False, blank=False)  # Attribute key, required field
    value = models.CharField(max_length=256, null=False, blank=False)  # Attribute value, required field
    gene = models.ManyToManyField(Gene, through='GeneAttributeLink')  # Many-to-many relationship with Gene through GeneAttributeLink

    def __str__(self):
        return self.key+"="+self.value  # Return key=value as string representation



class GeneAttributeLink(models.Model):  # Define a model for linking Gene and Attribute
    gene = models.ForeignKey(Gene, on_delete=models.DO_NOTHING)  # Foreign key to Gene, no action on delete
    attribute = models.ForeignKey(Attribute, on_delete=models.DO_NOTHING)  # Foreign key to Attribute, no action on delete
