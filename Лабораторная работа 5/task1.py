from pprint import pprint
pprint([{'bin': bin(a), 'dec': a, 'hex': hex(a), 'oct': oct(a)} for a in range(16)])