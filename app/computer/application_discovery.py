import os
import re
from pathlib import Path
from dataclasses import dataclass
from typing import Iterable

@dataclass
class Application:
    name: str
    path: str
    source: str

class ApplicationDiscovery:
    def __init__(self):
        self.roots = [
            Path(os.environ.get('ProgramFiles', r'C:\\Program Files')),
            Path(os.environ.get('ProgramFiles(x86)', r'C:\\Program Files (x86)')),
            Path(os.environ.get('LOCALAPPDATA', Path.home() / 'AppData/Local')),
        ]

    def discover(self, limit: int = 5000) -> list[Application]:
        found: dict[str, Application] = {}
        for root in self.roots:
            if not root.exists():
                continue
            try:
                for path in root.rglob('*.exe'):
                    key = str(path).lower()
                    if key not in found:
                        found[key] = Application(path.stem, str(path), 'filesystem')
                    if len(found) >= limit:
                        return list(found.values())
            except (PermissionError, OSError):
                continue
        return list(found.values())

    def find(self, query: str) -> list[Application]:
        q = re.sub(r'[^a-z0-9]+', '', query.lower())
        matches = []
        for app in self.discover():
            name = re.sub(r'[^a-z0-9]+', '', app.name.lower())
            if q in name or name in q:
                matches.append(app)
        return matches
