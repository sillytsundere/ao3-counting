import eel
# from datetime import datetime as dt

@eel.expose
def hello():
    print("Hello World!")

eel.init("www")
eel.start("index.html")

# while True:
#     timestamp = dt.now()
#     eel.addText("The time is now {}".format(timestamp.strftime("%I:%M:%S %p")))

#     eel.sleep(1.0)

