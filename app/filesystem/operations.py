from pathlib import Path

class Filesystem:
    def search(self, root: str, pattern: str='*', limit: int=100):
        base = Path(root).expanduser()
        results = []
        try:
            for item in base.rglob(pattern):
                results.append({'path': str(item), 'size': item.stat().st_size if item.is_file() else None})
                if len(results) >= limit:
                    break
            return True, f'Found {len(results)} items.', {'items': results}
        except Exception as e:
            return False, str(e), {}

    def list_dir(self, path: str):
        try:
            items = [{'name': p.name, 'path': str(p), 'is_dir': p.is_dir()} for p in Path(path).expanduser().iterdir()]
            return True, f'Found {len(items)} items.', {'items': items}
        except Exception as e:
            return False, str(e), {}
