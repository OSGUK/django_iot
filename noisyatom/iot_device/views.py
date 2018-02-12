from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from iot_device.models import IoTMachine
from .serializers import IoTMachineSerializer
from django.http import HttpResponse, HttpResponseRedirect, Http404, HttpResponseForbidden
import ipaddress

# Create your views here.


@csrf_exempt                                            # We need to do this so that a simple device can register.
def iot_machines_list(request):                         # TODO Add some type of authentication for iot devices
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


@csrf_exempt                                            # We need to do this so that a simple device can register.
def iot_machines_register(request):                     # TODO Add some type of authentication for iot devices
    """
    :param request: JSON {
                    device_id:      mac_adress e.g. 98:83:89:3a:96:a5
                    device_name:    "any text string"
                    local_ip:       IPV4 or IPV6 e.g. 192.168.0.1
                    }

    :return: HttpResponseForbidden, HttpResponse, HttpResponseRedirect

    Register an IoT Machine based on it's MAC address.
    If this is a POST we check it's unique. Verify the JSON package. And register the machine

    If this is a PUT we check it exists. verify the JSON package. And update the machine.

    TODO - Authentication & Authorization!

    """
    data = JSONParser().parse(request)

    # If it's a http post check the MAC is unique and register the machine
    if request.method == 'POST':
        print("We got the following POST data in the request: {}".format(data)) # TODO Remove print
        serializer = IoTMachineSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    # if it's a http put check the MAC exists and update values of the machine
    if request.method == 'PUT':
        print("We got the following PUT data in the request: {}".format(data))  # TODO Remove print

        try:
            iot_device = IoTMachine.objects.get(device_id=data['device_id'])
            serializer = IoTMachineSerializer(iot_device, data=data)
        except IoTMachine.DoesNotExist:
            print("This device does not exist") # TODO Remove print
            error={"device_id": "iot machine with this device id does not exist."}
            return JsonResponse(error, status=404)              # Return a http resource not found error code

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def iot_machine_find(request, mac_address):
    """
    Find an IoT Machine based on it's MAC address.
    If it has a public local IP address then redirect to this IP.
    If our embedded system does not have a valid IP address then don't redirect and show the user a
    friendly page saying the machine is not active at the moment.

    """
    print("Trying to find an IoT Machine and redirect locally with mac_address of: {}".format(mac_address)) # TODO Remove print

    # Make sure we can find the machine via it's mac address
    try:
        iot_device = IoTMachine.objects.get(device_id=mac_address)
    except IoTMachine.DoesNotExist:
        return HttpResponse(status=404)

    # Make sure the IP address we pass back is still valid
    try:
        ipaddress.IPv4Address(iot_device.local_ip)
    except ValueError:
        # TODO Paint a nice screen and show the user the device exists but routing is broken
        print("There was an issue with the stored IP address for the device: {} - handle it an carry on".format(iot_device.mac_address)) # TODO Remove print
        return Http404

    # Happy path - direct the user to the device
    if request.method == 'GET':

        scheme = 'http'                 # TODO make this a dynamic variable from settings or DB table
        path = 'light'                # TODO make this a dynamic variable from settings or DB table
        remote_url = "{0}://{1}/{2}".format(scheme, iot_device.local_ip, path)
        print("We found the device returning the IOT Local address: {}".format(remote_url))     # TODO Remove print
        return HttpResponseRedirect(remote_url)

    # If we get this far - we don't support other methods at the minute so reply with a forbidden.
    return HttpResponseForbidden

    #elif request.method == 'DELETE':
    #    print("Deleting the device with MAC address: {}".format(iot_device.device_id))
    #    iot_device.delete()
    #    return HttpResponse(status=204)