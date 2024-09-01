from django.shortcuts import render # type: ignore

# Create your views here.

class Timer:
    def __init__(self):
        self.PRE_TIME_1H = 360 #プリセット1時間
        self.PRE_TIME_2H = 720 #プリセット2時間
        self.PRE_TIME_30M = 180 #プリセット30分
    
    def preset_time(self):
        self.PRE_TIME_1H = 360 #プリセット1時間
        self.PRE_TIME_2H = 360 #プリセット2時間
        self.PRE_TIME_30M = 360 #プリセット30分

    def userstimer(self):
        return 0

class tasklist:
    def __init__(self) -> None:
        pass