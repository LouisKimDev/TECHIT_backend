from django.urls import path
from .views import post_create_view, post_delete_view, \
    post_detail_view, post_list_view, post_update_view

app_name = 'posts'

urlpatterns = [
    # 네임을 쓰면 ''안에 들어갈 내용이 바뀌어도 html이 post-list를 자동으로 참조함
    path('', post_list_view, name = 'post-list'),
    path('create/', post_create_view, name = 'post-create'),
    path('<int:id>/', post_detail_view, name = 'post-detail'),
    path('<int:id>/delete', post_delete_view, name = 'post-delete'),
    path('<int:id>/edit', post_update_view, name = 'post-update')
]