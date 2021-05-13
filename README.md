# EasyAssistant
EasyAssistant is a tool that helps you build your own voice assistant. 

## Usage
### Requirements
In order to use EasyAssistant, you will need the speech-recognition library. In order to download the library, you will need to use pip;
```
pip install SpeechRecognition
``` 
And more importantly, you have to have a microphone.
### Opening Programs
To use EasyAssistant to open programs you first need to open apppaths.txt. Thereon, you will see:

```bash
myprogram=C:/path/to/file.exe
myprogram2=C:/path/to/file2.exe
```

If you wish, you can delete or create new paths in this format. To do so, refer to:
```bash
namethatyouwillhavetosay=pathtothatprogram
```
This format could also be used to open any other type of file, from images to batch files.

### Opening Websites
To use EasyAssistant to open websites, you have to open websites.txt. On there, you will see:
```bash
google=google.com
youtube=youtube.com
twitter=twitter.com
wikipedia=wikipedia.org
```
If you wish, you can delete or create new paths in this format. To do so, refer to:
```bash
namethatyouwillhavetosay=websitenameanddomain
```
This format is only used for opening websites, as opening programs do not work the same way as to open websites.
### Using Your Assistant
To use your assistant, all you have to do is launch main.py and then start talking to the microphone. Have fun!
## License
[GNU GPL2](https://choosealicense.com/licenses/gpl-2.0/)
