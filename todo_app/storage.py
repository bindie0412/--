"""Storage abstractions for persisting application state."""

import json
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Dict, List

from .config import DATA_DIR, DATA_FILE


class CloudStorage(ABC):
    """Defines the contract for cloud-capable storage backends."""

    @abstractmethod
    def load_state(self) -> Dict:
        """Load state from the backing store."""

    @abstractmethod
    def save_state(self, state: Dict) -> None:
        """Persist state to the backing store."""


class LocalJSONStorage(CloudStorage):
    """Simple JSON-based storage simulating a cloud provider."""

    def __init__(self, path: Path = DATA_FILE):
        self.path = path
        DATA_DIR.mkdir(parents=True, exist_ok=True)

    def load_state(self) -> Dict:
        if not self.path.exists():
            return {"projects": [], "items": [], "notifications": []}
        with self.path.open("r", encoding="utf-8") as handle:
            return json.load(handle)

    def save_state(self, state: Dict) -> None:
        with self.path.open("w", encoding="utf-8") as handle:
            json.dump(state, handle, ensure_ascii=False, indent=2)


def to_serializable(collection: List) -> List[Dict]:
    """Convert Pydantic models into dictionaries for storage."""

    return [item.dict() for item in collection]
