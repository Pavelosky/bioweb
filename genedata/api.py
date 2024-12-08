from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework import mixins
from .models import *
from .serializers import *

# @api_view(['GET', 'POST', 'DELETE', 'PUT'])

# def gene_detail(request, pk):
#     """
#     Retrieve, update or delete a code snippet.
#     """
#     if request.method == 'POST':
#         serializer = GeneSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     try:
#         gene = Gene.objects.get(pk=pk)
#     except Gene.DoesNotExist:
#         return HttpResponse(status=404)
    
#     if request.method == 'GET':
#         serializer = GeneSerializer(gene)
#         return Response(serializer.data)
    
#     if request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = GeneSerializer(gene, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     if request.method == 'DELETE':
#         gene.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
class GeneDetail(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Gene.objects.all()
    serializer_class = GeneSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

# @api_view(['GET'])
# def gene_list(request):
#     """
#     List all code snippets, or create a new snippet.
#     """
#     try:
#         # Attempt to retrieve all Gene objects from the database
#         genes = Gene.objects.all()
#     except Gene.DoesNotExist:
#         # If no Gene objects exist, return a 404 Not Found response
#         return HttpResponse(status=404)
    
#     # Check if the request method is GET
#     if request.method == 'GET':
#         # Serialize the list of Gene objects into JSON format
#         serializer = GeneSerializer(genes, many=True)
#         # Return the serialized data as a JSON response
#         return JsonResponse(serializer.data, safe=False)

class GeneList(generics.ListAPIView):
    queryset = Gene.objects.all()
    serializer_class = GeneListSerializer

    
    
