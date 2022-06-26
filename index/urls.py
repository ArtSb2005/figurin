from django.urls import path

from contact.views import ContactCreate
from index.views import HomePageView, HtbPageView, ReviewsPageView, ReservationPageView, DeliveryPageView, \
    About1PageView, About2PageView, About3PageView, AvailPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('htb', HtbPageView.as_view(), name='htb'),
    path('reviews', ReviewsPageView.as_view(), name='reviews'),
    path('reservation', ReservationPageView.as_view(), name='reservation'),
    path('delivery', DeliveryPageView.as_view(), name='delivery'),

    path('avail', AvailPageView.as_view(), name='avail'),

    path('about1', About1PageView.as_view(), name='about1'),
    path('about2', About2PageView.as_view(), name='about2'),
    path('about3', About3PageView.as_view(), name='about3'),

    path('contact', ContactCreate.as_view(), name='contact'),

]