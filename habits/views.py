from django.shortcuts import get_object_or_404, redirect, render

from .models import Habit
from datetime import date


def habit_list(request):
    habits = Habit.objects.all()

    return render(request, "habits/habit_list.html", {
        "habits": habits,
        "today": date.today(),
    })


def add_habit(request):
    if request.method == "POST":
        name = request.POST.get("name")

        if name:
            Habit.objects.create(name=name)

    return redirect("habit_list")


def complete_habit(request, habit_id):
    habit = get_object_or_404(Habit, id=habit_id)

    if request.method == "POST":
        habit.complete()

    return redirect("habit_list")

def undo_completion(request, habit_id):
    habit=get_object_or_404(Habit, id=habit_id)

    if request.method=="POST":
        habit.undo_completion()

    return redirect("habit_list")

def delete_habit(request, habit_id):
    habit = get_object_or_404(Habit, id=habit_id)

    if request.method == "POST":
        habit.delete()

    return redirect("habit_list")