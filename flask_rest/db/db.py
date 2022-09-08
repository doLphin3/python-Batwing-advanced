import http


class UserDB:
    users = [{"name": "test", "email": "test@test.com", "password": "passhash"}]
    books = [{"name": "test_book", "author": "test_author"}]

    def get_all(self):
        return self.users

    def retrieve_by_email(self, email):
        for user in self.users:
            if user["email"] == email:
                return user
        return None

    def add(self, name, email, password_hash):
        user_already_exists = False
        for user in self.users:
            if user["email"] == email:
                user_already_exists = True
        if user_already_exists is False:
            new_user = {
                "name": name,
                "email": email,
                "password": password_hash
            }
            self.users.append(new_user)
            return new_user
        else:
            return "User already exists", http.HTTPStatus.CONFLICT

    def update_by_email(self, name, email, password):
        # TODO: refactor
        for user in self.users:
            if user["email"] == email:
                user["name"] = name
                user["password"] = password
                return user
        return None

    def delete_by_email(self, email):
        self.users = [user for user in self.users if user["email"] != email]
