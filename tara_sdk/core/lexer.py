import re
from ..utils.logger import setup_logger

log = setup_logger("LEXER")

class Token:
    def __init__(self, type_, value=None, line=0):
        self.type = type_
        self.value = value
        self.line = line

class Lexer:
    def __init__(self):
        # The Grammar Rules
        self.rules = [
            ('CREATE',  r'(?i)(create|init)\s+(\d+)\s+(qubits?)'),
            ('H',       r'(?i)(h|superpose)\s+(qubit\s+)?(\d+)'),
            ('CX',      r'(?i)(cx|link)\s+(\d+)\s+(to|with)\s+(\d+)'),
            ('MEASURE', r'(?i)(measure)\s+(all)'),
        ]

    def tokenize(self, code):
        tokens = []
        lines = code.split('\n')
        log.info(f"Scanning {len(lines)} lines of code...")
        
        for i, line in enumerate(lines):
            line = line.strip()
            if not line or line.startswith('#'): continue
            
            matched = False
            for type_, pattern in self.rules:
                match = re.search(pattern, line)
                if match:
                    if type_ == 'CREATE':
                        tokens.append(Token('CREATE', int(match.group(2)), i+1))
                    elif type_ == 'H':
                        tokens.append(Token('H', {'target': int(match.group(3))}, i+1))
                    elif type_ == 'CX':
                        tokens.append(Token('CX', {'ctrl': int(match.group(2)), 'target': int(match.group(4))}, i+1))
                    elif type_ == 'MEASURE':
                        tokens.append(Token('MEASURE', None, i+1))
                    matched = True
                    break
            
            if not matched:
                log.warning(f"Line {i+1} ignored: '{line}'")
        
        return tokens