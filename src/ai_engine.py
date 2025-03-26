import logging

class AIDiagnosticEngine:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.conversation_history = []
        self.question_count = 0

    def process_input(self, user_input, lang="en"):
        """Process user input and generate a response."""
        self.conversation_history.append({"role": "user", "content": user_input})
        self.logger.debug(f"Processing input: {user_input}")

        # Simulated diagnostic logic (replace with OpenAI API in production)
        if self.question_count < 3:
            response = self._ask_follow_up(lang)
        else:
            response = self._provide_advice(lang)

        self.conversation_history.append({"role": "assistant", "content": response})
        return response

    def _ask_follow_up(self, lang):
        """Generate follow-up questions."""
        questions = {
            "en": [
                "How long have you been experiencing this?",
                "Can you describe the intensity or type of discomfort?",
                "Have you noticed any other symptoms?"
            ],
            "zh": [
                "您这种情况持续多久了？",
                "您能描述一下不适的强度或类型吗？",
                "您有沒有注意到其他症状？"
            ]
        }
        question = questions[lang][self.question_count]
        self.question_count += 1
        return question

    def _provide_advice(self, lang):
        """Provide advice after sufficient questions."""
        advice = {
            "en": "Try resting and staying hydrated. If symptoms persist, consider consulting a local clinic. What city are you in?",
            "zh": "尝试休息并保持水分。如果症状持续，请考虑咨询当地诊所。您在哪个城市？"
        }
        return advice[lang]
