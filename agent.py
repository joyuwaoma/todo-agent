from google.genai.agents import Agent

def add_task(task: str) -> dict:
    """Adds a new task to the to-do list."""
    tasks.append({"task": task, "done": False})
    return {"message": f"Task '{task}' added successfully!"}

def list_tasks() -> dict:
    """Lists all current tasks."""
    if not tasks:
        return {"message": "No tasks yet!"}
    return {"tasks": tasks}

def complete_task(task: str) -> dict:
    """Marks a task as complete."""
    for t in tasks:
        if t["task"].lower() == task.lower():
            t["done"] = True
            return {"message": f"Task '{task}' marked as complete!"}
    return {"message": f"Task '{task}' not found."}

def delete_task(task: str) -> dict:
    """Deletes a task from the list."""
    for t in tasks:
        if t["task"].lower() == task.lower():
            tasks.remove(t)
            return {"message": f"Task '{task}' deleted!"}
    return {"message": f"Task '{task}' not found."}

# In-memory task storage
tasks = []

# Define the agent
root_agent = Agent(
    name="todo_agent",
    model="gemini-2.0-flash",
    description="A helpful productivity agent that manages your to-do list.",
    instruction="""
        You are a friendly productivity assistant. 
        You help users manage their daily tasks.
        You can add, list, complete, and delete tasks.
        Always be encouraging and helpful!
    """,
    tools=[add_task, list_tasks, complete_task, delete_task],
)
