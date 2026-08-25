from app.agent.engine import TaskEngine

class AltasCLI:
    def __init__(self):
        self.engine = TaskEngine()

    async def run(self):
        print('ALTAS ready. Type a goal, or STOP. Type exit to quit.')
        while True:
            text = input('ALTAS> ').strip()
            if not text:
                continue
            if text.lower() in {'exit', 'quit'}:
                break
            if text.upper() in {'STOP', 'CANCEL', 'ALTAS STOP'}:
                self.engine.cancel.cancel()
                print('ALTAS: Cancellation requested.')
                continue
            result = await self.engine.run_goal(text)
            print('ALTAS:', result.message)
