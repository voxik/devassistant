# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 13:16:47 2013

@author: Petr Hracek
"""

import mainWindow
import finalWindow
from devassistant.logger import logging
from gi.repository import Gtk

class pathWindow(object):
    def __init__(self, parent, mainWin, builder):
        self.parent = parent
        self.mainWin = mainWin
        self.pathWindow = builder.get_object("pathWindow")
        self.dirName = builder.get_object("dirName")
        self.entryProjectName = builder.get_object("entryProjectName")
        self.builder = builder
        
    def next_window(self, widget, data=None):
        if self.dirName.get_text() == "":
            md=Gtk.MessageDialog(None,
                                 Gtk.DialogFlags.DESTROY_WITH_PARENT,
                                 Gtk.MessageType.WARNING,
                                 Gtk.ButtonsType.CLOSE,
                                 "Specify directory for project")
            md.run()
            md.destroy()
        elif self.entryProjectName.get_text() == "":
            md=Gtk.MessageDialog(None,
                                 Gtk.DialogFlags.DESTROY_WITH_PARENT,
                                 Gtk.MessageType.WARNING,
                                 Gtk.ButtonsType.CLOSE,
                                 "Specify project name")
            md.run()
            md.destroy()
        else:
            self.parent.finalWindow.open_window(widget, data)
            self.pathWindow.hide()
        
    def open_window(self, widget, data=None):
        logging.info("Prev window")
        self.pathWindow.show_all()
   
    def prev_window(self, widget, data=None):
        self.pathWindow.hide()
        self.parent.open_window(widget, data)
    
    def get_data(self):
        return (self.dirName.get_text(), self.entryProjectName.get_text())
        
    def browse_path(self, window):
        dialog = Gtk.FileChooserDialog(
            "Please choose directory", self.pathWindow,
            Gtk.FileChooserAction.SELECT_FOLDER,
            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
             Gtk.STOCK_OPEN, Gtk.ResponseType.OK)
            )
        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            self.dirName.set_text(dialog.get_filename())
        dialog.destroy()
        
