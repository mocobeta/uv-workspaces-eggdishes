from abc import ABC, abstractmethod

class EggDish(ABC):
    name: str
    
    @abstractmethod
    def recipe(self) -> str:
        """Return the recipe for the egg dish."""
        pass
