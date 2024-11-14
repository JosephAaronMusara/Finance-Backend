from rest_framework import serializers
from .models import *

class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ['id', 'currency_code', 'description']

    def validate_currency_code(self, value):
        if len(value) > 3:
            raise serializers.ValidationError("Currency code cannot exceed 5 characters.")
        return value

    def validate_description(self, value):
        if len(value) > 50:
            raise serializers.ValidationError("Description cannot exceed 50 characters.")
        return value

class CurrentAssetSerializer(serializers.ModelSerializer):
    currency = CurrencySerializer()

    class Meta:
        model = CurrentAsset
        fields = ['id', 'currency', 'amount']

    def validate_amount(self, value):
        if value <= 0:
            raise serializers.ValidationError("Amount must be greater than zero.")
        return value

    def create(self, validated_data):
        currency_data = validated_data.pop('currency')
        currency, _ = Currency.objects.get_or_create(**currency_data)
        return CurrentAsset.objects.create(currency=currency, **validated_data)

    def update(self, instance, validated_data):
        currency_data = validated_data.pop('currency', None)
        if currency_data:
            currency, _ = Currency.objects.get_or_create(**currency_data)
            instance.currency = currency
        instance.amount = validated_data.get('amount', instance.amount)
        instance.save()
        return instance

class NetCurrentAssetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NetCurrentAsset
        fields = ['id', 'currency', 'odsecurity_amount','odusage_amount']

    def validate_currency(self, value):
        if len(value) > 3:
            raise serializers.ValidationError("Currency is denoted using 3 letters max.")
        return value

    def validate_odsecurity_amount(self, value):
        if value < 0:
            raise serializers.ValidationError("Amount must be non-negative.")
        return value

class UnutilizedGrantSerializer(serializers.ModelSerializer):
    currency = CurrencySerializer()

    class Meta:
        model = UnutilizedGrant
        fields = ['id', 'donor', 'currency', 'amount']

    def validate_donor(self, value):
        if len(value) > 50:
            raise serializers.ValidationError("Donor name cannot exceed 50 characters.")
        return value

    def validate_amount(self, value):
        if value < 0:
            raise serializers.ValidationError("Amount must be non-negative.")
        return value

    def create(self, validated_data):
        currency_data = validated_data.pop('currency')
        currency, _ = Currency.objects.get_or_create(**currency_data)
        return UnutilizedGrant.objects.create(currency=currency, **validated_data)

    def update(self, instance, validated_data):
        currency_data = validated_data.pop('currency', None)
        if currency_data:
            currency, _ = Currency.objects.get_or_create(**currency_data)
            instance.currency = currency
        instance.donor = validated_data.get('donor', instance.donor)
        instance.amount = validated_data.get('amount', instance.amount)
        instance.save()
        return instance

class TotalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Total
        fields = ['id', 'description', 'total_amount']

    def validate_description(self, value):
        if len(value) > 50:
            raise serializers.ValidationError("Description cannot exceed 50 characters.")
        return value

    def validate_total_amount(self, value):
        if value < 0:
            raise serializers.ValidationError("Total amount must be non-negative.")
        return value
