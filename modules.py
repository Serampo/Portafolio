
import json
import os
from datetime import datetime
# Crear archivo si no existe
def tasks():
    file_path = 'tasks.json'
    if not os.path.exists(file_path):
        with open(file_path, 'w') as f:
            json.dump([ ], f)
            print(f"Archivo '{file_path}' creado con lista vacía.")
    else:
        print(f"El archivo '{file_path}' ya existe.")


# Leer tareas
def read():
    with open('tasks.json', 'r') as f:
        data = json.load(f)
        print("Tareas actuales:", data)
    return data

# Escribir tareas
def write(tasks):
    with open('tasks.json', 'w') as f:
        json.dump(tasks, f)
        print(f"Archivo actualizado con: {tasks}")

# Agregar nueva tarea
def add():
    tasks_list = read()
    task_id = len(tasks_list) + 1  # ID incremental
    task_name = input("Nombre de la tarea: ")
    task_priority = input("Prioridad (Alta/Media/Baja): ")
    task_status = input("Estado (Pendiente/Completada): ")
    create_date = datetime.now().isoformat()
    update_date = datetime.now().isoformat()
    # Crear diccionario con los campos
    new_task = {
        "taskid": task_id,
        "taskname": task_name,
        "taskpriority": task_priority,
        "taskstatus": task_status,
        "createdate": create_date,
        "updatedate": update_date
    }

    tasks_list.append(new_task)
    write(tasks_list)
    print(f"Tarea '{task_name}' agregada exitosamente.")

def Update (task_id):
    tasks_list = read()
    for task in tasks_list:
        if task["taskid"] == task_id:
            task["taskname"] = input("Nuevo nombre de la tarea: ")
            task["taskpriority"] = input("Nueva prioridad (Alta/Media/Baja): ")
            task["taskstatus"] = input("Nuevo estado (Pendiente/Completada/En Progreso): ")
            task["updatedate"] = datetime.now().isoformat()
            write(tasks_list)
            print(f"Tarea con ID {task_id} actualizada exitosamente.")
            return
    print(f"No se encontró ninguna tarea con ID {task_id}.")



#Eliminar tarea y reordenar IDs

def delete(task_id):
    tasks_list = read()
    new_list = [task for task in tasks_list if task["taskid"] != task_id]

    if len(new_list) == len(tasks_list):
        print(f"No se encontró ninguna tarea con ID {task_id}.")
    else:
        # Si hay tareas restantes, reordenar IDs
        for index, task in enumerate(new_list, start=1):
            task["taskid"] = index

        write(new_list)
        if not new_list:
            print("Todas las tareas fueron eliminadas. Lista vacía.")
        else:
            print(f"Tarea con ID {task_id} eliminada y IDs reordenados.")
    delete_tasks=int(input("Ingrese el ID de la tarea a eliminar: "))

def done_tasks():
    tasks_list = read()
    for task in tasks_list:
        if task["taskstatus"].lower() == "completada":
            print(f"Tarea ID {task['taskid']}: {task['taskname']} - Estado: {task['taskstatus']}")
    return tasks_list

def pending_tasks():
    tasks_list = read()
    for task in tasks_list:
        if task["taskstatus"].lower() == "pendiente":
            print(f"Tarea ID {task['taskid']}: {task['taskname']} - Estado: {task['taskstatus']}")
    return tasks_list

def inprogress_tasks():
    tasks_list = read()
    for task in tasks_list:
        if task["taskstatus"].lower() == "en progreso":
            print(f"Tarea ID {task['taskid']}: {task['taskname']} - Estado: {task['taskstatus']}")
    return tasks_list
