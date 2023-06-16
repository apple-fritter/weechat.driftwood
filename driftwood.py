import weechat
import os
import re
from datetime import datetime

# Root log directory
LOG_DIR = os.path.expanduser("~/logs/weechat-driftwood/")

def sanitize_filename(filename):
    sanitized = re.sub(r'[^a-zA-Z0-9]', ' ', filename)
    sanitized = re.sub(r' (?=[a-zA-Z0-9])', '_', sanitized)
    sanitized = sanitized.rstrip('_')
    return sanitized

def driftwood_logger(data, buffer, date, tags, displayed, highlight, prefix, message):
    # Skip logging server buffers
    if weechat.buffer_get_string(buffer, "localvar_type") == "server":
        return weechat.WEECHAT_RC_OK

    # Skip logging join/part/quit messages
    if "irc_join" in tags or "irc_part" in tags or "irc_quit" in tags:
        return weechat.WEECHAT_RC_OK

    # Extract channel or nick from the buffer name
    channel = weechat.buffer_get_string(buffer, "short_name")
    if not channel:
        return weechat.WEECHAT_RC_OK

    # Get the nick of the sender
    nick = weechat.buffer_get_string(buffer, "localvar_nick")
    if not nick:
        return weechat.WEECHAT_RC_OK

    # Build log file path
    timestamp = datetime.fromtimestamp(int(date)).strftime("%Y%m%d")
    sanitized_channel = sanitize_filename(channel)
    sanitized_nick = sanitize_filename(nick)
    log_dir = os.path.join(LOG_DIR, sanitized_nick, sanitized_channel, timestamp)
    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(log_dir, "log.txt")

    # Format log entry
    entry = f"{prefix}\t{message}\n"

    # Append log entry to file
    with open(log_file, "a", encoding="utf-8") as file:
        file.write(entry)

    return weechat.WEECHAT_RC_OK

if __name__ == "__main__":
    weechat.register("driftwood_logger", "@apple-fritter", "1.0", "MIT",
                     "Log WeeChat buffers natively in Driftwood format", "", "")

    weechat.hook_print("", "", "", 1, "driftwood_logger", "")
