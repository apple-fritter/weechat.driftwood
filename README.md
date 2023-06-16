# WeeChat Driftwood Logger
The WeeChat Driftwood Logger is a plugin for WeeChat, a lightweight and extensible IRC client. This plugin enables native logging of IRC messages in the [Driftwood log format](https://github.com/apple-fritter/driftwood), providing a standardized and organized way to store and manage IRC logs.

## Features
- Logs IRC messages in the Driftwood format.
- Supports logging of private messages and channel messages.
- Ignores server buffers and join/part/quit messages by default.
- Sanitizes channel and nick names for proper filename handling.
- Creates a directory structure based on the Driftwood organizational method.

## Driftwood Log Format
The Driftwood log format is a [standardized format](https://github.com/apple-fritter/driftwood) for IRC logs. It uses a distinctive delimiter character to separate different fields within each log entry. The log format follows these conventions:

#### Columns are separated by the Unicode character (☕).
- The first column is left blank, and is a placeholder for content suppression, using the character `#`.
- Columns 2, 3, and 4 represent the hour, minutes, and seconds.
- Column 5 contains the sender.
- Column 6 contains the message text.
- The seventh column is left blank.

## Sanitization Consideration
To ensure proper filename handling and compatibility with various file systems, **the WeeChat Driftwood Logger sanitizes channel and nick names before creating log files.**

#### The following sanitization rules are applied:

- Non-alphanumeric characters, mid name, are replaced with whitespace.
- Leading and trailing non-alphanumeric characters are removed.

> This sanitization process ensures that the log files are named appropriately and conform to file naming conventions.

## Types of Data Logged
The WeeChat Driftwood Logger logs the following types of data:

1. Private messages
> Messages exchanged between users in private conversations
2. Channel messages
> Messages sent within IRC channels
3. Notices
> Various types of notices, such as server notices or user-specific notices
4. CTCP events
> Client-to-Client Protocol events, which include actions, requests, and responses

## Usage
1. Clone this repository to your local machine or download the ZIP file.
2. Copy the driftwood_logger.py file to the WeeChat plugins directory. (Default location: `~/.weechat/python/autoload/`)
3. Launch WeeChat and load the plugin by running the following command:
```shell
/python load autoload/driftwood_logger.py
```

## Flowchart
```
┌─ Start Program
│
├─ [Initialize WeeChat Driftwood Logger]
│   │
│   ├─ [Load Plugin]
│   ├─ [Set Log Directory]
│   ├─ [Create Directory Structure]
│   └─ [Set Logging Options]
│
├─ [Handle IRC Messages]
│   │
│   ├─ [Process Private Messages]
│   │   │
│   │   ├─ [Filter Non-Message Content]
│   │   └─ [Log Private Messages]
│   │
│   ├─ [Process Channel Messages]
│   │   │
│   │   ├─ [Filter Non-Message Content]
│   │   └─ [Log Channel Messages]
│   │
│   ├─ [Process Notices]
│   │   │
│   │   ├─ [Filter Non-Message Content]
│   │   └─ [Log Notices]
│   │
│   └─ [Process CTCP Events]
│       │
│       ├─ [Filter Non-Message Content]
│       └─ [Log CTCP Events]
│
├─ [Sanitize Filename]
│
└─ End Program
```

---

## [Disclaimer](DISCLAIMER)
**This software is provided "as is" and without warranty of any kind**, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose and noninfringement. In no event shall the authors or copyright holders be liable for any claim, damages or other liability, whether in an action of contract, tort or otherwise, arising from, out of or in connection with the software or the use or other dealings in the software.

**The authors do not endorse or support any harmful or malicious activities** that may be carried out with the software. It is the user's responsibility to ensure that their use of the software complies with all applicable laws and regulations.

---

## License

These files released under the [MIT License](LICENSE).
