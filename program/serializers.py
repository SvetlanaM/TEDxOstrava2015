from .models import Section, Schedule, SlotKind, Slot, Presentation
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework import routers, serializers, viewsets, permissions
from rest_framework.reverse import reverse
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from speakers.serializers import SpeakerSerializer
from mobile_settings.serializers import ImageSerializer


class SectionSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Section 

class ScheduleSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Schedule

class SlotKindSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = SlotKind
		fields = [
			'id',
			'slot_name',

		]



class SlotSerializer(serializers.HyperlinkedModelSerializer):
	kind = SlotKindSerializer(read_only = True, many = False)
	url = serializers.PrimaryKeyRelatedField(queryset = Presentation.objects.all())
	class Meta:
		model = Slot
		fields = [
			'id',
			'url',
			'kind',
			'start',
			'end',

		]


class PresentationSerializer(serializers.HyperlinkedModelSerializer):
	slot = SlotSerializer(many = False)
	cover_image = ImageSerializer(many = False)
	speakers = SpeakerSerializer(many = True)
	class Meta:
		model = Presentation
		fields = [
			'id',
			#'url',
			'slot',
			'cover_image',
			'speakers',
			
		]