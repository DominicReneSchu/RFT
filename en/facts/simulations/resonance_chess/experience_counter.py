from datetime import datetime
from collections import defaultdict

class ExperienceField:
    def __init__(self):
        # gruppenfähige Hauptstruktur: {erfahrungs_hash: {'count': int, 'last_occurrence': datetime, 'context': dict, 'type': 'positive'/'negative'}}
        self.field = defaultdict(lambda: {'count': 0, 'last_occurrence': None, 'context': {}, 'type': None})

    def register_experience(self, experience_key, context=None, experience_type='neutral'):
        now = datetime.now()
        entry = self.field[experience_key]

        entry['count'] += 1
        entry['last_occurrence'] = now
        entry['context'] = context if context else {}
        entry['type'] = experience_type

        # Resonanzregel: Bei hoher neg. Wiederholung, Strategie-Trigger auslösen
        if experience_type == 'negative' and entry['count'] > 2:
            self.trigger_solution_strategy(experience_key, entry)
        # Bei hoher pos. Wiederholung, Muster verstärken
        elif experience_type == 'positive' and entry['count'] > 2:
            self.reinforce_pattern(experience_key, entry)

    def trigger_solution_strategy(self, experience_key, entry):
        # Systemischer Lösungsimpuls: z.B. Logging, Strategiemodul, KI-Alert
        print(f"[Resonanzfeld] Negative Erfahrung '{experience_key}' wiederholt ({entry['count']}). Strategieverbesserung anstoßen.")

    def reinforce_pattern(self, experience_key, entry):
        # Erfolgssequenz verstärken: z.B. Priorisierung, Musterbank, Gruppenwirkung
        print(f"[Resonanzfeld] Positive Erfahrung '{experience_key}' wiederholt ({entry['count']}). Muster gruppenfähig verstärken.")

    def get_experience(self, experience_key):
        return self.field[experience_key]

    def summary(self):
        # Systemische Übersicht aller Erfahrungen
        for key, entry in self.field.items():
            print(f"Erfahrung: {key} | Count: {entry['count']} | Last: {entry['last_occurrence']} | Type: {entry['type']}")

# Beispielhafte Nutzung
if __name__ == "__main__":
    resonanzfeld = ExperienceField()
    # Negative Erfahrung, mehrfach
    for _ in range(3):
        resonanzfeld.register_experience("schach_matt_falle_links", {"position": "e2-e4"}, "negative")
    # Positive Erfahrung, mehrfach
    for _ in range(3):
        resonanzfeld.register_experience("sieg_durch_dame", {"position": "d1-h5"}, "positive")
    # Übersicht
    resonanzfeld.summary()