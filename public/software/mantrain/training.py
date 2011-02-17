#!/usr/bin/env python














import random, wx

def randIter(lst):
    while True:
        random.shuffle(lst)
        for l in lst:
            yield l

class Trainer(wx.Frame):
    def __init__(self, parent, id, iterator):
        self.iterator = iterator
        title = 'Trainer'
        size = (245,234)
        wx.Frame.__init__(self, parent, id, title, size=size)
        # max: 245x234
        self.img = wx.StaticBitmap(self, 1, size=size)
        self.txt = wx.TextCtrl(self)

        self.txt.Bind(wx.EVT_TEXT, self.OnKeyPress)
        self.txt.SetFocus()

        self.NewGraphic()

        self.Show(True)

    def OnKeyPress(self, evt):
        if evt.GetString() == self.answer:
            self.txt.SetValue('')
            self.NewGraphic()

    def NewGraphic(self):
        self.answer, self.imgpath = self.iterator.next()
        self.bitmap = wx.Bitmap(self.imgpath)
        self.img.SetBitmap(self.bitmap)

if __name__ == '__main__':
    asl = [(c, 'asl/'+c+'.jpg') for c in 'abcdefghijklmnopqrstuvwxyz']

    app = wx.PySimpleApp()
    frame = Trainer(None, wx.ID_ANY, randIter(asl))
    app.MainLoop()
