from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile,Product_Model,CommentModel



class UserSerializerView(serializers.ModelSerializer):

    class Meta:
       model = User
       fields = ['username', 'email']

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product_Model
        fields = '__all__'





class CommentSerializer(serializers.ModelSerializer):


    class Meta:
        model = CommentModel
        fields = '__all__'


# class ReviewtSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = ReviewModel
#         fields = '__all__'
#
#
# class orderSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = Order
#         fields = '__all__'