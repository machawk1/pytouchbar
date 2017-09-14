#!/usr/bin/env python
# -*- coding: utf-8 -*-

import objc
import sys
import emoji
import webcolors
from AppKit import \
        NSObject, NSTouchBar, NSButton, NSCustomTouchBarItem, \
        NSColor, NSApplication, NSApp
from PyObjCTools import AppHelper

NSApplicationDelegate = objc.protocolNamed('NSApplicationDelegate')
NSTouchBarProvider = objc.protocolNamed('NSTouchBarProvider')

def sanitizeButtonString(str):
    return str

def makeButton(text, color, parent):
    if text == 'radon':
        text = u"\U00002622 RADON!"
    button =  NSButton.buttonWithTitle_target_action_(
        sanitizeButtonString(text), parent, "buttonClicked:")
    button.setBezelColor_(makeColor(color))
    # button.setLabelColor_(makeColor('white'))
    return button

def makeColor(colorName):
    rgb = webcolors.name_to_rgb(colorName)
    color = NSColor.colorWithRed_green_blue_alpha_(rgb[0], rgb[1], rgb[2], 1.0)
    return color

class AppDelegate (NSObject, NSTouchBarProvider, NSApplicationDelegate):
    def buttonClicked_(self, view):
        print(view.title())

    def touchBar_makeItemForIdentifier_(self, touchbar, buttonStr):
        item = NSCustomTouchBarItem.alloc().initWithIdentifier_(buttonStr)
        button = makeButton(buttonStr, 'red', self)

        item.setCustomizationLabel_(buttonStr)
        item.setView_(button)
        return item

    def touchBar(self):
        touchbar = NSTouchBar.alloc().init()
        touchbar.setDelegate_(self)

        touchbar.setCustomizationIdentifier_('com.matkelly.pytouchbar')
        touchbar.setDefaultItemIdentifiers_(['radon', 'dukes'])
        touchbar.setCustomizationAllowedItemIdentifiers_(['radon', 'com.matkelly.pytouchbar'])

        return touchbar

def main():
    app = NSApplication.sharedApplication()
    app.setAutomaticCustomizeTouchBarMenuItemEnabled_(True)
    delegate = AppDelegate.alloc().init()
    NSApp().setDelegate_(delegate)
    AppHelper.runEventLoop()

if __name__ == '__main__':
    main()
