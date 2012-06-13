import wx
from chat import Chat

if __name__ == '__main__':
    app = wx.PySimpleApp()

    ventana = Chat()
    ventana.SetTitle("Representante de Atencion al Cliente")
    ventana.SetSize((320,480))
    ventana.Centre()
    ventana.Show()

    app.MainLoop()
