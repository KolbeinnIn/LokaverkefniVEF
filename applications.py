#Kolbeinn Ingólfsson
#Verkefni 4 - VEFII
#Main applicationið

from MVC import app
app.config.update(dict(
    SECRET_KEY="vo mega super secret lykill.",
))

if __name__ == '__main__':
    app.run(debug=True)
