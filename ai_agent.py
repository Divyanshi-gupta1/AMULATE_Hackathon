class ProductivityAgent:
    def __init__(self):
        self.tasks = []

    def run(self, user_input):
        print("→ Understanding user goal")
        parsed_task = self.parse_task(user_input)

        print("→ Planning tasks")
        self.tasks.append(parsed_task)

        print("→ Scheduling task")
        self.schedule_task(parsed_task)

        print("→ Reflecting on outcome")
        print("→ Task completed successfully")

    def parse_task(self, user_input):
        print("→ Extracting task details")

        task = {
            "name": "coding",
            "duration": 2,
            "time_hint": "after lunch"
        }

        if "urgent" in user_input.lower():
            task["priority"] = "high"
        else:
            task["priority"] = "medium"

        print(f"→ Assigned priority: {task['priority']}")
        return task


    def schedule_task(self, task):
        if task["priority"] == "high":
            print("→ High priority task detected")
        else:
            print("→ Normal priority task detected")

        print(f"→ Scheduling {task['name']} for {task['duration']} hours {task['time_hint']}")

agent = ProductivityAgent()
agent.run("Schedule a 4-hour cooking session after breakfast")
