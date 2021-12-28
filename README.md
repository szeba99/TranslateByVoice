# TranslateByVoice

Step one - Press the hotkey
Step two - Read the foreign text you don't understand
Step three - Wait a bit
Step four - Listen to the translation

# Configuring

A file called "settings.json" is included. There you can customize to and from which language you want to translate. You can also set the online TTS service.
Default is "microsoft" because I like its Hungarian voice, however you can set it to "google" or to whatever the balabolka cli lets.
duration is the duration to wait while recording your voice. As soon as you press the hotkey, recording starts.

You can also set a custom hotkey, the python keyboard library is used for this.

# Making it work

I had to use different version of PyAudio and maybe something else, because something didn't work, I forgot which, but the correct versions are used in the build,
which is located in the "dist" directory.

