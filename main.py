from pawpal_system import Owner, Pet, Task, Scheduler


def main():
    # Create an owner
    owner = Owner("Alex")

    # Create two pets
    dog = Pet("Buddy", "Dog")
    cat = Pet("Luna", "Cat")

    # Add pets to the owner
    owner.add_pet(dog)
    owner.add_pet(cat)

    # Add tasks to pets
    dog.add_task(Task("Morning feeding", "08:00", "daily"))
    dog.add_task(Task("Afternoon walk", "14:00", "daily"))
    cat.add_task(Task("Evening medication", "19:00", "daily"))

    # Create scheduler
    scheduler = Scheduler(owner)

    # Print Today's Schedule sorted by time by pet
    print(f"\nToday's Schedule for {owner.name}")
    print("-" * 40)
    for pet in owner.pets:
        pet_tasks = scheduler.sort_by_time(pet.tasks)
        for task in pet_tasks:
            print(f"{task.time} - {pet.name} - {task.description}")
    print("-" * 40)

    # Test conflict detection
    dog.add_task(Task("Lunch - Buddy", "12:00", "once"))
    cat.add_task(Task("Lunch - Luna", "12:00", "once"))

    print("\nChecking for conflicts...")
    conflicts = scheduler.detect_conflicts(scheduler.get_schedule())
    if not conflicts:
        print("No conflicts detected.")
    else:
        for c in conflicts:
            print(c)

    # Test marking a daily task complete and rescheduling
    evening_walk = Task("Evening walk", "20:00", "daily")
    new_task = evening_walk.mark_complete()

    # Safely access possible attribute names for completion and due date
    original_status = evening_walk.is_complete
    due_date = getattr(new_task, "due_date", None)

    print(
        f"\nMarked original task '{evening_walk.description}' is_complete: {evening_walk.is_complete}")

    print(f"Rescheduled task due_date: {due_date}")


if __name__ == "__main__":
    main()
