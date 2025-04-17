"""
The code is base on https://github.com/Pointcept/Pointcept
"""

from utils.registry import Registry


HOOKS = Registry("hooks")


def build_hooks(cfg):
    hooks = []
    for hook_cfg in cfg:
        hooks.append(HOOKS.build(hook_cfg))
    return hooks
