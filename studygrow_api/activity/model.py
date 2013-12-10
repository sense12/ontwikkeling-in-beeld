class Activity(object):

    found = False

    def __init__(self, title=None, estimate=None):
        self.title = title
        self.estimate = estimate

    def set_title(self, title):
        self.title = title

    def set_estemate(self, amount_of_pomodoros):
        self.estimate = amount_of_pomodoros

    def set_url(self, url):
        self.url = url

    def find(self, _id):
        self.found = True
        self.id = _id
        self.set_title('call sally simpson')
        self.set_estemate(self.id)

        return self
