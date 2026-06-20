import os
import sys
import unittest

if sys.platform.startswith("linux"):
    os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

from qtpy import QtCore

from stream_viewer.applications.main import LSLViewer, create_application as create_main_application
from stream_viewer.applications.stream_status_qml import (
    StreamStatusWindow,
    create_application as create_status_application,
)


class SmokeTestCase(unittest.TestCase):
    def _run_window_smoke_test(self, app_factory, window_factory):
        app = app_factory([])
        window = window_factory()
        window.show()
        app.processEvents()

        self.assertTrue(window.isVisible())

        QtCore.QTimer.singleShot(100, app.quit)
        app.exec_()

        window.close()
        app.processEvents()

    def test_lsl_viewer_launches(self):
        self._run_window_smoke_test(create_main_application, LSLViewer)

    def test_lsl_status_launches(self):
        self._run_window_smoke_test(create_status_application, StreamStatusWindow)


if __name__ == "__main__":
    unittest.main()
