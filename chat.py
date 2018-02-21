#!/usr/bin/env python3

import cgi
import cgitb
import os.path
import html

cgitb.enable()
FILE_LOG = "chat-log.txt"

def print_html(body):
    print("Content-Type: text/html: charset=utf-8")
    print("")
    print("""
    
    """.format(body))

def mode_read(form):
    log = ""
    if os.path.exists(FILE_LOG):
        with open() as f:
            log = f.read()
    print_html(log)

def main():
    form = cgi.FieldStorage()
    mode = form.getvalue("mode", "read")
    if mode == "read": mode_read(form)
    elif mode == "write": mode_read(form)
    else: mode_read(form)

if __name__ == "__main__":
    main()


