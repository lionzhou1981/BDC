import os
import time
import json
import Common
from pages import PageBase


class PageMain(PageBase.PageBase):
    def __init__(self, _display):
        super(PageMain, self).__init__(_display, "PageMain")
