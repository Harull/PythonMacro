dark_theme = """
    QMainWindow {
        background-color: #2b2b2b;
    }
    
    QWidget {
        background-color: #2b2b2b;
        color: #f0f0f0;
        font-size: 12pt;
    }
    
    QMenuBar {
        background-color: #333;
        color: #f0f0f0;
        font-size: 12pt;
    }

    QMenuBar::item {
        background-color: #333;
        color: #f0f0f0;
    }

    QMenuBar::item:selected {
        background-color: #444;
    }

    QMenu {
        background-color: #333;
        color: #f0f0f0;
    }

    QMenu::item:selected {
        background-color: #444;
    }

    QMenu::separator {
        height: 1px;
        background: #555;
    }

    QPushButton {
        background-color: #555;
        color: #f0f0f0;
        border: 1px solid #444;
        padding: 5px;
        border-radius: 4px;
    }

    QPushButton:hover {
        background-color: #666;
    }

    QPushButton:pressed {
        background-color: #777;
    }
    
    QPConsoleWidget{
        background-color: #141414;
        color: #ffcb21;
        border: 1px solid #555;
        padding: 5px;
    }

    QLineEdit {
        background-color: #444;
        color: #f0f0f0;
        border: 1px solid #555;
        padding: 5px;
    }

    QLineEdit:focus {
        border: 1px solid #888;
    }

    QLabel {
        color: #f0f0f0;
    }

    QComboBox {
        background-color: #444;
        color: #f0f0f0;
        border: 1px solid #555;
        padding: 3px;
    }

    QComboBox::drop-down {
        subcontrol-origin: padding;
        subcontrol-position: top right;
        width: 15px;
        border-left: 1px solid #555;
    }

    QComboBox QAbstractItemView {
        background-color: #333;
        color: #f0f0f0;
        selection-background-color: #444;
    }

    QScrollBar:vertical {
        background-color: #333;
        width: 12px;
        margin: 18px 0 18px 0;
    }

    QScrollBar::handle:vertical {
        background-color: #555;
        min-height: 20px;
        border-radius: 4px;
    }

    QScrollBar::add-line:vertical {
        background-color: #444;
        height: 18px;
        subcontrol-position: bottom;
        subcontrol-origin: margin;
    }

    QScrollBar::sub-line:vertical {
        background-color: #444;
        height: 18px;
        subcontrol-position: top;
        subcontrol-origin: margin;
    }

    QScrollBar:horizontal {
        background-color: #333;
        height: 12px;
        margin: 0 18px 0 18px;
    }

    QScrollBar::handle:horizontal {
        background-color: #555;
        min-width: 20px;
        border-radius: 4px;
    }

    QScrollBar::add-line:horizontal {
        background-color: #444;
        width: 18px;
        subcontrol-position: right;
        subcontrol-origin: margin;
    }

    QScrollBar::sub-line:horizontal {
        background-color: #444;
        width: 18px;
        subcontrol-position: left;
        subcontrol-origin: margin;
    }
"""
