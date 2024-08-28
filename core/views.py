from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import serializers
from core.models import CronLog
from rest_framework.views import APIView


class CronLogSerializer(serializers.ModelSerializer):

    class Meta:
        model = CronLog
        fields = '__all__'


class CronLogView(APIView):

    def get(self, request: Request):

        models = CronLog.objects.order_by('-created_at').all()
        return Response(CronLogSerializer(instance=models, many=True).data)
