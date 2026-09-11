'''Blackwell-safe vLLM boot: skip FlashInfer JIT that needs CUDA >= 12.9.'''

from __future__ import annotations

import inspect
import os

os.environ.setdefault('VLLM_USE_FLASHINFER_SAMPLER', '0')
os.environ.setdefault('VLLM_ATTENTION_BACKEND', 'FLASH_ATTN')


def _engine_params() -> set[str]:
    from vllm.engine.arg_utils import EngineArgs
    return set(inspect.signature(EngineArgs.__init__).parameters)


def llm_kwargs(base: dict) -> dict:
    params = _engine_params()
    extras = {
        'moe_backend': 'triton',
        'linear_backend': 'cutlass',
        'attention_backend': 'FLASH_ATTN',
    }
    for key, value in extras.items():
        if key in params and key not in base:
            base[key] = value
    return base


def make_llm(**kwargs):
    from vllm import LLM
    return LLM(**llm_kwargs(dict(kwargs)))


def probe() -> None:
    import vllm
    params = sorted(_engine_params())
    interesting = [
        name for name in params
        if any(token in name.lower() for token in (
            'moe', 'flash', 'backend', 'eager', 'linear', 'attn',
        ))
    ]
    print(f'vllm {vllm.__version__}', flush=True)
    print('engine extras:', interesting, flush=True)
    print('llm_kwargs sample:', llm_kwargs({'model': 'dummy'}), flush=True)


if __name__ == '__main__':
    probe()
