import wx
import aiml
import win32com.client
from wx._controls import TE_PROCESS_ENTER
 
class Aplicacion(wx.Frame):
    def __init__(self):
        self.Ventana()
        self.Agente()
        
    def Agente(self):
        self.agente = aiml.Kernel()     
        self.agente.learn("data.xml")
        self.agente.respond("LOAD AIML")
        
        self.lector = win32com.client.Dispatch("SAPI.SpVoice")
        self.lector.Speak("Bienvenido al Sistema!!!")

    def Ventana(self):
        wx.Frame.__init__(self, None, style= wx.RESIZE_BORDER | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX)
        
        self.panel = wx.Panel(self)
        self.texto = wx.TextCtrl(self.panel, style=wx.TE_MULTILINE | wx.TE_READONLY | wx.TE_NO_VSCROLL, size= (293,350), pos = (5,5))
        self.linea = wx.TextCtrl(self.panel, style=wx.TE_NO_VSCROLL | TE_PROCESS_ENTER, size= (200,50), pos = (10,365))      
        self.boton = wx.BitmapButton(self.panel, bitmap = wx.Bitmap("recursos\enviar.png"), pos = (220, 360))
        self.etiqueta = wx.StaticText(self.panel, label = "Proyecto Inteligencia Artificial - ULA, A2012 ", pos = (5, 425))           
        
        self.Bind(wx.EVT_TEXT_ENTER, self.Pregunta, self.linea)
        self.Bind(wx.EVT_BUTTON, self.Pregunta, self.boton)
        
    def Pregunta(self, evento):
        persona = self.linea.GetValue()
        self.texto.AppendText("> " + persona + "\n")
        self.linea.Clear()
        self.Respuesta(persona)
        
    def Respuesta(self,persona):
        maquina = self.agente.respond(persona)
        self.texto.AppendText("- " + maquina + "\n")
        self.lector.Speak(maquina)