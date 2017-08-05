import PyQt4
from PyQt4.QtGui import *
from PyQt4 import QtGui, QtCore
import pickle
import SABRE2_GUI
import numpy

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s


class SABRE2_main_subclass(QMainWindow):
    def __init__(self, ui_layout):
        QMainWindow.__init__(self)
        self.ui = ui_layout
        ui_layout.setupUi(self)
        ui_layout.statusBar = self.statusBar()
        ui_layout.DefinitionTabs.hide()  # to hide problem definition tabs
        ui_layout.AnalysisTabs.hide()  # to hide analysis tabs
        # Members Table Arrangements

        self.Members_table_options = ["Mid Depth", "Flange 1", "Flange 2"]
        self.Members_table_position = 3
        Members_table_row, Members_table_column, Members_table_values = DataCollection.table_properties(
            self, ui_layout.Members_table)

        ui_layout.Mem_def_add.clicked.connect(
            lambda: TableChanges.add_new_row(self, ui_layout.Members_table, self.Members_table_options,
                                             self.Members_table_position, Members_table_values))

        # QtCore.QObject.connect(ui_layout.Mem_def_add, QtCore.SIGNAL(_fromUtf8("clicked()")),
        #                        TableChanges.add_new_row(self, ui_layout.Members_table, self.Members_table_options,
        #                                                 self.Members_table_position, Members_table_values))

        # The data update for members tab
        DataCollection.Assign_comboBox(self, ui_layout.Members_table, self.Members_table_options,
                                       self.Members_table_position, Members_table_values)
        DataCollection.update_values(self, ui_layout.Members_table, Members_table_row,
                                     Members_table_column, Members_table_values,
                                     self.Members_table_position)
        ui_layout.Members_table.itemChanged.connect(
            lambda: DataCollection.update_values(self, ui_layout.Members_table, Members_table_row,
                                                 Members_table_column, Members_table_values,
                                                 self.Members_table_position))

        Members_table_values = DataCollection.update_values(self, ui_layout.Members_table, Members_table_row,
                                                            Members_table_column, Members_table_values,
                                                            self.Members_table_position)

        # Add new row button

        ui_layout.Members_table.itemChanged.connect(lambda: print("main_screen",Members_table_values))
        # ui_layout.Members_table.clicked.connect(lambda: print(updated_values))

        # ui_layout.Members_table.itemChanged.connect(lambda: print(updated_values))
        # variable = ui_layout.Members_table.itemChanged.connect(lambda: DataCollection.update_values(self, ui_layout.Members_table, Members_table_row,
        #                                               Members_table_column, Members_table_values,
        #                                               self.Members_table_position))
        #
        # ui_layout.Joints_Table.clicked.connect(lambda: print(variable))

        ui_layout.Fixities_table.itemChanged.connect(
            lambda: DataCollection.update_values(self, ui_layout.Fixities_table, Fixities_table_row,
                                                 Fixities_table_column, Fixities_table_values,
                                                 self.Fixities_table_position))

        ui_layout.Fixities_table.itemChanged.connect(lambda: print(Fixities_table_values))
















        # File dropdown actions
        ui_layout.actionNew.triggered.connect(lambda: DropDownActions('uidesign').NewAct())
        ui_layout.actionOpen.triggered.connect(lambda: DropDownActions('uidesign').OpenAct())
        ui_layout.actionSave.triggered.connect(lambda: DropDownActions('uidesign').SaveAct())
        ui_layout.actionSave_As.triggered.connect(lambda: DropDownActions('uidesign').Save_AsAct())
        ui_layout.actionPrint.triggered.connect(lambda: DropDownActions('uidesign').PrintAct())
        ui_layout.actionPrint_Preview.triggered.connect(lambda: DropDownActions('uidesign').Print_PreviewAct())
        ui_layout.actionQuit.triggered.connect(qApp.quit)

        # Help dropdown actions
        ui_layout.actionAbout.triggered.connect(lambda: DropDownActions('uidesign').AboutAct())

        # Status/message bar and progress bar
        # ui_layout.statusbar = PyQt4.QtGui.QStatusBar()
        # ui_layout.statusbar.setObjectName(_fromUtf8("statusbar"))
        # message = "Start creating the model by defining the joints"  # Update message with modeling progress and interupts ***************
        # ui_layout.statusbar.showMessage(message)
        # QMainWindow.setStatusBar(QMainWindow, ui_layout.statusbar)

        ui_layout.progressBar = PyQt4.QtGui.QProgressBar()
        ui_layout.statusbar.addPermanentWidget(ui_layout.progressBar)
        analysisprogress = 0  # Update this value later by integrating with analysis**********
        ui_layout.progressBar.setValue(analysisprogress)
        ui_layout.progressBar.setTextVisible(True)


