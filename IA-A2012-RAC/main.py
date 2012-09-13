import wx
from app import Aplicacion
    
if __name__ == '__main__':
    app = wx.PySimpleApp()
    chat = Aplicacion()
    app.MainLoop()
