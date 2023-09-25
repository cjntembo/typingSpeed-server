# import pygame 
# from pygame.locals import *
# import sys
# import time
# import random
# import pyjokes

# class Game:
    
#     def __init__(self):
#         self.w = 750
#         self.h = 500
#         self.rest = True
#         self.active = False
#         self.input_text = ''
#         self.word = ''
#         self.time_start = 0
#         self.total_time = 0
#         self.accuracy = "0%"        
#         self.results = 'Time:0 Accuracy:0 WPM:0'
#         self.wpm = 0
#         self.end = False
#         self.HEAD_C = (255,213,102)
#         self.TEXT_C = (240,240,240)
#         self.RESULT_C = (255,70,70)
        
#         pygame.init()
#         self.open_image = pygame.image.load('images.background.jpg')
#         self.open_image = pygame.transform.scale(scale(self.bg, (750,500)))
        
#         self.screen = pygame.display.set_mode((self.w/ self.h))
#         pygame.display.set_cation('TypingSpeed')
        
#     def draw_text(self, screen, msg, y, fsize, color):
#         font = pygame.font.Font(None, fsize)
#         text = font.render(msg, 1, color)
#         text_rect = text.get_rect(center=(self.w/2, y))
#         screen.blit(text, text_rect)
#         pygame.display.update()
        
#     def get_sentence(self):
#         sentence = pyjokes.get_jokes()
        
#         return sentence
    
#     def show_results(self, screen):
#         if(not self.end):
#             #Calculate time
#             self.total_time = time.time() - self.time_start
            
#             #Calculate Accuracy
#             count = 0
#             for i,c in enumerate(self.word):
#                 try:
#                     if self.input_text[i] == c:
#                         count += 1
                        
#                 except:
#                     pass
#             self.accuracy = count/len(self.word)*100
            
#             #Calculate wpm
#             self.wpm = len(self.input_text) * 60 / (5*self.total_time)
#             self.end = True
#             print(self.total_time)
            
#             self.results = "Time"+str(round(self.total_time)) + "secs Accuracy:" + str(round(self)) + "%" + ' wpm: ' + str(round(self.wpm))
            
#             #Draw Icon Image
#             self.time_img = pygame.image.load('images/icon.png')
#             self.time_img = pygame.transform.scale(self.time_img, (150, 150))
            
#             #screen.blit
#             screen.blit(self.time_img, (self.w/2-75, self.h-140))
#             self.draw_text(screen, "Reset", self.h - 70, 26, (100, 100, 100))
            
#             print(self.results)
#             pygame.display.update()
            
#     def run(self):
#         self.reset_game()

#         self.running = True
#         while (self.running):
#             clock = pygame.time.Clock()
#             self.screen.fill((0, 0, 0), (50, 250, 650, 50))
#             pygame.draw.rect(self.screen, self.HEAD_C, (50, 250, 650, 50), 2)

#             # update the text of the user
#             self.draw_text(self.screen, self.input_text,
#                            274, 26, (250, 250, 250))
#             pygame.display.update()

#             for event in pygame.event.get():
#                 if event.type == QUIT:
#                     self.running = False
#                     sys.exit()
#                 elif event.type == pygame.MOUSEBUTTONUP:
#                     x, y = pygame.mouse.get_pos()

#                     # Position of the input box
#                     if (x >= 50 and x <= 650 and y >= 250 and y <= 300):
#                         self.active = True
#                         self.input_text = ''
#                         self.time_start = time.time()

#                     # Position of Reset box
#                     if (x >= 310 and X <= 510 and y >= 390 and self.end):
#                         self.reset_game()
#                         x, y = pygame.mouse.get_pos()
#                     elif event.type == pygame.KEYDOWN:
#                           if self.active and not self.end:
#                                if event.key == pygame.K_RETURN:
#                                     print(self.input_text)
#                                     self.show_results(self.screen)
#                                     print(self.results)
#                                     self.draw_text(
#                                         self.screen, self.results, 350, 28, self.RESULT_C)
#                                     self.end = True

#                     elif even.key == pygame.K_BACKSPACE:
#                                     self.input_text = self.input_text[:-1]
#                     else:
#                                     try:
#                                         self.input_text += event.unicode
#                                     except:
#                                         pass
#                 pygame.display.update()
#             clock.tick(60)
            
#     def reset_game(self):
#         self.screen.blit(self.open_img, (0, 0))
#         pygame.display_update()
#         time.sleep(1)
        
#         self.reset = False
#         self.end = False
        
#         self.input_text = ''
#         self.word = ''
#         self.time_start = 0
#         self.total_time = 0
#         self.wpm = 0
        
#         #Get Random sentence
#         self.word = self.get_sentence()
#         if(not self.word): self.reset_game()
        
#         #Drawing Heading
#         self.screen.fill((0, 0, 0))
#         self.screen.blit(self.bg, (0, 0))
#         msg = "TypingSpeed Test"
#         self.draw_text(self.screen, msg, 60, 60, self.HEAD_C)
        
#         #Draw the rectangle for input box
#         pygame.draw.rect(self.screen, (250, 192, 25), (50, 250, 650, 50), 2)
        
#         #Draw the sentence string
#         self.draw_text(self.screen, self.word, 200, 28, self.TEXT_C)
        
#         pygame.display.update()
        
# Game().run()

import pygame
import random
import time

# Initialize pygame
pygame.init()

# Set up display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Typing Speed Test")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Fonts
font = pygame.font.Font(None, 36)
input_font = pygame.font.Font(None, 48)

# Generate random text
def get_random_text():
    text_list = [
        "The quick brown fox jumps over the lazy dog.",
        "Python is a powerful and versatile programming language.",
        "Coding is fun and creative!",
        "Practice makes perfect."
    ]
    return random.choice(text_list)

# Display text
def display_text(text):
    screen.fill(WHITE)
    text_surface = font.render(text, True, BLACK)
    text_rect = text_surface.get_rect(center=(400, 300))
    screen.blit(text_surface, text_rect)

# Main function for typing test
def typing_test():
    random_text = get_random_text()
    user_input = ""
    display_text(random_text)

    input_rect = pygame.Rect(300, 400, 200, 50)
    input_active = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    input_active = not input_active
                else:
                    input_active = False
                color = (255, 255, 255) if input_active else (200, 200, 200)
                pygame.draw.rect(screen, color, input_rect)

            if event.type == pygame.KEYDOWN:
                if input_active:
                    if event.key == pygame.K_RETURN:
                        if user_input == random_text:
                            return True
                        else:
                            return False
                    elif event.key == pygame.K_BACKSPACE:
                        user_input = user_input[:-1]
                    else:
                        user_input += event.unicode

        input_surface = input_font.render(user_input, True, BLACK)
        input_width = max(200, input_surface.get_width()+10)
        input_rect.w = input_width
        screen.blit(input_surface, (input_rect.x+5, input_rect.y+5))
        pygame.draw.rect(screen, (0, 0, 0), input_rect, 2)
        pygame.display.flip()

# Start typing test
def start_test():
    start_time = time.time()
    result = typing_test()
    end_time = time.time()

    if result:
        elapsed_time = end_time - start_time
        word_count = len(user_input.split())
        typing_speed = int(word_count / (elapsed_time / 60))
        print(f"Typing Speed: {typing_speed} words per minute")
    else:
        print("You didn't type the correct text.")

if __name__ == "__main__":
    start_test()
    pygame.quit()