class DropDownActions(QMainWindow):
    """docstring for Actions"""

    def __init__(self, ui_layout):
        QMainWindow.__init__(self)
        self.ui = ui_layout

    def AboutAct(ui_layout):
        # message = "Learn about Sabre2"
        # self.statusbar.showMessage(message)

        # Program information
        version = "3.0"
        website = "http://www.white.ce.gatech.edu/sabre"
        email = "fill in data"
        license_link = "fill in data"
        license_name = "fill in data"

        # Dialog box
        about_box = SABRE2_GUI.QtGui.QMessageBox()
        about_box.setWindowTitle("About Sabre2 Version 3.0")
        about_box.setTextFormat(SABRE2_GUI.QtCore.Qt.RichText)
        # about_box.setIconPixmap(QtGui.QPixmap(ComicTaggerSettings.getGraphic('about.png'))) #include image
        about_box.setText("""
        <HTML>
        <p><b>This demo shows use of <c>QTableWidget</c> with custom handling for
         individual cells.</b></p>
        <p>Using a customized table item we make it possible to have dynamic
         output in different cells. The content that is implemented for this
         particular demo is:
        <ul>
        <li>Adding two cells.</li>
        <li>Subtracting one cell from another.</li>
        <li>Multiplying two cells.</li>
        <li>Dividing one cell with another.</li>
             <li>Summing the contents of an arbitrary number of cells.</li>
             </HTML>
         """)
        about_box.setStandardButtons(SABRE2_GUI.QtGui.QMessageBox.Ok)
        about_box.exec_()

    def NewAct(self):
        # message = "Create a new file"
        # self.statusbar.showMessage(message)

        fileName = []
        inpdata = []
        # clear all user inputs
        # reset OpenGL screen
        # reset messages

    def OpenAct(self):
        # message = "Open an existing file"
        # self.statusbar.showMessage(message)

        fileName = PyQt4.QtGui.QFileDialog.getOpenFileName(None, "Open Sabre2 File", '',
                                                           "Sabre2 Files (*.mat);;All Files (*)")
        if not fileName:
            return
        try:
            in_file = open(str(fileName), 'rb')
        except IOError:
            QtGui.QMessageBox.information(self, "Unable to open file", "There was an error opening \"%s\"" % fileName)
            return

        inpdata = []
        inpdata = pickle.load(in_file)
        in_file.close()

        if len(inpdata) == 0:
            QtGui.QMessageBox.information(self, "File is empty")
        else:
            # needs to be updated once data structure is determined**************************
            for name, address in inpdata:
                self.nameLine.setText(name)
                self.addressText.setText(address)

        self.updateInterface(self.NavigationMode)

        # Fill in spread sheet cells
        # update OpenGL screen
        # update messages
        # go directly to analysis screen

    def SaveAct(self):
        # message = "Save the model to disk"
        # self.statusbar.showMessage(message)

        inpdata = "text test addon"
        # fileName = "test1.txt"

        if len(inpdata) == 0:
            QtGui.QMessageBox.information(self, "No data has been attributed to the model")
        else:
            try:
                fileName
            except NameError:  # if data has not been saved to a file yet invoke popup save screen
                import pickle
                fileName = PyQt4.QtGui.QFileDialog.getSaveFileName(None, "Save Sabre2 File", '',
                                                                   "Sabre2 File (*.mat);;All Files (*)")
                if not fileName:
                    return
                try:
                    out_file = open(str(fileName), 'wb')
                except IOError:
                    PyQt4.QtGui.QMessageBox.information(self, "Unable to open file",
                                                        "There was an error opening \"%s\"" % fileName)
                    return

                pickle.dump(inpdata, out_file)
                out_file.close()
            else:
                import pickle
                try:  # if file already exists skip popup and update save file
                    out_file = open(str(fileName), 'wb')
                except IOError:
                    PyQt4.QtGui.QMessageBox.information(self, "Unable to open file",
                                                        "There was an error opening \"%s\"" % fileName)
                    return

                pickle.dump(inpdata, out_file)
                out_file.close()

    def Save_AsAct(self):
        # message = "Name the file saved to disk"
        # self.statusbar.showMessage(message)

        inpdata = "text test"

        # Invoke save popup screen
        if len(inpdata) == 0:
            QtGui.QMessageBox.information(self, "No data has been attributed to the model")
        else:
            import pickle
            fileName = PyQt4.QtGui.QFileDialog.getSaveFileName(None, "Save Sabre2 File As", '',
                                                               "Sabre2 File (*.mat);;All Files (*)")
            if not fileName:
                return
            try:
                out_file = open(str(fileName), 'wb')
            except IOError:
                PyQt4.QtGui.QMessageBox.information(self, "Unable to open file",
                                                    "There was an error opening \"%s\"" % fileName)
                return

            pickle.dump(inpdata, out_file)
            out_file.close()

    def PrintAct(self):
        message = "Print screen"
        self.statusbar.showMessage(message)

        # not sure what we are printing?
        # data, results, or just screenshot of OpenGL?

    def Print_PreviewAct(self):
        message = "Preview screen print"
        self.statusbar.showMessage(message)

    def statusMessage(self, message):
        self.ui.statusBar.showMessage(message)


