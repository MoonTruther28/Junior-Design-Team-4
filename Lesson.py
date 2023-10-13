from os import wait
from AudioVisual import AudioVisual
from PlanetDetection import PlanetDetection
from PlanetMotion import PlanetMotion


class Lesson:
    current_question_index = 0
    questions = [
        {"question": "Which planet is closest to sun?", "answer": "Mercury"},
        {"question": "Which planet is known as the Red Planet?", "answer": "Mars"},
        {"question": "Which planet is the largest?", "answer": "Jupiter"},
        {"question": "Which planet is the smallest?", "answer": "Saturn"},
        {"question": "Which planet is the furthest from the sun?", "answer": "Venus"}
        # TODO: ...other questions
    ]

    def __init__(self):
        self.audio_visual = AudioVisual()
        self.planet_detection = PlanetDetection()
        self.planet_motion = PlanetMotion()

    def start_lesson(self):
        """Method to start the lesson."""
        self.next_question()
        
    def next_question(self):
        """Method to proceed to the next question."""
        self.current_question_index += 1
        if self.current_question_index < len(self.questions):
            self.audio_visual.display_question(self.questions[self.current_question_index]['question'])
        else:
            self.finish_lesson()
        
    def check_response(self, planet: str):
        """Method to check the response.

        Args:
        planet (str): The planet name in the response.
        """
        correct_answer = self.questions[self.current_question_index]['answer']
        if planet == correct_answer:
            self.audio_visual.display_success(planet)
            self.audio_visual.play_success_sound()
            wait(1000)
            self.audio_visual.play_rotation_sound()
            speed = self.get_orbit_speed(planet)
            self.planet_motion.rotate_arm(speed)
        else:
            self.audio_visual.play_fail_sound()

    def get_orbit_speed(self, planet: str) -> int:
        """Method to get the orbit speed of a planet.

        Args:
        planet (str): The planet name.
        """

        orbit_speeds = {
            "Mercury": 1,
            "Venus": 0.88,
            "Earth": 1,
            "Mars": 0.52,
            # TODO: ...other planets
        }
        return orbit_speeds.get(planet, 1)

    def finish_lesson(self):
        """Method to finish the lesson."""
        self.audio_visual.display_lesson_complete("Lesson Complete!")
        self.audio_visual.play_lesson_complete_sound()
