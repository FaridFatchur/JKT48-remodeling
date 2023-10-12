from rest_framework import serializers
from .models import Member

class MemberSerializer(serializers.ModelSerializer):
    photo = serializers.ImageField(max_length=None, allow_empty_file=True, use_url=True)

    class Meta:
        model = Member
        fields = ('id_member', 'stage_name', 'gen', 'full_name', 'date_of_birth', 'blood_type', 'horoskop', 'height', 'photo', 'is_capt', 'is_cent', 'is_trainee')