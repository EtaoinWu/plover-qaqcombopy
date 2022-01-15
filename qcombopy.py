"""
"""

KEYS = (
    # numeric prefix
    '#',
    # left hand initials
    'B-', 'p-', 'L-', 'n-',
    'D-', 't-', 'G-', 'k-',
    'R-', 'r-',
    # initial modifier
    'H-', 'h-',
    # center
    '*', ';',
    # rhotic
    '-ɚ', '-ɝ',

    # final
    # medial
    '-i', '-u', '-ü',
    # nucleus
    '-a', '-A',
    # coda
    '-N', '-I', '-U',
    # nucleus, part 2
    '-e', '-o', '-E',
    '-X', '-Z'
)

IMPLICIT_HYPHEN_KEYS = KEYS

SUFFIX_KEYS = ()

UNDO_STROKE_STENO = '*'

NUMBER_KEY = '#'

NUMBERS = {
    'B-': '1-',
    'L-': '2-',
    'D-': '3-',
    'G-': '4-',
    'R-': '5-',
    'p-': '1-',
    'n-': '2-',
    't-': '3-',
    'k-': '4-',
    'r-': '5-',
    '-ɚ': '-6',
    '-u': '-7',
    '-I': '-8',
    '-o': '-9',
    '-X': '-0',
    '-ɝ': '-6',
    '-ü': '-7',
    '-U': '-8',
    '-E': '-9',
    '-Z': '-0',
}

KEYMAPS = {
    'Keyboard': {
        '#': 'c',
        # left hand initials
        'B-': 'q', 'p-': 'a', 'L-': 'w', 'n-': 's',
        'D-': 'e', 't-': 'd', 'G-': 'r', 'k-': 'f',
        'R-': 't', 'r-': 'g',
        # initial modifier
        'H-': 'v', 'h-': (),
        # center
        '*': 'b',
        ';': 'z',
        # rhotic
        '-ɚ': 'h', '-ɝ': 'n',

        # final
        # medial
        '-i': 'j', '-u': 'u', '-ü': 'm',
        # nucleus
        '-a': 'space', '-A': (),
        # coda
        '-N': 'k', '-I': 'i', '-U': ',',
        # nucleus, part 2
        '-e': 'l', '-o': 'o', '-E': '.',
        '-X': 'p', '-Z': ()
    },
    'Gemini PR': {
        # numeric prefix
        '#': ('#1', '#2', '#3', '#4', '#5', '#6', '#7', '#8', '#9', '#A', '#B', '#C'),
        # left hand initials
        'B-': 'S1-', 'p-': 'S2-', 'L-': 'T-', 'n-': 'K-',
        'D-': 'P-', 't-': 'W-', 'G-': 'H-', 'k-': 'R-',
        'R-': "*1", 'r-': '*2',
        # initial modifier
        'H-': 'A-', 'h-': 'O-',
        # center
        ';': '-D',
        '*': '-Z',
        # rhotic
        '-ɚ': '*3', '-ɝ': '*4',

        # final
        # medial
        '-i': (), '-u': '-F', '-ü': '-R',
        # nucleus
        '-a': '-E', '-A': '-U',
        # coda
        '-N': (), '-I': '-P', '-U': '-B',
        # nucleus, part 2
        '-e': (), '-o': '-L', '-E': '-G',
        '-X': '-T', '-Z': '-S'
    }
}

ORTHOGRAPHY_RULES = {}
ORTHOGRAPHY_RULES_ALIASES = {}
ORTHOGRAPHY_WORDLIST = None

DICTIONARIES_ROOT = '.'
DEFAULT_DICTIONARIES = ('overwrite.json', 'dictionary.py')
