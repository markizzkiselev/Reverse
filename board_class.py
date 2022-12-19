import pygame
from config import *
from random import choice


class Board:
    def __init__(self, dim, screen):
        self.x_px = dim[0]
        self.y_px = dim[1]

        self.x = self.x_px // CELL_SIZE
        self.y = self.y_px // CELL_SIZE

        self.matrix = []
        for _ in range(self.x):
            row = []
            for _ in range(self.y):
                row.append(choice([0, 1]))
            self.matrix.append(row)

        self.now_player = 0

        self.screen = screen

    def turn(self, xy):
        if self.matrix[xy[0]][xy[1]] == self.now_player:
            for i in self.matrix:
                i[xy[1]] = self.now_player
            self.matrix[xy[0]] = [self.now_player] * self.y
            self.next_player()

    def next_player(self):
        if self.now_player == 1:
            self.now_player = 0
        else:
            self.now_player = 1

    def draw_cell(self, xy):
        if self.matrix[xy[0]][xy[1]] == 0:
            pygame.draw.circle(self.screen,
                               CELL_COLOR_0,
                               (xy[0] * CELL_SIZE + CELL_SIZE // 2,
                                xy[1] * CELL_SIZE + CELL_SIZE // 2),
                               CELL_SIZE // 2 - 3)
        else:
            pygame.draw.circle(self.screen,
                               CELL_COLOR_1,
                               (xy[0] * CELL_SIZE + CELL_SIZE // 2,
                                xy[1] * CELL_SIZE + CELL_SIZE // 2),
                               CELL_SIZE // 2 - 3)

    def draw_map(self):
        self.screen.fill((0, 0, 0))
        for i in range(self.x + 1):
            pygame.draw.line(self.screen, (255, 255, 255),
                             (0, i * CELL_SIZE),
                             (DIMENSIONS[0], i * CELL_SIZE), 3)
            pygame.draw.line(self.screen, (255, 255, 255),
                             (0, i * CELL_SIZE - 1),
                             (DIMENSIONS[0], i * CELL_SIZE - 1), 3)
        for i in range(self.y + 1):
            pygame.draw.line(self.screen, (255, 255, 255),
                             (i * CELL_SIZE, 0),
                             (i * CELL_SIZE, DIMENSIONS[1]), 3)
            pygame.draw.line(self.screen, (255, 255, 255),
                             (i * CELL_SIZE - 1, 0),
                             (i * CELL_SIZE - 1, DIMENSIONS[1]), 3)
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                self.draw_cell([i, j])
