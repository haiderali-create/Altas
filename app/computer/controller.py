import subprocess
import time
import pyautogui
import psutil
from .application_discovery import ApplicationDiscovery

class ComputerController:
    def __init__(self):
        self.discovery = ApplicationDiscovery()

    def launch_application(self, query: str):
        matches = self.discovery.find(query)
        if not matches:
            return False, f"I couldn't find {query} on this computer.", {}
        app = matches[0]
        try:
            subprocess.Popen([app.path], shell=False)
            time.sleep(1)
            running = any(p.info.get('name','').lower() == app.name.lower()+'.exe' for p in psutil.process_iter(['name']))
            return running, f"Opened {app.name}." if running else f"Started {app.name}, but could not verify it is running yet.", {'application': app.__dict__}
        except Exception as e:
            return False, f"Failed to launch {app.name}: {e}", {}

    def screenshot(self, path='altas_screen.png'):
        image = pyautogui.screenshot()
        image.save(path)
        return True, 'Screenshot captured.', {'path': path}

    def click(self, x: int, y: int):
        pyautogui.click(x, y)
        return True, 'Clicked.', {}

    def type_text(self, text: str):
        pyautogui.write(text, interval=0.01)
        return True, 'Typed text.', {}

    def press_key(self, key: str):
        pyautogui.press(key)
        return True, f'Pressed {key}.', {}

    def hotkey(self, keys: list[str]):
        pyautogui.hotkey(*keys)
        return True, 'Shortcut sent.', {}
