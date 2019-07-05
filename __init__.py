#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# __init__.py
# 
# Copyright (c) 2019 Ben Lindsay <benjlindsay@gmail.com>

from pathlib import Path
import sys

class mod_call(object):
    def __call__(self):
        from IPython.display import Audio
        wav = str(Path(__file__).parent / "beep-01a.wav")
        return Audio(wav, autoplay=True)
sys.modules[__name__] = mod_call()
