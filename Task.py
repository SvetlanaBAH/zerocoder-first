class Task:
    def __init__(self, description, due_date):
        self.description = description
        self.due_date = due_date
        self.completed = False

    def mark_as_completed(self):
        self.completed = True

    def __str__(self):
        status = "Выполнено" if self.completed else "Не выполнено"
        return f"Задача: {self.description}, Срок: {self.due_date}, Статус: {status}"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, due_date):
        task = Task(description, due_date)
        self.tasks.append(task)

    def mark_task_as_completed(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].mark_as_completed()
        else:
            print("Ошибка: Индекс задачи вне диапазона.")

    def show_current_tasks(self):
        print("Текущие задачи (не выполненные):")
        for index, task in enumerate(self.tasks):
            if not task.completed:
                print(f"{index}: {task}")


# Пример использования
if __name__ == "__main__":
    manager = TaskManager()

    # Добавление задач
    manager.add_task("Купить продукты", "2023-10-10")
    manager.add_task("Сделать домашнее задание", "2023-10-15")

    # Показать текущие задачи
    manager.show_current_tasks()

    # Отметить задачу как выполненную
    manager.mark_task_as_completed(0)

    # Показать текущие задачи после завершения одной из них
    manager.show_current_tasks()