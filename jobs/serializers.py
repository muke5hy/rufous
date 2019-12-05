from rest_framework import serializers
from jobs.models import Jobs

class JobsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Jobs
        fields = ['job_title', 'job_discribtion', 'hourly_rate', 'job_period','job_requirement']
        ordering = ['']