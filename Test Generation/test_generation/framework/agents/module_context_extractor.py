"""Module Context Extractor Agent: distills global navigation and module lists into a per-module context."""

import json
from importlib import resources
from typing import Any, Dict, List

from test_generation.framework.agents.base import BaseAgent

_PROMPT_TEMPLATE: str = (
    resources.files("test_generation.prompts")
    .joinpath("module_context_extractor.md")
    .read_text(encoding="utf-8")
)


class ModuleContextExtractorAgent(BaseAgent):

    @property
    def name(self) -> str:
        return "Module-Context-Extractor"

    @property
    def system_prompt(self) -> str:
        return _PROMPT_TEMPLATE

    # ------------------------------------------------------------------
    # Public interface
    # ------------------------------------------------------------------

    def run(
        self,
        module_title: str,
        description: str,
        navigation_overview: str,
        all_modules: List[str],
    ) -> Dict[str, Any]:
        return self.call_llm_json(
            self._build_prompt(module_title, description, navigation_overview, all_modules),
            temperature=0.1,
            max_tokens=1024,
            reasoning_effort="low",
        )

    async def arun(
        self,
        module_title: str,
        description: str,
        navigation_overview: str,
        all_modules: List[str],
    ) -> Dict[str, Any]:
        return await self.acall_llm_json(
            self._build_prompt(module_title, description, navigation_overview, all_modules),
            temperature=0.1,
            max_tokens=1024,
            reasoning_effort="low",
        )

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    @staticmethod
    def _build_prompt(
        module_title: str,
        description: str,
        navigation_overview: str,
        all_modules: List[str],
    ) -> str:
        all_modules_str = "\n".join(f"- {m}" for m in all_modules)
        
        return (
            f"<navigation_overview>\n{navigation_overview}\n</navigation_overview>\n\n"
            f"<all_modules>\n{all_modules_str}\n</all_modules>\n\n"
            f"<module_title>\n{module_title}\n</module_title>\n\n"
            f"<module_description>\n{description}\n</module_description>"
        )
