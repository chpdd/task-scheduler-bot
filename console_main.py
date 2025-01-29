from tasks_allocation_package.classes import Planner

import datetime as dt
import os.path

if __name__ == "__main__":
    tasks_file_name = os.path.join("data_files", "tasks6.txt")
    days_file_name = os.path.join("data_files", "days6.txt")

    default_task_work_hours = 2
    default_day_work_hours = 4

    # start_date = dt.date.today()_
    # start_date = dt.date(day=16, month=12, year=2024)
    start_date = dt.date(day=1, month=1, year=2024)
    planner = Planner(start_date=start_date, dflt_day_work_hours=default_day_work_hours,
                      dflt_task_work_hours=default_task_work_hours)
    planner.read_tasks_days_from_file(tasks_file_name, days_file_name)

    # planner.interest_importance_sort()
    planner.print_present_tasks_rus()
    planner.procrastinate_sort_v1()
    planner.print_failed_tasks_rus()
    planner.print_calendar_with_schedule_rus()
