#!/usr/bin/env python
# coding: utf-8
import base64
import hashlib
import random


def trip(key: str = "aiueoaiueo700", seed: int = 100) -> str:
    random.seed(seed)
    key = "".join(random.sample(key, len(key)))
    key = key.encode('cp932')
    code = hashlib.sha1(key).digest()
    code = base64.b64encode(code, b'./')
    code = code[:12]
    return code.decode('cp932')


print(trip())
