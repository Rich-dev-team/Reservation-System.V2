from rest_framework import serializers
from .models import Account, ActionLog, BkList, Production, Staff, Store


class Acc_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'
        # fields = ('user_id', 'social_id', 'social_app', 'username', 'phone','birth',)


class Actlog_Serializer(serializers.ModelSerializer):
    class Meta:
        model = ActionLog
        fields = '__all__'


class Bklist_Serializer(serializers.ModelSerializer):
    class Meta:
        model = BkList
        fields = '__all__'


class Prod_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Production
        fields = '__all__'


class Staff_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = '__all__'


class Store_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = '__all__'