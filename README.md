# OpenAI Chat Completion in Keyboard using Pythonista

https://user-images.githubusercontent.com/12567059/223289833-7b7cb51e-2da0-46e3-8d5d-56cf668f262d.MP4

## Prerequisites

0. Get [Pythonista](https://apps.apple.com/us/app/pythonista-3/id1085978097) on your iOS device

   > Pythonista is a complete scripting environment for Python, running directly on your iPad or iPhone. It includes support for both Python 3.6 and 2.7, so you can use all the language improvements in Python 3, while still having 2.7 available for backwards compatibility.
   >
   > In true Python fashion, batteries are included – from popular third-party modules like requests, numpy, matplotlib, and many more, to modules that are tailor-made for iOS. You can write scripts that access sensor and location data, your photo library, contacts, reminders, the clipboard, and much more.
   >
   > You can also use Pythonista to build interactive multi-touch experiences, custom user interfaces, animations, and 2D games.
   >
   > Apart from learning and practicing Python, you can also use Pythonista to automate parts of iOS with app extensions, e.g. to invoke scripts directly from the standard share sheet in almost any app.

1. Install [StaSh](https://github.com/ywangd/stash)
2. Install `sseclient-py` by launching StaSh shell using `launch_stash.py` and then execute `pip install sseclient-py`
3. Put the corresponding files into Pythonista documents
4. Replace `OPENAI_TOKEN` in `chat_cmpl.py` with your OpenAI token
5. Add `chat_cmpl.py` to your Keyboards in Pythonista by going to `Settings` -> `Pythonista Keyboard` -> `Add` -> Choose `chat_cmpl.py` as the script
6. Go to iOS Settings -> General -> Keyboard -> Keyboards -> Add New Keyboard -> Pythonista Keyboard and enable Full Access
7. Now you can use the keyboard to chat with OpenAI anywhere in iOS!
