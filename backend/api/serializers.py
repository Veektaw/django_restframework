from rest_framework import serializers

class UserPublicSerializer(serializers.Serializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='products',
        lookup_field='pk',
        read_only=True
        )
        
    title = serializers. CharField(read_only=True)
    
class UserNestedSerializer(serializers.Serializer):
    username = serializers.CharField(read_only=True)
    id = serializers.IntegerField(read_only=True)
    other_products = serializers.SerializerMethodField (read_only=True)

    def get_other_products (self, obj):
        print (obj)
        user = obj
        # my_products_qs = user.product_set.all() [:5]
        return UserNestedSerializer( many=True, context=self.context).data