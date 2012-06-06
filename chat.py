#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Interfaz del representante de atención al cliente

import pygtk
import aiml
import os.path
from festival import say
pygtk.require('2.0')
import gtk

rac = aiml.Kernel()
rac.learn("RAC.aiml")
rac.respond("LOAD AIML")

class Chatbot:
    def callback(self, widget, textview, entrada):
        self.text = "Tu: "+self.entrada.get_text()
        self.bot = rac.respond(self.entrada.get_text())
        enditer = self.textbuffer.get_end_iter()
        self.textbuffer.insert(enditer, "\n" + self.text)
        self.textbuffer.insert(enditer, "\nRAC: " + self.bot)
        self.entrada.set_text("")
        if self.sonido.get_active():
            say(self.text)
            say("RAC: "+self.bot )

    def delete_event(self, widget, event, data=None):
        gtk.main_quit()
        return gtk.FALSE

    def __init__(self):
        self.chat = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.chat.set_resizable(gtk.TRUE)
        self.chat.set_size_request(300, 400)
        self.chat.set_title("Representante de atención al cliente")
        self.chat.connect("delete_event", self.delete_event)
        self.chat.set_border_width(10)

        self.sw = gtk.ScrolledWindow()
        self.sw.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
        self.hbox = gtk.HBox(gtk.FALSE, 0)

        self.vbox = gtk.VBox(gtk.FALSE, 0)
        self.chat.add(self.vbox)

        self.lectura = gtk.TextView()
        self.textbuffer = self.lectura.get_buffer()
        self.textbuffer.set_text("Bienvenidos al sistema de atención al cliente")
        self.sw.add(self.lectura)
        self.lectura.set_editable(gtk.FALSE)
        self.sw.show()
        self.lectura.show()
        self.vbox.pack_start(self.sw, gtk.TRUE, gtk.TRUE, 0)

        self.entrada = gtk.Entry()
        self.entrada.connect("activate", self.callback, self.textbuffer, self.entrada.get_text())
        self.entrada.show()
        self.vbox.pack_start(self.entrada, gtk.FALSE, gtk.FALSE, 5)

        # creación de los botones.
        self.hboton = gtk.HButtonBox()
        self.hboton.show()
        self.enviar = gtk.Button("Enviar")
        self.enviar.connect("clicked", self.callback, self.textbuffer, self.entrada.get_text())
        self.hboton.add(self.enviar)
        self.enviar.show()
        self.cerrar = gtk.Button("Cerrar")
        self.cerrar.connect("clicked", lambda w: gtk.main_quit())
        self.hboton.add(self.cerrar)
        self.cerrar.show()
        self.sonido = gtk.CheckButton("Activar la voz")
        self.sonido.set_active(gtk.TRUE)
        self.hboton.add(self.sonido)
        self.sonido.show()

        self.vbox.pack_start(self.hboton, gtk.FALSE, gtk.FALSE, 0)

        self.hbox.show()
        self.vbox.show()
        self.chat.show()

def main():
    gtk.main()

if __name__ == "__main__":
    Chatbot()
    main()
