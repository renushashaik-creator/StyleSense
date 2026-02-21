class UserProfile:
    def __init__(self, user_id):
        self.user_id = user_id
        self.preferences = {}
        self.body_type = None

    def set_body_type(self, body_type):
        self.body_type = body_type

    def update_preferences(self, preference_key, preference_value):
        self.preferences[preference_key] = preference_value

    def get_preferences(self):
        return self.preferences

    def get_body_type(self):
        return self.body_type

    def save_preferences(self):
        # Logic to save preferences, possibly to a database or a file
        pass

    def load_preferences(self):
        # Logic to load preferences, possibly from a database or a file
        pass
