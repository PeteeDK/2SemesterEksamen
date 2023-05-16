import FrontEnd as FrontEnd
import Backend as Backend


class Controller:
    def __init__(self, CheckInAndOut, View):
        Backend.CheckInAndOut = CheckInAndOut
        FrontEnd.MainPage = View

