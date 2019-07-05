# -*- coding: utf-8 -*-

"""Top-level package for Beep."""

__author__ = """Ben Lindsay"""
__email__ = 'benjlindsay@gmail.com'
__version__ = '0.1.0'

from pathlib import Path
import sys

class mod_call(object):
    def __call__(self):
        from IPython.display import Audio
        wav = str(Path(__file__).parent / "beep-01a.wav")
        return Audio(wav, autoplay=True)

sys.modules[__name__] = mod_call()
