from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import IoTMachine
from .serializers import IoTMachineSerializer

# Create your views here.


@csrf_exempt                                            # We need to do this so that a simple device can register.
def iot_machines_list(request):                          # TODO Add some type of authentication for iot devices
    """
    List all machines, or create a new iot machine.
    """
    if request.method == 'GET':
        iot_machines = IoTMachine.objects.all()
        iot_serializer = IoTMachineSerializer(iot_machines, many=True)
        return JsonResponse(iot_serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = IoTMachineSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)



@csrf_exempt
def iot_machine_find(request, mac_address):
    """
    Find an IoT Machine based on it's MAC address.

    """
    print("Trying to find an IoT Machine and redirect locally")

    try:
        iot_device = IoTMachine.objects.get(device_id=mac_address)
    except IoTMachine.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = IoTMachineSerializer(iot_device)
        print("We found the device returning the IOT Local address: {}".format(iot_device.local_ip))
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = IoTMachineSerializer(iot_device, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)


    #elif request.method == 'DELETE':
    #    print("Deleting the device with MAC address: {}".format(iot_device.device_id))
    #    iot_device.delete()
    #    return HttpResponse(status=204)