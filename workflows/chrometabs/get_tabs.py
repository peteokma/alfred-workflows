#author: Peter Okma

from alfred_utils.feedback import Feedback
import subprocess
import json
import sys

query = " ".join(sys.argv[1:]).lower()

script = '''
tell application "Google Chrome"
    set tabList to {}
    set json to {"["}
    set windowIndex to 0
    repeat with theWindow in every window
        set windowIndex to windowIndex + 1
        set tabIndex to 0
        repeat with theTab in every tab of theWindow
            set tabIndex to tabIndex + 1
            set end of json to "{"
            set end of json to {quote, "win", quote, ":", windowIndex, ","}
            set end of json to {quote, "tab", quote, ":", tabIndex, ","}
            set end of json to {quote, "url", quote, ":", quote, URL of theTab, quote, ","}
            set end of json to {quote, "title", quote, ":", quote, title of theTab, quote, "}" }
            set end of json to ","
        end repeat
    end repeat
    set json to items 1 thru -2 of json
    set end of json to "]"
    return json as text
    end tell'''

pipe = subprocess.PIPE
p = subprocess.Popen(['osascript', '-s', 's', '-'],
                     stdin=pipe, stdout=pipe, stderr=pipe)
stdout, stderr = p.communicate(script)
stdout = stdout.decode('string_escape')
tabs = json.loads(stdout[1:-2])

fb = Feedback()
for tab in tabs:
    if query in tab['title'].lower() or query in tab['url'].lower():
        fb.add_item(tab['title'],
                    subtitle=tab['url'],
                    arg="%s,%s" % (tab['win'], tab['tab']))
print fb
