def Light():
    # creates light background
    app.bg = '#bcf7e9'
    windowL.bg = '#bcf7e9'
    windowS.bg = '#bcf7e9'
    windowDFree.bg = '#bcf7e9'
    windowDPaid.bg = '#bcf7e9'
    windowVideo.bg = '#bcf7e9'
    windowTips = '#bcf7e9'
#
#
def Dark():
    # creates dark background for accessibility
    app.bg = '#5c5655'
    windowL.bg = '#5c5655'
    windowS.bg = '#5c5655'
    windowDFree.bg = '#5c5655'
    windowDPaid.bg = '#5c5655'
    windowVideo.bg = '#5c5655'
    windowTips = '#5c5655'
#
#
LightButton = PushButton(app, text="Press this button for light mode", command = Light)
LightButton = PushButton(app, text="Press this button for dark mode", command = Dark)