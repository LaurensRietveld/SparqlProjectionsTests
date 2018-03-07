from SPARQLWrapper import SPARQLWrapper, JSON
from pythonql.parser.Preprocessor import makeProgramFromString
import json


def loadText(filename):
    with open(filename, 'r') as fin:
        lines = fin.readlines()
        text = ''.join(lines)
        return text

endpoint = loadText('test/resources/test1.endpoint').strip()
query = loadText('test/resources/test1.query')
expected = loadText('test/resources/test1.expected')
projectionScript = loadText('test/resources/test1.pyql')


sparql = SPARQLWrapper(endpoint=endpoint)
sparql.setMethod('GET')
sparql.setReturnFormat(JSON)
sparql.setQuery(query)

results = sparql.query().convert()

programResult = []
program = makeProgramFromString(projectionScript)
exec(program)

print '===================================================================='
print '=== THIS IS WHAT WE GOT: ==========================================='
print '===================================================================='
print json.dumps(programResult, indent=2)

print '===================================================================='
print '=== THIS IS WHAT WE EXPECTED: ======================================'
print '===================================================================='
print expected
