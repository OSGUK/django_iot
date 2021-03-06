from django.shortcuts import render
from django.urls import reverse



def index_view(request):
    context = {}

    return render(request, 'index.html', context)


def coming_soon(request):
    context={
        'main_title': 'Coming Soon',
        'paragraph1': 'We are working hard!',
        'paragraph2': 'Stay tuned for our QR codes!',
        'paragraph3': ''}

    return render(request, 'sub-header.html', context)


def dashboard_view(request):
    context = {}
    return render(request, 'dashboard.html', context)

def alfa_view(request):
    template_name = 'alfa.html'
    # TODO Make this dynamic data from a table in our database
    context = {
        'main_title': 'Ecommerce Platform for Alfa Aesar Ltd',
        'description1': 'This project encompassed the migration of a legacy Websmart system into a modern python Django web platform. The platform was deployed onto a hosted server running with Redhat SE Linux 6.2 on an IBM PowerPC platform.',
        'description2': 'Read on to find out more about the specifics...',
        'description3': ''
    }
    return render(request, template_name, context)


def about_us(request):
    # TODO Make this dynamic content from a data base.
    context={
        'main_title':'About Us',
        'description1': 'We have been active for 4 years. A dynamic tech focussed company. We love technology. Our core competences are in Python and Python web frameworks.',
        'description2': 'Check back soon for our open source products centred around QR Code generation and mapping with OAuth2 services.',
        'description3': 'For now - read more to meet the team.'}
    return render(request, 'about-us.html', context)


def ons_view(request):
    template_name = 'ons.html'
    # TODO Make this dynamic data from a table in our database
    context = {
        'main_title': 'Office of National Statistics',
        'description1':'The aim of this project was to convert a legacy Java webserver into a microservices framework. To do this python Django and Flask micro services were written and deployed.',
        'description2':'The cloud tech stack was Cloud Foundary and Docker.',
        'description3':'Highlights on this system were on the authentication framework. Read on for more details...'
    }
    return render(request, template_name, context)


def vodafone_view(request):
    template_name = 'vodafone.html'
    # TODO Make this dynamic content from a data base.
    context={
        'main_title':'Vodafone Patent Wall',
        'description1': 'Noisy Atom provided consultancy in creating a QR code and URL mapping system for the Vodafone Patent Wall',
        'description2': 'It allows static QR codes to be created and etched onto perspex, but still allow dynamic routing to a CMS system to visualise information about Vodafones inventors, technology ant patents',
        'description3': 'For now - read more and see the end results of our innovation.'}
    return render(request, template_name, context)
