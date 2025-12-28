DEMO_MODE = True

class LanguageModel:
    def interpret(self, user_input):
        if not DEMO_MODE:
            print("→ LLM interpreting user intent")
        return user_input.lower()


class CalendarTool:
    def __init__(self):
        self.events = []

    def schedule(self, task):
        event = {
            "task": task["name"],
            "duration": task["duration"],
            "time": task["time_hint"],
            "priority": task["priority"]
        }
        self.events.append(event)

        if not DEMO_MODE:
            print("→ Calendar updated")
        print(f"→ Event added: {event}")


class ProductivityAgent:
    def __init__(self):
        self.tasks = []
        self.calendar = CalendarTool()
        self.llm = LanguageModel()

    def run(self, user_input):
        if "next" in user_input.lower():
            self.suggest_next_task()
            return

        if not DEMO_MODE:
            print("→ Understanding user goal")
        task = self.interpret_task(user_input)

        if not DEMO_MODE:
            print("→ Planning tasks")
        self.tasks.append(task)

        if not DEMO_MODE:
            print("→ Scheduling task")
        self.schedule_task(task)

        if not DEMO_MODE:
            print("→ Reflecting on outcome")
        self.reflect()

    def interpret_task(self, user_input):
        if not DEMO_MODE:
            print("→ Extracting task details")

        text = self.llm.interpret(user_input)

        if any(word in text for word in ["dsa", "coding"]):
            name = "coding"
        elif any(word in text for word in ["exam", "assignment", "study", "revision"]):
            name = "studying"
        else:
            name = "personal task"


        duration = 2
        for word in text.split():
            if word.isdigit():
                duration = int(word)
                break

        if "before dinner" in text:
            time_hint = "before dinner"
        elif "after lunch" in text:
            time_hint = "after lunch"
        else:
            time_hint = "today"

        if any(word in text for word in ["study", "exam", "assignment", "revision"]):
            priority = "high"
        elif "urgent" in text:
            priority = "high"
        else:
            priority = "medium"

        print(f"→ Task: {name}")
        print(f"→ Duration: {duration} hours")
        print(f"→ Time preference: {time_hint}")
        print(f"→ Assigned priority: {priority}")

        return {
            "raw_task": user_input.strip(),
            "name": name,
            "duration": duration,
            "time_hint": time_hint,
            "priority": priority
        }

    def schedule_task(self, task):
        if task["priority"] == "high":
            print("→ High priority task detected")
        else:
            print("→ Normal priority task detected")

        self.calendar.schedule(task)

    def suggest_next_task(self):
        if not self.tasks:
            print("→ No tasks found in memory")
            print("→ Note: Memory resets when the agent restarts")
            return

        priority_score = {"high": 2, "medium": 1}

        best_task = max(
            self.tasks,
            key=lambda t: (priority_score[t["priority"]], t["duration"])
        )

        print(
            f"→ Suggested next task: {best_task['raw_task']} "
            f"({best_task['priority']} priority, "
            f"{best_task['duration']} hours, "
            f"{best_task['time_hint']})"
        )

        print("→ Reviewing stored tasks")
        for task in self.tasks:
            print(
                f"→ Pending task: {task['name']} "
                f"({task['priority']} priority)"
            )

    def reflect(self):
        if not self.tasks:
            print("→ Reflection: No tasks were managed")
        else:
            print(f"→ Reflection: {len(self.tasks)} task(s) managed successfully")

if __name__ == "__main__":
    agent = ProductivityAgent()

    while True:
        user_input = input("\nUser: ")

        if user_input.lower() in ["exit", "quit"]:
            print("→ Exiting agent")
            break

        agent.run(user_input)