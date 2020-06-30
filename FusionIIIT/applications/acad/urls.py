from django.conf.urls import url,include
from django.contrib import admin
from . import views

urlpatterns = [
    
    url(r'^$', views.main),
    url(r'^admin/', views.acad_admin),
    url(r'^add_course/', views.add_course,name="add_courses"),
    url(r'^add_curriculum/', views.add_curriculum),
    url(r'^add_mtech_curriculum/', views.add_mtech_curriculum),
    url(r'^get_batch_curriculum/', views.get_batch_curriculum),
    url(r'^get_mtech_curriculum/', views.get_mtech_curriculum),
    url(r'^set_batch_semester/', views.set_batch_semester),
    url(r'^set_mtech_semester/', views.set_mtech_semester),
    url(r'^get_batch_semesters/', views.get_batch_semesters),
    url(r'^get_mtech_semesters/', views.get_mtech_semesters),
    url(r'^add_curr_course/', views.add_curr_course),
    url(r'^add_mtech_curr_course/', views.add_mtech_curr_course),
    url(r'^view_btech/', views.view_btech_curriculum),
    url(r'^view_mtech/', views.view_mtech),
    url(r'^send/', views.send_list),

]
