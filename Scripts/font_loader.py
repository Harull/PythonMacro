from PySide2.QtGui import QFontDatabase, QFont

class FontLoader():

    @staticmethod
    def GetQFont(path : str):
        font_id = QFontDatabase.addApplicationFont(path)
        if font_id == -1:
            print("Error : Impossible to load the font")
        else:
            font_families = QFontDatabase.applicationFontFamilies(font_id)
            if font_families:
                return QFont(font_families[0], 12) 