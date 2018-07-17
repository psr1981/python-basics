class CManager(object):
    def __init__(self):
        print ('__init__')
    
    def __enter__(self):
        print ('__enter__')
        return self
    
    def __exit__(self, type, value, traceback):
        print ('__exit__:', type, value)
        return True  # Suppress this exception

    def __del__(self):
        print ('__del__', self)

with CManager() as c:
    print ('doing something with c:', c)
    raise RuntimeError()
    print ('finished doing something')
    print ('done something')


