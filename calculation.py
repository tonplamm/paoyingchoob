import arcade
from random import randint

class allAboutScore:

    def __init__(self, screen):
        self.screen = screen
        self.button_1 = 1
        self.button_2 = 1
        self.button_3 = 1
        self.player_left_1 = 0
        self.player_left_2 = 0
        self.player_left_3 = 0
        self.player_right_1 = 0
        self.player_right_2 = 0
        self.player_right_3 = 0
        self.score_left = -1
        self.score_right = 0
        self.canplay = True

    def on_key_press(self, key, key_modifiers):
        if (self.player_left_1 != self.button_1 or self.player_left_2 != self.button_2 or self.player_left_3 != self.button_3) and self.canplay == True:
            if key == arcade.key.A:
                self.player_left_1 += 1
                if self.player_left_1 > self.button_1:
                    self.player_left_1 = 0
            elif key == arcade.key.S:
                self.player_left_2 += 1
                if self.player_left_2 > self.button_2:
                    self.player_left_2 = 0
            elif key == arcade.key.D:
                self.player_left_3 += 1
                if self.player_left_3 > self.button_3:
                    self.player_left_3 = 0
            if self.player_left_1 == self.button_1 and self.player_left_2 == self.button_2 and self.player_left_3 == self.button_3:
                self.score_left += 1
                self.canplay = False

        if (self.player_right_1 != self.button_1 or self.player_right_2 != self.button_2 or self.player_right_3 != self.button_3) and self.canplay == True:
            if key == arcade.key.J:
                self.player_right_1 += 1
                if self.player_right_1 > self.button_1:
                    self.player_right_1 = 0
            elif key == arcade.key.K:
                self.player_right_2 += 1
                if self.player_right_2 > self.button_2:
                    self.player_right_2 = 0
            elif key == arcade.key.L:
                self.player_right_3 += 1
                if self.player_right_3 > self.button_3:
                    self.player_right_3 = 0
            if self.player_right_1 == self.button_1 and self.player_right_2 == self.button_2 and self.player_right_3 == self.button_3:
                self.score_right += 1
                self.canplay = False

        if (self.score_left == 3 or self.score_right == 3) and key == arcade.key.SPACE:
            self.score_left = 0
            self.score_right = 0
        elif self.canplay == False and key == arcade.key.SPACE:
            self.canplay = True
            self.button_1 = randint(1, 10)
            self.button_2 = randint(1, 10)
            self.button_3 = randint(1, 10)
            self.player_left_1 = 0
            self.player_left_2 = 0
            self.player_left_3 = 0
            self.player_right_1 = 0
            self.player_right_2 = 0
            self.player_right_3 = 0
