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
    background: #2b2b2b;           
    width: 10px;                   
    margin: 0px 0px 0px 0px;       
    border: none;                  
    }

    QScrollBar::handle:vertical {
        background: #5c5c5c;           
        min-height: 20px;              
        border-radius: 5px;            
    }

    QScrollBar::handle:vertical:hover {
        background: #888888;           
    }

    QScrollBar::handle:vertical:pressed {
        background: #aaaaaa;         
    }

    QScrollBar::sub-line:vertical,
    QScrollBar::add-line:vertical {
        height: 0px;                   
        width: 0px;
    }

    QScrollBar::add-page:vertical, 
    QScrollBar::sub-page:vertical {
        background: none;             
    }

    QScrollBar:horizontal {
        background: #2b2b2b;
        height: 10px;
        margin: 0px 0px 0px 0px;
        border: none;
    }

    QScrollBar::handle:horizontal {
        background: #5c5c5c;
        min-width: 20px;
        border-radius: 5px;
    }

    QScrollBar::handle:horizontal:hover {
        background: #888888;
    }

    QScrollBar::handle:horizontal:pressed {
        background: #aaaaaa;
    }

    QScrollBar::sub-line:horizontal,
    QScrollBar::add-line:horizontal {
        width: 0px;
        height: 0px;
    }

    QScrollBar::add-page:horizontal, 
    QScrollBar::sub-page:horizontal {
        background: none;
    }

    QListWidget {
    background-color: #2b2b2b;      /* Dark background for the list */
    border: 1px solid #3c3c3c;      /* Thin border around the list */
    color: #ffffff;                 /* Text color */
    padding: 5px;
    border-radius: 5px;             /* Slight rounding for a clean look */
    }

    QListWidget::item {
        background-color: #3c3c3c;      /* Dark gray for each item background */
        padding: 10px;                  /* Padding around text */
        margin: 3px 0;                  /* Spacing between items */
        border-radius: 5px;             /* Rounded corners for each item */
        color: #ffffff;                 /* Text color */
    }

    QListWidget::item:hover {
        background-color: #444444;      /* Slightly lighter gray when hovered */
    }

    QListWidget::item:selected {
        background-color: #555555;      /* Different gray when selected */
        color: #ffffff;                 /* Keep text color white when selected */
    }

    QListWidget::item:selected:active {
        background-color: #666666;      /* Slightly darker when clicked/active */
    }

    QListWidget::item:selected:!active {
        background-color: #4d4d4d;      /* Gray when item is selected but not active (focus lost) */
    }
"""
