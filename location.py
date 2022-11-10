
class Location:
    room_image = "" # room image path

    def __init__(self, center_x, center_y):
        self.cx = center_x
        self.cy = center_y
        self.location = 0

    def get_location(self):
        if self.cy > 270:       # 1번 줄
            if 10 < self.cx < 200:      # 1번 자리
                self.location = 1
            elif 230 < self.cx < 400:   # 2번 자리
                self.location = 2
            elif 420 < self.cx < 570:   # 3번 자리
                self.location = 3
            elif 590 < self.cx:         # 4번 자리
                self.location = 4
        
        elif self.cy > 190:     # 2번 줄
            if 20 < self.cx < 130:      # 1번 자리
                self.location = 5
            elif 160 < self.cx < 270:   # 2번 자리
                self.location = 6
            elif 290 < self.cx < 390:   # 3번 자리
                self.location = 7
            elif 400 < self.cx:         # 4번 자리
                self.location = 8

        elif self.cy > 140:     # 3번 줄
            if 0 < self.cx < 80:      # 1번 자리
                self.location = 9
            elif 100 < self.cx < 190:   # 2번 자리
                self.location = 10
            elif 230 < self.cx < 300:   # 3번 자리
                self.location = 11
            elif 310 < self.cx < 380:         # 4번 자리
                self.location = 12

        elif self.cy > 110:     # 4번 줄
            if 10 < self.cx < 70:      # 1번 자리
                self.location = 13
            elif 80 < self.cx < 140:   # 2번 자리
                self.location = 14
            elif 170 < self.cx < 230:   # 3번 자리
                self.location = 15
            elif 250 < self.cx < 300:         # 4번 자리
                self.location = 16

        else:                   # 5번 줄
            if 0 < self.cx < 50:      # 1번 자리
                self.location = 17
            elif 55 < self.cx < 100:   # 2번 자리
                self.location = 18
            elif 120 < self.cx < 170:   # 3번 자리
                self.location = 19
            elif 180 < self.cx < 220:         # 4번 자리
                self.location = 20
    
        return self.location

    

