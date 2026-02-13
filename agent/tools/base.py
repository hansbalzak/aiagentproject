from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable, Dict

from agent.exceptions import ToolError


ToolFunc = Callable[..., Any]


@dataclass
class ToolSpec:
    name: str
    description: str
    func: ToolFunc


class ToolRegistry:
    """
    Simple registry used by the orchestrator:
      registry.call("read_file", path="x.txt")
    """

    def __init__(self) -> None:
        self._tools: Dict[str, ToolSpec] = {}

    def register(self, name: str, func: ToolFunc, description: str = "") -> None:
        if not name or not isinstance(name, str):
            raise ToolError("Tool name must be a non-empty string")
        self._tools[name] = ToolSpec(name=name, description=description, func=func)

    def call(self, name: str, **kwargs: Any) -> Any:
        spec = self._tools.get(name)
        if not spec:
            raise ToolError(f"Unknown tool: {name}")
        try:
            return spec.func(**kwargs)
        except TypeError as e:
            raise ToolError(f"Bad args for tool '{name}': {e}")
        except Exception as e:
            raise ToolError(f"Tool '{name}' failed: {e}")

    def list_tools(self) -> Dict[str, str]:
        return {name: spec.description for name, spec in self._tools.items()}
