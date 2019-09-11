from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def method():
    min_number = 1
    max_number = 1000
    moves = 10
    start = f"Think about number from {min_number} - {max_number} and I will try to guess it in 10 steps!"
    guess = int((max_number - min_number) / 2) + min_number
    guessing = f"I'm guessing... {guess}!"
    if request.method == "GET":
        return render_template("formularz.html", moves=moves, min_number=min_number, max_number=max_number, guessing=guessing,start=start)

    if request.method == "POST":
        moves = int(request.form["moves"])
        while moves > 0:
            min_number = int(request.form["min_number"])
            max_number = int(request.form["max_number"])

            if request.form["action"] == "too_big_number":
                guess = int((max_number - min_number) / 2) + min_number
                moves = moves - 1
                max_number = guess
                guess = int((max_number - min_number) / 2) + min_number
                guessing = f"I'm guessing... {guess}!"

                return render_template("formularz.html", moves=moves, min_number=min_number, max_number=max_number, start=start,
                                   guessing=guessing)
            if request.form["action"] == "too_small_number":
                guess = int((max_number - min_number) / 2) + min_number
                min_number = guess
                moves = int(moves) - 1
                guess = int((max_number - min_number) / 2) + min_number
                guessing = f"I'm guessing... {guess}!"
                return render_template("formularz.html", min_number=min_number, max_number=max_number, start=start,
                                   guessing=guessing, moves=moves)

            if request.form["action"] == "success":
                start = None
                guessing = "I'm the winner!"
                return render_template("formularz.html", start=start,
                                       guessing=guessing,moves=moves)

        return "Loser"
if __name__ == "__main__":
    app.run()
