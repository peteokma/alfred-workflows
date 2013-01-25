#author: Peter Okma

from alfred_utils.feedback import Feedback
import urllib
import json
import sys

query = sys.argv[1]
url = 'http://en.wikipedia.org/w/api.php?action=opensearch&search=%s' % query
response = json.load(urllib.urlopen(url))

fb = Feedback()
for title in response[1]:
    url = 'en.wikipedia.org/wiki/%s' % title
    url.replace(' ', '_')
    fb.add_item(title,
        subtitle="Read wikipedia article on %s" % title,
        arg=title.replace(" ", "_"))
print fb
