class Instruments:
    def __init__(self, name="none", item_id=0, user="none", video_link="none"):
        self.name = name
        self.item_id = item_id
        self.user = user
        self.video_link = video_link

    def set_user(self, user_name):
        self.user = user_name

    def remove_user(self):
        self.user = "none"