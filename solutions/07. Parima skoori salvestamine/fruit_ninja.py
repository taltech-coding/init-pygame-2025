# TODO: Write the current self.highscore to the file "highscore.txt".
#       If you get an error, then make sure you convert the high score
#       to str before writing it to the file.
with open("highscore.txt", "w") as file:
    file.write(str(self.highscore))
