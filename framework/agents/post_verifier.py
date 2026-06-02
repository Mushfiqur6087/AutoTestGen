import json
from importlib import resources
from typing import Any, Dict

from autospectest.framework.agents.base import BaseAgent

_GATE_PROMPT = resources.files("autospectest.prompts").joinpath("state_mutation_gate.md").read_text(encoding="utf-8")
_VERIFY_PROMPT = resources.files("autospectest.prompts").joinpath("post_verification.md").read_text(encoding="utf-8")

class StateMutationGateAgent(BaseAgent):
    @property
    def name(self) -> str:
        return "State-Mutation-Gate"

    @property
    def system_prompt(self) -> str:
        return _GATE_PROMPT

    async def arun(self, test_case: Dict[str, Any]) -> Dict[str, Any]:
        prompt = (
            "<test_case>\n"
            f"{json.dumps(test_case, indent=2)}\n"
            "</test_case>"
        )
        return await self.acall_llm_json(
            user_prompt=prompt,
            temperature=0.0,
            max_tokens=256
        )

    def run(self, test_case: Dict[str, Any]) -> Dict[str, Any]:
        raise NotImplementedError("Use arun")

class PostVerificationAgent(BaseAgent):
    @property
    def name(self) -> str:
        return "Post-Verifier"

    @property
    def system_prompt(self) -> str:
        return _VERIFY_PROMPT

    async def arun(self, description: str, test_case: Dict[str, Any]) -> Dict[str, Any]:
        prompt = (
            "<description>\n"
            f"{description}\n"
            "</description>\n\n"
            "<test_case>\n"
            f"{json.dumps(test_case, indent=2)}\n"
            "</test_case>"
        )
        return await self.acall_llm_json(
            user_prompt=prompt,
            temperature=0.2,
            max_tokens=1024
        )

    def run(self, description: str, test_case: Dict[str, Any]) -> Dict[str, Any]:
        raise NotImplementedError("Use arun")
