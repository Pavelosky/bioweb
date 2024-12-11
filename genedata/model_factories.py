import factory
from random import randint, choice

from django.test import TestCase
from django.conf import settings
from django.core.files import File

from .models import *

class ECFactory(factory.django.DjangoModelFactory):
    # This factory creates instances of the EC model with predefined attributes.
    # The ec_name attribute is set to "transferase".
    ec_name = "transferase"

    class Meta:
        # Specifies the model that this factory is for.
        model = EC

class SequencingFactory(factory.django.DjangoModelFactory):
    # This factory creates instances of the Sequencing model with predefined attributes.
    # The sequencing_factory attribute is set to "Sanger".
    # The factory_location attribute is set to "UK".
    sequencing_factory = "Sanger"
    factory_location = "UK"

    class Meta:
        # Specifies the model that this factory is for.
        model = Sequencing


class GeneFactory(factory.django.DjangoModelFactory):
    # This factory creates instances of the Gene model with predefined attributes.
    # Various attributes like gene_id, entity, start, stop, sense, start_codon, access are set with default values.
    # The sequencing attribute is set using a SubFactory, which means it will create a Sequencing instance using SequencingFactory.
    # The ec attribute is set using a SubFactory, which means it will create an EC instance using ECFactory.
    gene_id = factory.Sequence(lambda n: 'gene%d' % n+str(1))
    entity = choice(['Plasmid', 'Chromosome'])
    start = randint(1, 100000)
    stop = start + randint(1, 10000)
    sense = "+"
    start_codon = "M"
    sequencing = factory.SubFactory(SequencingFactory)
    ec = factory.SubFactory(ECFactory)
    access = 0

    class Meta:
        # Specifies the model that this factory is for.
        model = Gene
