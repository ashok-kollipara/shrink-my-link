# shrink my link

An attempt at python command line personal url shortening tool from multiple services concurrently at once via API with custom shorten back-half / alias provision.

## Demo  

![shrink my link](/.assets/shrink_demo_final.gif "shrink my link") 

## Index

- [Dependencies](#dependencies)
- [Installation](#installation)
- [Configuration](#configuration)
- [Examples](#examples)
- [Providers](#compatible-providers)

## Dependencies

- [`Python 3.10`](https://www.python.org/about/gettingstarted/)
- [`aiohttp`](https://docs.aiohttp.org/en/stable/)
- [`pip`](https://pypi.org/project/pip/)
    
    - Install all the required packages :
    ```
    pip install -r requirements.txt
    ```
    
- make (optional)


## Installation

- **Using Makefile for installation :**
You can edit the install destination path `(defaults to ~/.local/bin)` and filename `shrink` in Makefile
```
make install clean
```

- **Manually :**
Run the following commands in terminal
```
cp shrink.py shrink
chmod +x shrink
cp shrink ~/.local/bin/
```

**Note :** 

It is assumed that `~/.local/bin` is already added to $PATH. If not add it to PATH and update via .bashrc or .zshrc

**WINDOWS :** 

- Read this on how to : [Add file / folder to PATH](https://answers.microsoft.com/en-us/windows/forum/all/enviromnent-variables-adding-to-system-path/902feff1-cac2-49e3-9021-7fa4bedf4347)

- Please add an alias `shrink` to `python \path\to\folder\shrink.py` for console to use the tool.

 - [Add alias in Windows Command Prompt](https://stackoverflow.com/questions/20530996/aliases-in-windows-command-prompt)
 - [Windows console aliases](https://docs.microsoft.com/en-us/windows/console/console-aliases)


## Configuration

#### UNIX / LINUX


1. Copy the `templates/api_keys_template` file to your desired folder and Read and Fill it with necessary details

2. Rename the file after placing in your desired folder
```
mv templates/api_keys_template ~/.config/api_keys
```
3. Source the file to your shell environment variables via .bashrc or .zshrc
```
echo "source ~/.config/api_keys" >> ~/.bashrc
```
4. Test by opening new termial window or refreshing shell and do:
```
echo "$TINYURL_ROUTE"
```
5. **DO NOT** add `api_keys` file to any git repo or online public backup

#### WINDOWS
For Windows please refer to guides on environmental variables setup
- [Guide: Pheonixnap](https://phoenixnap.com/kb/windows-set-environment-variable)
- [Guide: Microsoft Powershell](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_environment_variables?view=powershell-7.2)

**NOTE :** 

Please add the variables for persistent setup and also check your IDE environment variables if you use an IDE to fork and develop further as this can pose some problems with environment variables



## Usage

#### Unix / Linux
```
usage: shrink [-h] [-v] [-a ALIAS] [-q] URL

To shorten the given Long URL

positional arguments:
  URL                   the long url to shorten

options:
  -h, --help            show this help message and exit
  -v, --verbose         add verbosity to output
  -a ALIAS, --alias ALIAS
                        try for custom back-half e.g bit.ly/{ALIAS}
  -q, --quick           quickly get single link, useful to chain commands in Linux

```  

**ALTERNATIVELY,**  there is a choice to use the application standalone with any of the providers from the `src/` folder
## Examples

- **Simple copy avaiable with middle-click mouse**
```
shrink -q https://example.com | xclip -r 
```  
- **Copy with Notification :**
```
shrink -q https://example.com | xclip -r && notify-send "Short URL" "Ready to paste"
```

- **Pick and Paste : Like a Boss**  
  
  With [fzf](https://github.com/junegunn/fzf) :
```
shrink https://example.com/ -a test | fzf | xclip -r && notify-send "Short URL" "Ready to paste"
```  
  Or with [dmenu](https://tools.suckless.org/dmenu/) :
```
shrink https://example.com/ -a test | dmenu | xclip -r && notify-send "Short URL" "Ready to paste" 
```

## Compatible providers

Based on the free tier options with API provided for personal use from these URL shortening service providers. (as of 17-Aug-2022)

**Thank You :**

- [cutt.ly](https://cutt.ly)
- [tinyurl.com](https://tinyurl.com)
- [bitly.com](https://bitly.com)


