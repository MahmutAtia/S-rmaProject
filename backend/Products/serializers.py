from rest_framework import serializers, reverse
from .models import Product


class ProductInlineSerializer(serializers.Serializer):
      title = serializers.CharField(read_only =True)
      content = serializers.CharField(read_only =True)
      price = serializers.FloatField(read_only =True)


      
class UserSerializer(serializers.Serializer):
      username = serializers.CharField()
      pk = serializers.IntegerField()
      other_products = serializers.SerializerMethodField(read_only = True)

      def get_other_products(self,obj):
            user = obj
            qs = user.product_set.all()
            return ProductInlineSerializer(qs,many= True).data
            
            

            



class ProductSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only = True)
    discount = serializers.SerializerMethodField(read_only = True)
    sales = serializers.SerializerMethodField(read_only = True)
    url = serializers.SerializerMethodField(read_only = True)
    url_2 = serializers.HyperlinkedIdentityField(view_name="detail-view",
                                                 lookup_field="pk" )
    class Meta:
        model = Product
        fields = ["owner","url","url_2","title", "content", "price","discount","sales"]

    def get_url_2(self,obj):
        request = self.context.get("request")
        if request is None:
            return None

        return reverse.reverse("detail-view",kwargs={"pk":obj.pk} ,request= request)
        
    def get_url(self,obj):
        request = self.context.get("request")
        if request is None:
               return None

        return reverse.reverse("detail-view",kwargs={"pk":obj.pk} ,request= request)
           
           

    def get_discount(self,obj):

        if isinstance(obj, Product):
                return obj.get_discount
        else:
                return None
    
    def get_sales(self,obj):
        
            
        if isinstance(obj, Product):
                    return obj.sales_price()
        else:
                    return None
    
        
            