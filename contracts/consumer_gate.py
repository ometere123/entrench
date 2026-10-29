# { "Depends": "py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6" }
"""Small independent consumer proving that stale constitutional heads are unusable."""
from genlayer import *


@gl.contract_interface
class IEntrench:
    class View:
        def is_executed(self, pid: u256, expected_head: str) -> bool: ...


class ConstitutionalActionGate(gl.Contract):
    registry: Address
    proposal_id: u256
    expected_head: str
    performed: bool

    def __init__(self, registry: Address, proposal_id: u256, expected_head: str):
        self.registry = registry
        self.proposal_id = proposal_id
        self.expected_head = expected_head
        self.performed = False

    @gl.public.write
    def perform(self) -> None:
        if self.performed:
            raise gl.vm.UserError("ONE_SHOT")
        registry = IEntrench(self.registry)
        if not registry.view().is_executed(self.proposal_id, self.expected_head):
            raise gl.vm.UserError("AMENDMENT_NOT_CANONICAL")
        self.performed = True

    @gl.public.view
    def did_perform(self) -> bool:
        return self.performed
