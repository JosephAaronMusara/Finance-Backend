from rest_framework import serializers
from .models import *

class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ['id', 'currency_code', 'name']

    def validate_currency_code(self, value):
        if len(value) > 3:
            raise serializers.ValidationError("Currency code cannot exceed 5 characters.")
        return value

    def validate_description(self, value):
        if len(value) > 50:
            raise serializers.ValidationError("Name cannot exceed 50 characters.")
        return value
class BankBalanceSerializer(serializers.ModelSerializer):
    currency = serializers.PrimaryKeyRelatedField(queryset=Currency.objects.all())

    class Meta:
        model = BankBalance
        fields = ['id','name','type', 'currency', 'amount']

    def validate_amount(self, value):
        if value <= 0:
            raise serializers.ValidationError("Amount must be greater than zero.")
        return value

    def create(self, validated_data):
        return BankBalance.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.currency = validated_data.get('currency', instance.currency)
        instance.name = validated_data.get('name', instance.name)
        instance.amount = validated_data.get('amount', instance.amount)
        instance.type = validated_data.get('type',instance.type)

        instance.save()
        return instance
    
class AccountReceivableSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountReceivable
        fields = '__all__'

    def validate_total_amount(self, value):
        if value <= 0:
            raise serializers.ValidationError("Amount must be greater than zero.")
        return value
    
    def validate_balance(self, value):
        if value <= 0:
            raise serializers.ValidationError("Amount must be greater than zero.")
        return value

    def create(self, validated_data):
        return AccountReceivable.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.invoice_date = validated_data.get('invoice_date', instance.invoice_date)
        instance.invoice_number = validated_data.get('invoice_number', instance.invoice_number)
        instance.customer_name = validated_data.get('customer_name', instance.customer_name)
        instance.total_amount = validated_data.get('total_amount',instance.total_amount)
        instance.due_date = validated_data.get('due_date', instance.due_date)
        instance.balance = validated_data.get('balance',instance.balance)
        instance.service_type = validated_data.get('service_type',instance.service_type)


        instance.save()
        return instance

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = ['id', 'description', 'amount']

    def validate_description(self, value):
        if len(value) > 50:
            raise serializers.ValidationError("Description cannot exceed 50 characters.")
        return value

    def validate_amount(self, value):
        if value <= 0:
            raise serializers.ValidationError("Amount must be greater than zero.")
        return value