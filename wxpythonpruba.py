# First things, first. Import the wxPython package.
# pylint: disable=no-member

import wx
import wx.grid as gridlib
import numpy
from pandas import DataFrame

class MyFrame(wx.Frame):
    """
    A Frame that says Hello World
    """

    def __init__(self, *args, **kw):
        # ensure the parent's __init__ is called
        super(MyFrame, self).__init__(*args, **kw)

        # create a panel in the frame
        panel = wx.Panel(self)

        self.myGrid = gridlib.Grid(panel)
        self.myGrid.CreateGrid(9, 9)

        for i in range(9):
            for j in range(9):
                self.myGrid.SetCellValue(i, j, '0')

        self.myGrid.AutoSize()

        button = wx.Button(panel, wx.ID_ANY, 'Test', (10, 10))
        button.Bind(wx.EVT_BUTTON, self.onButton)

        # and create a sizer to manage the layout of child widgets
        sizer = wx.BoxSizer(wx.VERTICAL)
        # sizer.Add(st, wx.SizerFlags().Border(wx.TOP|wx.LEFT, 25))
        # sizer.Add(self.myGrid, 1, wx.LEFT)
        sizer.Add(self.myGrid, proportion=0, border=0)
        sizer.Add(button, proportion=0, border=2)
        panel.SetSizer(sizer)

    def intMio(self, str):
        if str == '':
            return 0
        else:
            return int(str)

    def onButton(self, event):
        matRes = numpy.array((9,9), int)
        for i in range(9):
            for j in range(9):
                matRes[i][j] = self.intMio(self.myGrid.GetCellValue(i,j))
        print(DataFrame(matRes))

if __name__ == '__main__':
    # When this module is run (not imported) then create the app, the
    # frame, show it, and start the event loop.
    app = wx.App()
    frm = MyFrame(None, title='Resolver Sudokus')
    frm.Show()
    app.MainLoop()