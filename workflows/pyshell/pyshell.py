#author: Peter Okma

from alfred_utils.feedback import Feedback
import sys
import re

# import addition packages you want to access here

query = " ".join(sys.argv[1:])
fb = Feedback()
try:
    res = str(eval(query))
    fb.add_item(res, arg=res)
except SyntaxError as e:
    if ('EOF', 'EOL' in e.msg):
        fb.add_item('...')
    else:
        fb.add_item('SyntaxError', e.msg)
except Exception as e:
        fb.add_item(e.__class__.__name__,
            subtitle=e.message)
print fb
