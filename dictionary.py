LONGEST_KEY = 1
from typing import Dict, Optional, List, Sequence, cast
import re
import regex

regs = [
        (r'[Bp]+', 'b'),
        (r'[Ln]+', 'l'),
        (r'[Dt]+', 'd'),
        (r'[Gk]+', 'g'),
        (r'[Hh]+', 'h'),
        (r'[Aa]+', 'a'),
        (r'[Rr]+', 'r'),
        (r'[ɚɝ]+', 'R'),
        (r'uü', 'i'),
        (r'IU', 'N'),
        (r'oE', 'e'),
        (r'ü', 'V'),
        (r'^a$', ' '),
        (r'^a[eE]$', 'a'),
        (r'^R$', 'er'),
        (r'[XRZ]+', ''),
        (r'^bldg', 'z'),
        (r'^ldg', 'r'),
        (r'^bld?', 'f'),
        (r'^ld', 'c'),
        (r'^dg', 's'),
        (r'^gr', 'z'),
        (r'^bh', 'p'),
        (r'^fh', 'm'),
        (r'^lh', 'n'),
        (r'^dh', 't'),
        (r'^gh', 'k'),
        (r'^rh', 'zh'),
    # g,k,h 接 i/ü 時作 ⟨ji/ju, qi/qu, xi/xu⟩
        (r'^[gz]([iV])', r'j\1'),
        (r'^[kc]([iV])', r'q\1'),
        (r'^[hs]([iV])', r'x\1'),
    # 上排三鍵並擊 ⟨ong, uang⟩
        (r'(ua?)Io$', r'\1Ne'),
        (r'aI$', 'ai'),
        (r'I[oe]$', 'ei'),
        (r'uI$', 'uei'),
    # -i 鍵亦可用作韻母 ⟨i⟩
        (r'^gI$', 'ji'),
        (r'^kI$', 'qi'),
        (r'^hI$', 'xi'),
        (r'I$', 'i'),
    # 下排三鍵並擊 ⟨iong⟩
        (r'VUE$', 'VNe'),
    # ü 活用爲介音 ⟨i⟩ 以利於並擊 ⟨iao, iou⟩
        (r'V(a?)U$', r'i\1U'),
        (r'aU$', 'ao'),
        (r'UE?$', 'ou'),
        (r'([aiuV])Ne$', r'\1ng'),
    # ⟨eng⟩ 省略 ⟨e⟩
        (r'Ne$', 'eng'),
        (r'^ung$', 'weng'),
        (r'ung$', 'ong'),
        (r'Vng$', 'iong'),
        (r'([aiuV])N$', r'\1n'),
    # ⟨en⟩ 省略 ⟨e⟩
        (r'N$', 'en'),
        (r'^un$', 'wen'),
    # 漢語拼音方案的拼寫規則
        (r'^i(ng?)$', r'yi\1'),
        (r'^i$', 'yi'),
        (r'^i', 'y'),
        (r'^u$', 'wu'),
        (r'^u', 'w'),
        (r'^V', 'yu'),
        (r'^([jqx])V', r'\1u'),
    # 一些容錯
        (r'^([zcsr]h?)i([aoe])', r'\1\2'),
        (r'^([zcsr]h?)i(ng?)$', r'\1e\2'),
    # 拼寫規則
        (r'iou$', 'iu'),
        (r'uei$', 'ui'),
        (r'V', 'v'),
        (r'E', 'e'),
        (r'^([bpf])$', r'\1u'),
        (r'^([mdtnlgkh])$', r'\1e'),
        (r'^([zcsr]h?)$', r'\1i'),
        (r"^([bpm])([iu]|a|i?e|o|[ae]i|i?ao|[oi]u|i?an|[ie]n|[ei]ng|ang|ong)$", r"\1\2'"),
        (r"^([fw])(u|a|o|[ae]i|ao|ou|an|en|eng|ang|ong)$", r"\1\2'"),
        (r"^([dt])([iu]|i?a|i?e|uo|[aeu]i|i?ao|[oi]u|[iu]?an|[ue]n|[ei]ng|ang|ong)$", r"\1\2'"),
        (r"^([nl])([iuv]|i?a|[iv]?e|u?o|[aeu]i|i?ao|[oi]u|[iu]?an|[iue]n|[ei]ng|i?ang|ong)$", r"\1\2'"),
        (r"^([gkh])(u|u?a|e|uo|u?ai|[ue]i|ao|ou|u?an|[ue]n|eng|u?ang|ong)$", r"\1\2'"),
        (r"^([zcs]h?|r)([iu]|u?a|e|uo|u?ai|[ue]i|ao|ou|u?an|[ue]n|eng|u?ang|ong)$", r"\1\2'"),
        (r"^([jqxy])([iu]|i?a|[iu]?e|o|i?ao|[oi]u|[iu]?an|[iu]n|ing|i?ang|i?ong)$", r"\1\2'"),
        (r"^([aeo]|[ae]i|ao|ou|[ae]ng?|er)$", r"\1'"),
        (r"^([A-Za-z]+)$", "")
  ]

def pm2py(s):
  for pat, fmt in regs:
    s = regex.sub(pat, fmt, s)
  return s

# Lookup function: return the translation for <key> (a tuple of strokes)
# or raise KeyError if no translation is available/possible.
def lookup(key: List[str])->str:
  print("TEST: ", key)
  assert len(key) <= LONGEST_KEY
  form = pm2py(key[0])
  print('test: ', form)
  return form

# Optional: return an array of stroke tuples that would translate back
# to <text> (an empty array if not possible).
def reverse_lookup(text):
  return []
