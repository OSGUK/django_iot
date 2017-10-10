from django.shortcuts import render
from django.conf import settings
# Create your views here.

def rolepoint_view(request):
    print("Hitting role point view")
    context = {}
    return render(request, 'rolepoint.html', context)

def populate_context(data_dict, context):
    context['name'] = data_dict['name']


def rolepoint_search(request):
    print ("hitting rolepoint search")
    context = {'name': 'none',
               'address': 'none',
               'company': 'none',
               'email': 'none',
               'city': 'none',
               'country': 'none',
               'job_history': 'none'}

    if 'rp_search' in request.POST:
        print("We have a search querry for rp_search of:{}".format(request.POST['rp_search'].lower()))
    else:
        print("rp_search not found - sending user back to enter a search criteria")
        return render(request, 'rolepoint.html', context)

    # Lets search the roleplay data for the name given.
    search_name = request.POST['rp_search'].lower()
    #TODO Change to list comprehension for this simple search
    for key in settings.ROLEPOINT_DATA:
        if key['name'].lower()== search_name:
            print("***** Match found *****")
            context = key
            print('Context is now: {}'.format(context))




    return render(request, 'rolepoint-search.html', context)

def dashboard_view(request):
    context = {}
    return render(request, 'dashboard.html', context)
