from django.urls import path

from . import views

urlpatterns = [
    # ex: /immo/5/
    path('<int:scenario_id>/', views.load_scenario, name='load_scenario'),
    # ex: /immo/5/save/
    path('<int:scenario_id>/save/', views.save_scenario, name='save_scenario'),
    # ex: /immo/all/
    path('all/', views.all_scenarios, name='all_scenarios'),
    # ex: /immo/create/
    path('create/', views.create_scenario, name='create_scenario'),

]