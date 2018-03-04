"""Hello, wxPython! program."""
import wx


class Frame(wx.Frame):
    """Frame class that displays an image."""

    def __init__(self, image, parent=None, id=-1, pos=wx.DefaultPosition, title='Hello, Python!'):
        """Create a Frame instance and display image."""
        temp = image.ConvertToBitmap()
        size = temp.GetWidth(), temp.GetHeight()
        wx.Frame.__init__(self, parent, id, title, pos, size)
        self.bmp = wx.StaticBitmap(parent=self, bitmap=temp)


# 你没有必要创建你自己的wx.App子类，你通常想这样做是为了能够在OnInit()方法中创建你的顶级框架。
# 通常，如果在系统中只有一个框架的话，避免创建一个wx.App子类是一个好的主意。
class App(wx.App):
    """Application class."""

    def OnInit(self):
        image = wx.Image('wxPython.jpg', wx.BITMAP_TYPE_JPEG)
        self.frame = Frame(image)
        self.frame.Show()
        self.SetTopWindow(self.frame)
        return True


if __name__ == '__main__':
    app = App()
    app.MainLoop()
