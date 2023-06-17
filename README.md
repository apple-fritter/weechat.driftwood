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

1. Private messages: Messages exchanged between users in private conversations.
2. Channel messages: Messages sent within IRC channels.
3. Notices: Various types of notices, such as server notices or user-specific notices.
4. CTCP events: Client-to-Client Protocol events, which include actions, requests, and responses.

## Usage
1. Clone this repository to your local machine or download the ZIP file.
2. Copy the driftwood.py file to the WeeChat plugins directory. (Default location: `~/.weechat/python/autoload/`)
3. Launch WeeChat and load the plugin by running the following command:
```shell
/python load autoload/driftwood.py
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

## <a id="irc-meta"></a>🤪 IRC Meta
### <a id="fritterz"></a> [@apple-fritter](https://github.com/apple-fritter)'s IRC Repositories:

---

#### Driftwood Suite of IRC Analytics
###### Driftwood utilities
- [driftwood](https://github.com/apple-fritter/driftwood): A unified IRC log format definition. (Rust)
- [flotsam](https://github.com/apple-fritter/flotsam): Aggregate a per-user metric of flagged contributions to any given user. (Rust)
- [jetsam](https://github.com/apple-fritter/jetsam): Flag lines of driftwood formatted IRC logs for sanitization, moderation, or further review. (Rust)
- [scrimshaw](https://github.com/apple-fritter/scrimshaw): Create a quoteslist of any given user, from your driftwood formatted logs. (Rust)

##### Driftwood native logging plugins
- [weechat.driftwood](https://github.com/apple-fritter/weechat.driftwood): Natively log WeeChat messages in the driftwood standard. (Python)

---

#### heX-Chat
- [xchat.channel-moderation](https://github.com/apple-fritter/xchat.channel-moderation): Moderate an IRC channel. (Python)
- [doppelganger](https://github.com/apple-fritter/doppelganger): X-Chat mIRC imposter. Fingerprint subversion. (Python bundle)

---

#### IRCcloud
- [irccloud-to-weechat](https://github.com/apple-fritter/irccloud-to-weechat): Convert IRC logs from IRCcloud format to Weechat format. (Rust)
- [irccloud-to-xchat](https://github.com/apple-fritter/irccloud-to-xchat): Convert IRC logs from IRCcloud format to XChat format. (Rust)

---

#### WeeChat
- [weechat.driftwood](https://github.com/apple-fritter/weechat.driftwood): Natively log WeeChat messages in the driftwood standard. (Python)
- [weechat.ban-evasion-detection](https://github.com/apple-fritter/weechat.ban-evasion-detection): Detect and prevent ban evasion. (Python)
- [weechat.typo-aggregator](https://github.com/apple-fritter/weechat.typo-aggregator): Record misspelled words in a TSV (tab-separated values) file. (Python)
- [weechat.whois-aggregator](https://github.com/apple-fritter/weechat.whois-aggregator): Aggregate whois data in a rolling CSV file. (Python)
- [weechat.youtube-info](https://github.com/apple-fritter/weechat.youtube-info): Deprecated. Extract video information from a YouTube URL and post it back to the channel. (Python)
- [weechat.youtube-api](https://github.com/apple-fritter/weechat.youtube-api): Extract video information from a YouTube URL and post it back to the channel. (Python)

---

### IRC usage considerations
When working with any project involving IRC (Internet Relay Chat), it's important to keep the following considerations in mind to ensure a positive and respectful environment for all participants.

#### Philosophy of Use
Tailor your project's behavior and responses to align with the expected norms and conventions of IRC. Take into account the preferences and expectations of IRC users, ensuring that your project provides a seamless and familiar experience within the IRC ecosystem.

#### Foster a Positive and Inclusive Environment
Respect and adhere to the guidelines and policies of the IRC platform you are using. Familiarize yourself with the platform's rules regarding script usage, automation, and acceptable behavior. Comply with the platform's Terms of Service, and be mindful of any limitations or restrictions imposed by the platform. Strive to create an inclusive and welcoming environment where all users can engage respectfully and comfortably.

#### Respect the Rights and Dignity of Other Users
Maintain a polite and courteous demeanor in all interactions. Uphold the fundamental principles of respect, avoiding engagement in illegal, inappropriate, or offensive behavior. This includes refraining from using derogatory or inflammatory language, sharing explicit, triggering, or offensive content, engaging in harassment, or launching personal attacks. Obtain explicit consent before interacting with other users or sending automated responses. Respect the privacy of other users and avoid invading their personal space without their permission.

#### Respect the IRC Community and Channels
Avoid disrupting the normal flow of conversation within IRC channels. Ensure that your project's actions and responses do not cause unnecessary disruptions or inconvenience to other users. Implement mechanisms to prevent spamming or flooding the channel with excessive or irrelevant messages. Handle errors gracefully, preventing unintended behavior or disruptions to the IRC platform or the experiences of other users.

#### Ensure Compatibility
Consider the potential variations in behavior across different IRC platforms and clients. While aiming for compatibility, be aware that certain functionalities may not be available or consistent across all platforms. Test your project on multiple IRC platforms and clients to ensure compatibility and provide the best possible experience for users.

---

## Contributing
Contributions are welcome! If you'd like to contribute, please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your changes to your forked repository.
5. Submit a pull request to the main repository.

---

## [Disclaimer](DISCLAIMER)
**This software is provided "as is" and without warranty of any kind**, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose and noninfringement. In no event shall the authors or copyright holders be liable for any claim, damages or other liability, whether in an action of contract, tort or otherwise, arising from, out of or in connection with the software or the use or other dealings in the software.

**The authors do not endorse or support any harmful or malicious activities** that may be carried out with the software. It is the user's responsibility to ensure that their use of the software complies with all applicable laws and regulations.

---

## License
This project is licensed under the [MIT License](LICENSE).