class DataCollection(QMainWindow):
    """docstring for Actions"""

    def __init__(self, ui_layout):
        QMainWindow.__init__(self)
        self.ui = ui_layout

    def Assign_comboBox(self, tableName, options, position, values):
        combo_box = QtGui.QComboBox()
        flag_combo = 1
        for t in options:
            combo_box.addItem(t)
        r = tableName.rowCount()
        c = tableName.columnCount()
        for i in range(r):
            combo_box = QtGui.QComboBox()
            for t in options:
                combo_box.addItem(t)
            tableName.setCellWidget(i, position, combo_box)
            combo_box.activated.connect(
                lambda: DataCollection.update_values(self, tableName, r, c, values, position))
        text_trigger = tableName.item(0, 3)
        if text_trigger.text() == "1":
            tableName.item(0, 3).setText("0")
        else:
            tableName.item(0, 3).setText("1")
        return tableName

    def Assign_checkBox(self, tableName, options, position, values):
        check_box = QtGui.QCheckBox()
        flag_check = 1; flag_uncheck = 0
        r = tableName.rowCount()
        c = tableName.columnCount()
        for i in range(r):
            check_box = QtGui.QCheckBox()
            tableName.setCellWidget(i, position, check_box)
            check_box.clicked.connect(
                lambda: DataCollection.update_values(self, tableName, r, c, values, position, i, flag_check))
        text_trigger = tableName.item(0, 1)
        if text_trigger.text() == "1":
            tableName.item(0, 1).setText("0")
        else:
            tableName.item(0, 1).setText("1")
        return tableName

    def table_properties(self, edit):
        """Initializing the table properties"""

        row = edit.rowCount()
        column = edit.columnCount()
        r, c = row, column
        # table_initiation = [[0 for x in range(r)] for y in range(c)]  # initialize table values
        table_initiation = numpy.zeros((row, column))
        # print("table initiation  = " , table_initiation)
        # print("table initiation1  = " , numpy.matrix(table_initiation1))
        # # Members_table_values = numpy.array(Members_table_values)
        # # Members_table_values = numpy.transpose(Members_table_values)
        # # print(Members_table_values)
        return r, c, table_initiation

    def update_values(self, tableName, numberRow, numberCol, val1, position):
        col = tableName.currentColumn()
        row = tableName.currentRow()
        row_check = tableName.rowCount()
        col_check = tableName.columnCount()

        if row_check > (numpy.size(val1, 0)):
            table_add = numpy.zeros((1, col_check))
            for i in range(row_check - numpy.size(val1, 0)):
                val1 = numpy.append(val1, table_add, axis=0)

        if row == -1:
            pass
        else:
            try:
                for i in range(row_check+1):
                    for j in range(col_check):
                        if tableName.item(i, j) is None:
                            pass
                        elif j == position:
                            value_combo = tableName.cellWidget(i, position).currentIndex()
                            val1[i, position] = value_combo
                            DropDownActions.statusMessage(self, message="")
                        else:
                            val1[i, j] = float(tableName.item(i, j).text())
                            DropDownActions.statusMessage(self, message="")
            except ValueError:
                tableName.clearSelection()
                tableName.item(row, col).setText("")
                DropDownActions.statusMessage(self, message="Please enter only numbers!")
        print("val1", val1)
        return val1


class TableChanges(QMainWindow):
    """This Class is imposing the changes on the Definition Tables"""

    def __init__(self, ui_layout):
        QMainWindow.__init__(self)
        self.ui = ui_layout
        datacollection = DataCollection()

    def add_new_row(self, tableName, options, position, values):
        row_position = tableName.rowCount()
        col_number = tableName.columnCount()

        tableName.insertRow(row_position)

        DataCollection.Assign_comboBox(self, tableName, options, position, values)
