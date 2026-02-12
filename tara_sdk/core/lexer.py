import re

class Token:
    def __init__(self, type, value=None):
        self.type = type
        self.value = value

class Lexer:
    def __init__(self):
        # Expanded vocabulary using non-capturing groups (?: ... )
        # This allows multiple words to trigger the same logic tag.
        self.patterns = [
            ('CREATE', r'(?:create|add|initialize|make|spawn) (\d+) qubits?'),
            ('H', r'(?:h|hadamard|superpose|spin) qubit (\d+)'),
            ('X', r'(?:x|not|flip|invert) qubit (\d+)'),
            ('Z', r'(?:z|phase) qubit (\d+)'),
            ('CX', r'(?:cx|cnot|link|connect) (\d+) with (\d+)'),
            ('MEASURE', r'(?:measure|observe|collapse|check) all'),
            ('ENTANGLE', r'(?:entangle|pair|spook) (\d+) and (\d+)') 
        ]

    def tokenize(self, text):
        tokens = []
        lines = text.lower().split('\n')
        
        for line in lines:
            line = line.strip()
            if not line:
                continue
                
            matched = False
            for tag, pattern in self.patterns:
                match = re.match(pattern, line)
                if match:
                    # Note: groups(1) and groups(2) refer to the (\d+) parts
                    if tag == 'CREATE':
                        tokens.append(Token(tag, int(match.group(1))))
                    elif tag in ['H', 'X', 'Z']:
                        tokens.append(Token(tag, {'target': int(match.group(1))}))
                    elif tag == 'CX':
                        tokens.append(Token(tag, {'ctrl': int(match.group(1)), 'target': int(match.group(2))}))
                    elif tag == 'ENTANGLE':
                        tokens.append(Token(tag, {'q1': int(match.group(1)), 'q2': int(match.group(2))}))
                    elif tag == 'MEASURE':
                        tokens.append(Token(tag))
                    
                    matched = True
                    break
            
            if not matched:
                raise ValueError(f"T.A.R.A. doesn't understand this command: {line}")
                
        return tokens