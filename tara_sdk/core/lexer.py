import re

# 1. ADD THE TOKEN CLASS DEFINITION
class Token:
    def __init__(self, type, value=None):
        self.type = type
        self.value = value

    def __repr__(self):
        return f"Token({self.type}, {self.value})"

# 2. UPDATED LEXER
class Lexer:
    def __init__(self):
        # T.A.R.A. Vocabulary: Mapping human intent to Quantum Logic
        self.patterns = [
            ('CREATE', r'\bspawn\b.*?(\d+)'),
            ('SPIN', r'\bspin\b.*?(\d+)'),         
            ('LINK', r'\blink\b.*?(\d+).*?(\d+)'), 
            ('OBSERVE', r'\bobserve\b'),           
            ('X', r'\bx\b.*?(\d+)'),
            ('Z', r'\bz\b.*?(\d+)'),
            ('ENTANGLE', r'\bentangle\b.*?(\d+).*?(\d+)')
        ]

    def tokenize(self, text):
        tokens = []
        for line in text.split('\n'):
            line = line.strip().lower()
            if not line: continue
            matched = False
            for tag, pattern in self.patterns:
                match = re.search(pattern, line)
                if match:
                    if tag == 'CREATE': 
                        tokens.append(Token('CREATE', int(match.group(1))))
                    elif tag in ['SPIN', 'X', 'Z']: 
                        tokens.append(Token(tag, {'target': int(match.group(1))}))
                    elif tag in ['LINK', 'ENTANGLE']: 
                        tokens.append(Token('LINK', {'ctrl': int(match.group(1)), 'target': int(match.group(2))}))
                    elif tag == 'OBSERVE': 
                        tokens.append(Token('OBSERVE'))
                    matched = True
                    break
            if not matched: 
                # Professional Error Handling
                raise ValueError(f"T.A.R.A. Logic Error: Command not recognized: '{line}'")
        return tokens