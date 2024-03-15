from ovos_workshop.skills import OVOSSkill
from ovos_workshop.decorators import intent_handler


class CharmingAnswers(OVOSSkill):

    @intent_handler('answers.stupid.intent')
    def handle_answers_stupid(self, message):
        self.speak_dialog('answers.stupid')

    @intent_handler('who.thebest.intent')
    def handle_answers_thebest(self, message):
        self.speak_dialog('who.thebest')
