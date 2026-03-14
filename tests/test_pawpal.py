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
