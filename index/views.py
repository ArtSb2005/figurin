import requests
from django.shortcuts import render
from django.views.generic import TemplateView
from index.m import medias, cl


class HomePageView(TemplateView):
    template_name = 'index.html'

    def post(self, request):
        if request.method == "POST":
            print(request.POST)
            id = cl.media_id(request.POST["pk"])
            comment = cl.media_comments(id, 0)
            return render(request, "item.html", {"object": request.POST["pk"], "medias": medias, "comment":comment})

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['object'] = medias
        return context

class AvailPageView(TemplateView):
    template_name = 'avail.html'

    def post(self, request):
        if request.method == "POST":
            print(request.POST)
            id = cl.media_id(request.POST["pk"])
            comment = cl.media_comments(id, 0)
            return render(request, "item.html", {"object": request.POST["pk"], "medias": medias, "comment":comment})

    def get_context_data(self, **kwargs):
        context = super(AvailPageView, self).get_context_data(**kwargs)
        context['object'] = medias
        return context

class HtbPageView(TemplateView):
    template_name = 'htb.html'

class ReviewsPageView(TemplateView):
    template_name = 'reviews.html'

class ReservationPageView(TemplateView):
    template_name = 'reservation.html'

class DeliveryPageView(TemplateView):
    template_name = 'delivery.html'

class About1PageView(TemplateView):
    template_name = 'about1.html'

class About2PageView(TemplateView):
    template_name = 'about2.html'

class About3PageView(TemplateView):
    template_name = 'about3.html'

class KodlerPageView(TemplateView):
    template_name = 'kodler.html'