"""Test-runner compatibility for the pinned Direct Mode SDK on native Windows.

genlayer-test==0.29.2 replaces fd 0 with a temporary file and immediately
unlinks that file. Windows keeps the duplicated fd open, so the unlink raises
WinError 32 before any contract code is loaded. Keep the file until the pinned
runner restores stdin, then remove it. This is test infrastructure only; it
does not change contract behavior or production deployment code.
"""

from __future__ import annotations

import os
import tempfile


def _install_windows_fd0_compat() -> None:
    if os.name != "nt":
        return

    from gltest.direct import loader, vm as vm_module

    if getattr(loader, "_entrench_windows_fd0_patch", False):
        return

    def inject_message_to_fd0(vm) -> None:
        from genlayer.py import calldata
        from genlayer.py.types import Address

        sender_addr = vm.sender
        if isinstance(sender_addr, bytes):
            sender_addr = Address(sender_addr)

        contract_addr = vm._contract_address
        if isinstance(contract_addr, bytes):
            contract_addr = Address(contract_addr)

        origin_addr = vm.origin
        if isinstance(origin_addr, bytes):
            origin_addr = Address(origin_addr)

        message_data = {
            "contract_address": contract_addr,
            "sender_address": sender_addr,
            "origin_address": origin_addr,
            "stack": [],
            "value": vm._value,
            "datetime": vm._datetime,
            "is_init": False,
            "chain_id": vm._chain_id,
            "entry_kind": 0,
            "entry_data": b"",
            "entry_stage_data": None,
        }

        fd, path = tempfile.mkstemp()
        try:
            os.write(fd, calldata.encode(message_data))
            os.lseek(fd, 0, os.SEEK_SET)
            vm._original_stdin_fd = os.dup(0)
            os.dup2(fd, 0)
            vm._entrench_message_temp_path = path
        except Exception:
            try:
                os.close(fd)
            finally:
                try:
                    os.unlink(path)
                except OSError:
                    pass
            raise
        finally:
            os.close(fd)

    original_cleanup = vm_module.VMContext._cleanup_after_deactivate

    def cleanup_after_deactivate(vm) -> None:
        path = getattr(vm, "_entrench_message_temp_path", None)
        try:
            original_cleanup(vm)
        finally:
            if path:
                try:
                    os.unlink(path)
                except FileNotFoundError:
                    pass
                vm._entrench_message_temp_path = None

    loader._inject_message_to_fd0 = inject_message_to_fd0
    vm_module.VMContext._cleanup_after_deactivate = cleanup_after_deactivate
    loader._entrench_windows_fd0_patch = True


_install_windows_fd0_compat()
