class Login:
    def __init__(self, correct_username, correct_password):
        self.correct_username = correct_username
        self.correct_password = correct_password

    def validate_login(self, username, password):
        if username == self.correct_username and password == self.correct_password:
            return "success"
        else:
            return "failure"
