from dataclasses import dataclass


@dataclass(frozen=True)
class RetrievalPolicy:
    max_nodes: int = 3
    max_chars: int = 6000

    def __post_init__(self):
        if not 1 <= self.max_nodes <= 20:
            raise ValueError("max_nodes must be between 1 and 20")
        if not 500 <= self.max_chars <= 10000:
            raise ValueError("max_chars must be between 500 and 10000")
