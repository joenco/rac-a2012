import wx
from wx._controls import TE_PROCESS_ENTER
from rivescript import RiveScript
from win32com.client import Dispatch
 
class Aplicacion(wx.Frame):
    def __init__(self):
        self.Ventana()
        self.Agente()
        
    def Agente(self):
        self.agente = RiveScript()
        self.agente.load_directory("./recursos")
        self.agente.sort_replies()
        self.lector = Dispatch("SAPI.SpVoice")
        self.lector.Speak("Bienvenido al Sistema!")

    def Ventana(self):
        wx.Frame.__init__(self, None, style= wx.RESIZE_BORDER | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX)
        self.panel = wx.Panel(self)
        self.texto = wx.TextCtrl(self.panel, style=wx.TE_MULTILINE | wx.TE_READONLY, size= (293,350), pos = (5,5))
        self.linea = wx.TextCtrl(self.panel, style=wx.TE_NO_VSCROLL | TE_PROCESS_ENTER, size= (200,50), pos = (10,365))      
        self.boton = wx.BitmapButton(self.panel, bitmap = wx.Bitmap("recursos\_enviar.png"), pos = (220, 360))
        self.etiqueta = wx.StaticText(self.panel, label = "Proyecto Inteligencia Artificial - ULA, A2012 ", pos = (5, 425))          
        self.Bind(wx.EVT_TEXT_ENTER, self.Pregunta, self.linea)
        self.Bind(wx.EVT_BUTTON, self.Pregunta, self.boton)        
        self.linea.SetFocus()
        
    def Pregunta(self, evento):
        self.texto.AppendText("> " + self.linea.GetValue() + "\n")
        self.Respuesta() 
                
    def Respuesta(self):
        bot = self.agente.reply("rac", self.linea.GetValue().__str__())
        self.linea.Clear()
        self.texto.AppendText("- " + str(bot).capitalize() + "\n")
        self.lector.Speak(bot)
        if self.agente.get_uservar("rac", "disconnect") != "undefined":
            self.Close(True)
      