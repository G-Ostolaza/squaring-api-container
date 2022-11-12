from squaring.views import SquaringView, HelloWorldView
from django.urls import path

urlpatterns = [
    path('<int:number>', view=SquaringView.as_view()),
    path('', view= HelloWorldView.as_view())
]
