from .drivers import Chrome, Firefox, Android, Ios
from .app_ui import AppUi

from unittest import TestCase as _TestCase

import logging

from configuration import configuration as cfg


class BaseTest(_TestCase):
    # TODO rewrite this so that logging works
    #  currently unittest rewires stdout and logging isn't working afterwards
    #  see https://stackoverflow.com/questions/7472863
    #  consider the metaclass approach
    #  together with writing custom set_up and tear_down and possibly runner

    def setUp(self) -> None:
        self.log = logging.getLogger(__name__)
        self.log.info(f"Test case setup")
        self.app = AppUi(Firefox())
        # self.app = AppUi(Chrome())
        # self.app.go_to_url(cfg.URL)

    def tearDown(self) -> None:
        self.log.info(f"Closing application.")
        self.app.quit()
