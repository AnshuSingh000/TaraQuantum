import re

class Token:
    def __init__(self, type, value=None):
        self.type = type
        self.value = value

class Lexer:
    def __init__(self):
        # Using word boundaries (\b) and search allows "add put H on 0" to work
        self.patterns = [
            ('H', r'\bh\b.*(\d+)'),
            ('X', r'\bx\b.*(\d+)'),
            ('Z', r'\bz\b.*(\d+)'),
            ('S', r'\bs\b.*(\d+)'),
            ('T', r'\bt\b.*(\d+)'),
            ('CX', r'\bcx\b.*?(\d+).*?(\d+)'),
            ('MEASURE', r'\bmeasure\b'),
            ('CREATE', r'\b(?:create|add|make)\b.*?(\d+)')
        ]

    def tokenize(self, text):
        tokens = []
        lines = text.split('\n')
        
        for line in lines:
            line = line.strip()
            if not line: continue
                
            matched = False
            for tag, pattern in self.patterns:
                # search looks for the gate anywhere in your "add put..." sentence
                match = re.search(pattern, line, re.IGNORECASE)
                if match:
                    if tag == 'H':
                        tokens.append(Token(tag, {'target': int(match.group(1))}))
                    elif tag == 'CX':
                        tokens.append(Token(tag, {'ctrl': int(match.group(1)), 'target': int(match.group(2))}))
                    elif tag == 'CREATE':
                        tokens.append(Token(tag, int(match.group(1))))
                    elif tag in ['X', 'Z', 'S', 'T']:
                        tokens.append(Token(tag, {'target': int(match.group(1))}))
                    elif tag == 'MEASURE':
                        tokens.append(Token(tag))
                    
                    matched = True
                    break
            
            if not matched:
                raise ValueError(f"T.A.R.A. doesn't understand this command: {line}")
                
        return tokens