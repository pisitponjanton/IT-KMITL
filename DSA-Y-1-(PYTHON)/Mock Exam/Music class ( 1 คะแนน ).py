"""Music class ( 1 คะแนน )"""
class Music:
    def __init__(self):
        self.name :str = None
        self.genre :str = None
        self.duration :int = None

    def show_info(self):
        return self.name+" <|> "+self.genre+" <|> "+f"{self.duration//60}.{self.duration%60:>02}"
def main():
    """main"""
    music = Music()
    music.name = input()
    music.genre = input()
    music.duration = int(input())
    print(music.show_info())
main()