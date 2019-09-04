"""webapps URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from ResumeForest import views
urlpatterns = [
    path('', views.login_action, name='login'),
    path('logout', views.logout_action, name='logout'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
    path('register', views.register_action, name='register'),
    path('employee_home', views.employee_home_action, name='employee_home'),
    path('employer_home', views.employer_home_action, name='employer_home'),
    path('employer_profile', views.employer_profile_action, name="employer_profile"),
    path('employer_search_result', views.employer_search_result_action, name='employer_search_result'),
    path('employer_update_profile', views.employer_update_profile, name="employer_update_profile"),
    path('check_resume/<int:id>', views.check_resume, name="check_resume"),
    path('send_interest/<int:id>', views.send_interest, name='send_interest'),
    path('conntect_all', views.connect_all, name='connect_all'),

    # paths related to resume and profile
    path('info_collect', views.info_collect_action, name='info_collect'),
    path('resume_generate', views.resume_generate_action, name='resume_generate'),
    path('resume_delete/<int:id>', views.delete_action, name='resume_delete'),
    path('set_master/<int:id>', views.set_master_action, name='set_master'),
    path('contact_info_update', views.contact_info_update_action, name='contact_info_update'),
    path('submit_education', views.submit_education_action, name='submit_education'),
    path('submit_experience', views.submit_experience_action, name='submit_experience'),
    path('submit_project', views.submit_project_action, name='submit_project'),
    path('submit_skill', views.submit_skill_action, name='submit_skill'),
    path('delete_block', views.delete_block_action, name='delete_block'),
    path('get_jpg/<int:id>', views.get_jpg, name='get_jpg'),
    path('get_pdf/<int:id>', views.get_pdf, name='get_pdf'),

]
