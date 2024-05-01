import os
from .types import Mode


# initialize real terminal
os.system("")


class Window:
    """
    Terminal window class
    """

    # terminal mode
    _mode: Mode | None = None

    # real terminal width and height
    _terminal_width: int = os.get_terminal_size().columns
    _terminal_height: int = os.get_terminal_size().lines

    # virtual terminal resolution (will equal to real one if high_res flag is not set)
    _width: int = _terminal_width
    _height: int = _terminal_height

    # terminal image buffer
    _disp_buffer: list[int] = list()

    @classmethod
    def initialize(cls, mode: Mode):
        """
        Initializes the window with given mode
        """

        # change mode
        cls._mode = mode

        # any kind of color mode cannot work with high_res flag
        if mode is not Mode.bw and mode is Mode.high_res:
            raise NotImplementedError("Unable to have color with high_res flag enabled")

        # update virtual width and height
        cls._width = cls._terminal_width if mode is not Mode.high_res else cls._terminal_width * 2
        cls._height = cls._terminal_height if mode is not Mode.high_res else cls._terminal_height * 4

        # initialize the image buffer
        cls._disp_buffer = [0 for _ in range(cls._width * cls._height)]

    @classmethod
    def update(cls):
        """
        Updates the image displayed
        """