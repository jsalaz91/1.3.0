import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout

def launch_dashboard():
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle("Arbitrage Bot Dashboard")

    layout = QVBoxLayout()
    label = QLabel("Phase 13 Dashboard is Live")
    layout.addWidget(label)

    window.setLayout(layout)
    window.resize(300, 100)
    window.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    launch_dashboard()
