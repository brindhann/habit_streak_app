from django.urls import path

from . import views


urlpatterns = [
    path("", views.habit_list, name="habit_list"),
    path("add/", views.add_habit, name="add_habit"),
    path("complete/<int:habit_id>/", views.complete_habit, name="complete_habit"),
    path("delete/<int:habit_id>/", views.delete_habit, name="delete_habit"),
    path("undo/<int:habit_id>/", views.undo_completion, name="undo_completion"),
]