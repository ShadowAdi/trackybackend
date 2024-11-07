from rest_framework import serializers
from .models import Job
from account.models import Account


class JobSerializer(serializers.ModelSerializer):
    posted_by = serializers.PrimaryKeyRelatedField(queryset=Account.objects.all())

    class Meta:
        model = Job
        fields = "__all__"
