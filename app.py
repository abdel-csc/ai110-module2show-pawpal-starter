import streamlit as st
from pawpal_system import Owner, Pet, Task, Scheduler

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")
st.title("🐾 PawPal+")

# Session state setup
if "owner" not in st.session_state:
    st.session_state.owner = None
if "pets" not in st.session_state:
    st.session_state.pets = []

# Owner and Pet setup
st.subheader("Owner & Pet Setup")
owner_name = st.text_input("Owner name", value="Alex")
pet_name = st.text_input("Pet name", value="Buddy")
species = st.selectbox("Species", ["Dog", "Cat", "Other"])

if st.button("Add Pet"):
    if st.session_state.owner is None:
        st.session_state.owner = Owner(owner_name)
    new_pet = Pet(pet_name, species)
    st.session_state.owner.add_pet(new_pet)
    st.session_state.pets.append(pet_name)
    st.success(f"Added {pet_name} the {species}!")

if st.session_state.pets:
    st.write("Your pets:", st.session_state.pets)

st.divider()

# Task setup
st.subheader("Add a Task")
selected_pet = st.selectbox(
    "Select pet", st.session_state.pets if st.session_state.pets else ["No pets yet"])
task_desc = st.text_input("Task description", value="Morning walk")
task_time = st.text_input("Time (HH:MM)", value="08:00")
task_freq = st.selectbox("Frequency", ["once", "daily", "weekly"])

if st.button("Add Task"):
    if st.session_state.owner is None:
        st.warning("Please add a pet first!")
    else:
        for pet in st.session_state.owner.pets:
            if pet.name == selected_pet:
                pet.add_task(Task(task_desc, task_time, task_freq))
                st.success(f"Added task '{task_desc}' to {selected_pet}!")

st.divider()

# Generate schedule
st.subheader("Today's Schedule")
if st.button("Generate Schedule"):
    if st.session_state.owner is None:
        st.warning("No pets added yet!")
    else:
        scheduler = Scheduler(st.session_state.owner)
        sorted_tasks = scheduler.sort_by_time(scheduler.get_schedule())

        if not sorted_tasks:
            st.info("No tasks scheduled yet!")
        else:
            schedule_data = [{"Time": t.time, "Task": t.description,
                              "Frequency": t.frequency} for t in sorted_tasks]
            st.table(schedule_data)

        conflicts = scheduler.detect_conflicts(scheduler.get_schedule())
        for c in conflicts:
            st.warning(c)
