from django.urls import path
from .views import ApiView,api,ProductsCLApi,alt_api_view
from rest_framework.authtoken.views import obtain_auth_token

from .views import ProductRUDApi
urlpatterns = [
    path("",api, name="api"),
    path("auth/",obtain_auth_token ),
    path("products/<int:pk>",ProductRUDApi.as_view(), name= "detail-view" ),
    path("products/",ProductsCLApi.as_view() ),
    # path("products/<int:pk>/update",ProductUpdateApi.as_view() ),
    # path("products/<int:pk>/delete",ProductDeleteApi.as_view() ),
    path("api/generic", ApiView.as_view()),
     path("api/generic/<int:pk>", ApiView.as_view()),
      path("api/generic/<int:pk>/update",ApiView.as_view() ),
    path("api/generic/<int:pk>/delete",ApiView.as_view() ),


    
    path("altapi/<int:pk>", alt_api_view),
    path("altapi", alt_api_view)

]