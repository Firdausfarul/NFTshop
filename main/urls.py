from django.urls import path
from main.views import show_main, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id , register, login_user, logout_user, delete_product, increase_amount, decrease_amount, get_product_json, add_product_ajax, get_product_json_by_user_id, create_product_flutter
app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product', create_product, name='create_product'),
    path('xml/', show_xml, name='show_xml'), 
    path('json/', show_json, name='show_json'), 
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'), 
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    path('user_json/<int:id>/', get_product_json_by_user_id, name='get_product_json_by_user_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('delete_product/<int:id>/', delete_product, name='delete_product'),
    path('increase_amount/<int:id>/', increase_amount, name='increase_amount'),
    path('decrease_amount/<int:id>/', decrease_amount, name='decrease_amount'),
    path('get_product_json/', get_product_json, name='get_product_json'),
    path('create-ajax/', add_product_ajax, name='add_product_ajax'),
    path('create-flutter/', create_product_flutter, name='create_product_flutter'),
]

