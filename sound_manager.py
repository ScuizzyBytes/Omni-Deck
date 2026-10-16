import os

import pygame


class SoundManager:  

    def __init__(self, sound_folder: str = "My First Project/assets"):
        pygame.mixer.init()   

        self.sound_folder = sound_folder
        self.sounds = {}
        self.load_sounds()

    def load_sounds(self) -> None:
        if os.path.exists(self.sound_folder):
            for filename in os.listdir(self.sound_folder):
                if filename.endswith(".wav"):

                    full_path = os.path.join(self.sound_folder, filename)

                    sound_name = filename.split(".")[0]
                    self.sounds[sound_name] = pygame.mixer.Sound(full_path)

    def play(self, sound_name: str) -> None:
        if sound_name in self.sounds:
            self.sounds[sound_name].play()
        else:
            print(f"Звук '{sound_name}' не найден в памяти!")
