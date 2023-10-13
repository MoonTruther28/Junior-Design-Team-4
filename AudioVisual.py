import time 

class AudioVisual:
    def display_question(self, question: str, display: bool):
        """Method to display the question.

        Args:
        question (str): The question to be displayed.
        """ 
        oldlastindex = 0
        lastindex = 0
        i = 1
        done = 0
        lines = []
        while (lastindex < len(question)-1):
            lastcompare = 16 + lastindex
            if (len(question)-1 < lastcompare):
                lastcompare = len(question)-1
                done = 1
            if (question[lastcompare] != ' '):
                lastindex = question[oldlastindex:lastcompare].rfind(" ") + oldlastindex
            else: 
                lastindex = lastcompare 
            
            if (lastcompare >= len(question)-1):
                lastindex = len(question)
            line = question[oldlastindex:lastindex] 
            oldlastindex = lastindex
            i += 1 
            print(line) 
            lines.append(line)
            if (done): 
                break
            
            j = 0
            while(display):
                if (j > 1 and j % 2 == 0):
                    time.sleep(5)
                    I2C_LCD1602.clear()
                row = j % 2
                I2C_LCD1602.show_string(lines[j], 0, row)
                j += 1
                if (j > i-1):
                    j = 0





    def display_success(self, planet: str):
        """Method to display a success message.

        Args:
        planet (str): The planet name in the success message.
        """
        # Code to display success message on LED and play correct sound
        I2C_LCD1602.show_string("Correct!", 0, 0)

    def display_failure(self, planet: str):
        """Method to display a failure message.

        Args:
        planet (str): The planet name in the failure message.
        """
        # Code to display failure message on LED
        I2C_LCD1602.show_string("Incorrect..." , 0, 0)
        I2C_LCD1602.show_string("Try again." , 0, 1)

    def display_lesson_complete(self, message: str):
        """Method to display a lesson complete message.

        Args:
        message (str): The message to be displayed.
        """

    def play_success_sound(self):
        """Method to play success sound."""
        # Code to play the specified sound
        pass

    def play_fail_sound(self):
        """Method to play fail sound."""
        # Code to play the specified sound
        pass

    def play_rotation_sound(self):
        """Method to play rotation sound."""
        # Star Wars
        music.play(music.tone_playable(392, music.beat(BeatFraction.HALF)),
            music.PlaybackMode.UNTIL_DONE)
        music.play(music.tone_playable(587, music.beat(BeatFraction.HALF)),
            music.PlaybackMode.UNTIL_DONE)
        music.play(music.tone_playable(523, music.beat(BeatFraction.QUARTER)),
            music.PlaybackMode.UNTIL_DONE)
        music.play(music.tone_playable(494, music.beat(BeatFraction.QUARTER)),
            music.PlaybackMode.UNTIL_DONE)
        music.play(music.tone_playable(440, music.beat(BeatFraction.QUARTER)),
            music.PlaybackMode.UNTIL_DONE)
        music.play(music.tone_playable(784, music.beat(BeatFraction.HALF)),
            music.PlaybackMode.UNTIL_DONE)
        music.play(music.tone_playable(587, music.beat(BeatFraction.QUARTER)),
            music.PlaybackMode.UNTIL_DONE)
        music.play(music.tone_playable(523, music.beat(BeatFraction.QUARTER)),
            music.PlaybackMode.UNTIL_DONE)
        music.play(music.tone_playable(494, music.beat(BeatFraction.QUARTER)),
            music.PlaybackMode.UNTIL_DONE)
        music.play(music.tone_playable(440, music.beat(BeatFraction.QUARTER)),
            music.PlaybackMode.UNTIL_DONE)
        music.play(music.tone_playable(784, music.beat(BeatFraction.HALF)),
            music.PlaybackMode.UNTIL_DONE)
        music.play(music.tone_playable(587, music.beat(BeatFraction.QUARTER)),
            music.PlaybackMode.UNTIL_DONE)
        music.play(music.tone_playable(523, music.beat(BeatFraction.QUARTER)),
            music.PlaybackMode.UNTIL_DONE)
        music.play(music.tone_playable(494, music.beat(BeatFraction.QUARTER)),
            music.PlaybackMode.UNTIL_DONE)
        music.play(music.tone_playable(523, music.beat(BeatFraction.QUARTER)),
            music.PlaybackMode.UNTIL_DONE)
        music.play(music.tone_playable(440, music.beat(BeatFraction.HALF)),
            music.PlaybackMode.UNTIL_DONE)
        # Code to play the specified sound
        pass

    def stop_rotation_sound(self):
        """Method to stop rotation sound."""
        # Code to stop the specified sound
        pass

    def play_lesson_complete_sound(self):
        """Method to play lesson complete sound."""
        # Code to play the specified sound
        pass

