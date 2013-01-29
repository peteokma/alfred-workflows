import subprocess
import sys

query = sys.argv[1]
args = query.split(",")

script = '''
    on run {win_id, tab_id}
        set win_id to win_id as number
        set tab_id to tab_id as number
        tell application "Google Chrome"
            activate
            set active tab index of window win_id to tab_id
            set index of window win_id to 1
        end tell
end run'''

pipe = subprocess.PIPE
p = subprocess.Popen(['osascript', '-'] + args,
                     stdin=pipe, stdout=pipe, stderr=pipe)
p.communicate(script)
