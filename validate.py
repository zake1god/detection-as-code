import sys
from sigma.parser import SigmaCollectionParser
from sigma.backends.splunk import SplunkBackend

def validate_rule(filepath):
    with open(filepath, 'r') as f:
        parser = SigmaCollectionParser(f, 'yaml')
        collection = parser.parse()
        backend = SplunkBackend()
        backend.convert(collection)

if __name__ == "__main__":
    validate_rule(sys.argv[1])
