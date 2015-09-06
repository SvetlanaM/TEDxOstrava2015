from .serializers import MenuSerializer, MPNSDeviceSerializer, MPNSDeviceCreateSerializer
from .models import Menu, Language, MPNSDevice
from rest_framework import generics,  permissions, mixins
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication, BasicAuthentication


class MenuListAPIView(generics.ListAPIView):
	queryset = Menu.objects.filter(active = True)
	serializer_class = MenuSerializer
	paginate_by = 10

class MPNSDeviceAPIView(generics.ListAPIView):
	queryset = MPNSDevice.objects.all()
	serializer_class = MPNSDeviceSerializer
	paginate_by = 10

class MPNSDetailAPIView(mixins.DestroyModelMixin, mixins.UpdateModelMixin, generics.RetrieveAPIView):
	queryset = MPNSDevice.objects.all()
	serializer_class = MPNSDeviceSerializer
	lookup_field = 'id'

	def get_object(self):
		id = self.kwargs.pop("id")
		obj = get_object_or_404(MPNSDevice, id = id)
		return obj

class MPNSDeviceCreateAPIView(generics.CreateAPIView):
	serializer_class = MPNSDeviceCreateSerializer
	





