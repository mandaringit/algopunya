# import sys
#
# sys.stdin = open('input.txt', 'r')


class StemCell:

    def __init__(self, hp):
        self.life = hp  # 생명력 기준
        self.hp = hp  # 깎을 생명력
        self.is_activate = False
        self.passed_time = 0
        self.dead = False

    def plus_one_hour(self):  # 한시간 경과 후
        if not self.dead:
            self.passed_time += 1  # 시간을 추가하고

            if self.is_activate:  # 만약 활성상태였으면
                self.hp -= 1  # 생명력도 깎고
                if self.hp == 0:
                    self.dead = True

            # passed_time이 hp시간동안 비활성상태
            if self.passed_time == self.life:
                self.is_activate = True



#
# T = int(input())
#
# for tc in range(1, T + 1):
#

