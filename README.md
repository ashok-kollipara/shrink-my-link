# Shrink my link

An attempt at command line personal url shortening tool from multiple services concurrently at once via API with custom shorten back-half alias provision.

## INSTALLATION

Using Makefile for installation. 

You can edit the install destination path (defaults to ~/.local/bin) and filename in Makefile

```
make install clean

```

## USAGE

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

### Will be working with the below providers

- cuttly
- tinyurl
- bitly (WIP in async mode, 50 links/month on free plan)
