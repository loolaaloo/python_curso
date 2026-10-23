completed_tasks = 0

def complete_task():
    global completed_tasks
    completed_tasks += 1
    print("Tareas compeltadas:", completed_tasks)
complete_task()
complete_task()
complete_task()
print(completed_tasks)