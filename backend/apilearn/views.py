from django.shortcuts import render,get_object_or_404
from django.http import JsonResponse
from Products.models import Product
from rest_framework.decorators import api_view
from django.forms.models import model_to_dict
from Products.serializers import ProductSerializer
from rest_framework import generics , mixins, permissions, authentication
from rest_framework.response import Response
import json
# Create your views here.


class ProductRUDApi(generics.RetrieveUpdateDestroyAPIView):

    permission_classes = [permissions.DjangoModelPermissions]
    authentication_classes = [authentication.SessionAuthentication,
                              authentication.TokenAuthentication]
    queryset= Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"

class ProductsCLApi(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [authentication.SessionAuthentication,
                              authentication.TokenAuthentication]
    permission_classes = [permissions.DjangoModelPermissions]

    def  get_queryset(self):
        qs = Product.objects.filter(owner = self.request.user)
        return qs
        


    def perform_create(self,serializer):
        print(serializer.validated_data)

        serializer.save()
 

class ApiView(mixins.RetrieveModelMixin,
              mixins.CreateModelMixin
    ,mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"
    def get(self,request, *args,**kwargs):
        print(args,kwargs)
        pk = kwargs.get("pk")
        if pk is not None:
            return self.retrieve(request)
        return self.list(request)
    def post(self, request, *args, **kwargs):
        return self.create(request)
    
    def perform_create(self, serializer):
        content = serializer.validated_data.get("content")
        serializer.save(content = content+" this is cool stuff")

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

  
    









@api_view(["GET","POST"])
def alt_api_view(request,pk=None):

    if request.method == "GET":
        if pk is not None:
            #detail view
            obj = get_object_or_404(Product,pk=pk)
            serializer = ProductSerializer(obj,many=False)
            return JsonResponse(serializer.data)
       
        
        qs = Product.objects.all()
        serializer = ProductSerializer(qs,many=True)
        return Response(serializer.data)
    if request.method == "POST":
        print(request.data)
        serializer = ProductSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

            return Response(serializer.data)

        else:
           return JsonResponse({"msg":"not valid"})
        






@api_view(["POST"])
def api(request):
    print(request.data)
    serializer  = ProductSerializer(data = request.data)
    if serializer.is_valid():
        print(serializer.data)
        return JsonResponse({"sucses":"true"} )
    else:
        return JsonResponse({"sucses":"false"} )
        print("not valid")
 