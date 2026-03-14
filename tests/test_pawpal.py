from datetime import date, timedelta
from pawpal_system import Owner, Pet, Task, Scheduler
import sys
import os
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))


def test_mark_complete():
    task = Task("Morning feeding", "08:00", "daily")
    assert task.is_complete == False
    task.mark_complete()
    assert task.is_complete == True


def test_add_task_increases_count():
    pet = Pet("Buddy", "Dog")
    assert len(pet.get_tasks()) == 0
    pet.add_task(Task("Walk", "14:00", "daily"))
    assert len(pet.get_tasks()) == 1


def test_pet_with_no_tasks():
    pet = Pet("Empty", "Cat")
    assert len(pet.get_tasks()) == 0


def test_sort_by_time():
    owner = Owner("Alice")
    pet = Pet("Buddy", "Dog")
    owner.add_pet(pet)
    pet.add_task(Task("t1", "14:00", "daily"))
    pet.add_task(Task("t2", "08:00", "daily"))
    pet.add_task(Task("t3", "19:00", "daily"))
    scheduler = Scheduler(owner)
    sorted_tasks = scheduler.sort_by_time(scheduler.get_schedule())
    times = [t.time for t in sorted_tasks]
    assert times == ["08:00", "14:00", "19:00"]


def test_recurring_task():
    task = Task("Daily feed", "08:00", "daily")
    new_task = task.mark_complete()
    assert new_task is not None
    assert new_task.due_date == date.today() + timedelta(days=1)


def test_conflict_detection():
    owner = Owner("Sam")
    pet1 = Pet("Rex", "Dog")
    pet2 = Pet("Mittens", "Cat")
    owner.add_pet(pet1)
    owner.add_pet(pet2)
    pet1.add_task(Task("Lunch walk", "12:00", "once"))
    pet2.add_task(Task("Vet meds", "12:00", "once"))
    scheduler = Scheduler(owner)
    conflicts = scheduler.detect_conflicts(scheduler.get_schedule())
    assert len(conflicts) > 0
