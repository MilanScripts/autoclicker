# Auto Clicker

![Auto Clicker Preview](https://media.discordapp.net/attachments/1223356103610470564/1280633481751166986/MacBook_Pro_13-Inch-SCREENss.png?ex=66d8ca5f&is=66d778df&hm=16367897e456236290d441a72ed22a626f7eabe1c303c7b0ce30dde58fd3e597&=&format=webp&quality=lossless&width=413&height=350)

## Overview

The Auto Clicker is a simple, lightweight tool designed to automate mouse clicks at user-defined intervals. Built using Flask, Python, and pyautogui, it provides a web-based interface for controlling the auto-clicking functionality.

### Features

- **Web Interface**: Easily control the auto-clicker using a web browser.
- **Custom Intervals**: Set intervals for clicks in milliseconds, seconds, minutes, and hours.
- **Hotkey Support**: Start and stop auto-clicking using a configurable hotkey.
- **Configurable Theme**: Customize the appearance of the interface (theme support coming soon).

## How It Works

1. **Configuration**: The tool uses a configuration file (`config.cfg`) to store settings such as click intervals and hotkey preferences. 
2. **Auto-Clicking**: When enabled, the auto-clicker continuously sends clicks at the specified interval using the `pyautogui` library.
3. **Control Interface**: You can start or stop the auto-clicker and adjust settings via the web interface hosted by Flask.
4. **Hotkey Integration**: Use a configurable hotkey to toggle the clicking functionality on or off without accessing the web interface.

## Usage

1. **Access the Web Interface**: Open your web browser and navigate to `http://127.0.0.1:5000`.
2. **Configure Settings**: Use the interface to set the desired click interval (milliseconds, seconds, minutes, hours).
3. **Start/Stop Clicking**: Use the buttons on the web interface or the configured hotkey to control the auto-clicker.

## License
MIT License

Copyright (c) 2024 MilanScripts

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
