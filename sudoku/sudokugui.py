# pylint: disable=no-member

import wx
import wx.grid as gridlib
import numpy
from pandas import DataFrame
import sudoku

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
        self.reset(0)
        self.myGrid.HideColLabels()
        self.myGrid.HideRowLabels()
        self.myGrid.AutoSize()

        btnResolver = wx.Button(panel, wx.ID_ANY, 'Resolver', (10, 10))
        btnResolver.Bind(wx.EVT_BUTTON, self.resolver)

        btnReset = wx.Button(panel, wx.ID_ANY, 'Reset', (10, 10))
        btnReset.Bind(wx.EVT_BUTTON, self.reset)

        # and create a sizer to manage the layout of child widgets
        sizer = wx.BoxSizer(wx.VERTICAL)
        # sizer.Add(st, wx.SizerFlags().Border(wx.TOP|wx.LEFT, 25))
        sizer.Add(self.myGrid)#, 1, wx.EXPAND
        sizer.Add(btnResolver)#, wx.SizerFlags().Border(wx.BOTTOM|wx.RIGHT, 25))
        sizer.Add(btnReset)#, wx.SizerFlags().Border(wx.BOTTOM|wx.RIGHT, 25))
        panel.SetSizer(sizer)

    def intMio(self, str):
        if str == '':
            return 0
        else:
            return int(str)

    def reset(self, event):
        for i in range(9):
            for j in range(9):
                self.myGrid.SetCellValue(i, j, '0')

    def resolver(self, event):
        matRes = numpy.zeros((9,9), int)
        for i in range(9):
            for j in range(9):
                matRes[i][j] = self.intMio(self.myGrid.GetCellValue(i,j))
        matRes = sudoku.main(matRes)
        for i in range(9):
            for j in range(9):
                self.myGrid.SetCellValue(i,j, str(matRes[i][j]))

if __name__ == '__main__':
    # When this module is run (not imported) then create the app, the
    # frame, show it, and start the event loop.
    app = wx.App()
    frm = MyFrame(None, title='Resolver Sudokus')
    frm.Show()
    app.MainLoop()