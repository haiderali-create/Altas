from app.computer.controller import ComputerController
from app.filesystem.operations import Filesystem
from .cancellation import CancellationToken
from .models import StepResult, TaskResult

class TaskEngine:
    def __init__(self):
        self.computer = ComputerController()
        self.filesystem = Filesystem()
        self.cancel = CancellationToken()
        self.context = []

    async def execute_direct(self, action: str, arguments: dict):
        if self.cancel.cancelled:
            return StepResult(action=action, success=False, message='Cancelled.')
        table = {
            'launch_application': lambda: self.computer.launch_application(arguments['application']),
            'screenshot': lambda: self.computer.screenshot(arguments.get('path', 'altas_screen.png')),
            'click': lambda: self.computer.click(arguments['x'], arguments['y']),
            'type': lambda: self.computer.type_text(arguments['text']),
            'press_key': lambda: self.computer.press_key(arguments['key']),
            'hotkey': lambda: self.computer.hotkey(arguments['keys']),
            'list_files': lambda: self.filesystem.list_dir(arguments['path']),
            'search_files': lambda: self.filesystem.search(arguments['root'], arguments.get('pattern', '*')),
        }
        if action not in table:
            return StepResult(action=action, success=False, message=f'Unknown tool action: {action}')
        success, message, data = table[action]()
        return StepResult(action=action, success=success, message=message, data=data)

    async def run_goal(self, goal: str):
        self.cancel.reset()
        self.context.append({'role': 'user', 'content': goal})
        return TaskResult(success=False, message='AI planner is not configured yet. Add OPENAI_API_KEY to enable natural-language planning.', steps=[])
