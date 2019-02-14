#!/Users/evamy/bot/bin/python
# ################################################################################################
#       
#         Uses speech recognition module to identify what the user is commanding via
#         voice commands.
# 
# ################################################################################################
# ################################################################################################
# 
#         @version 0: Taking voice input using google speech recognizer
# 
#         @author: Antriksh Agarwal
# 
# ################################################################################################

from . import sr, r
from server.respond import getResponse


while(1):
    with sr.Microphone() as source:
        # audio = r.listen(source)

        # use the microphone as source for input. Here, we also specify
        # which device ID to specifically look for incase the microphone
        # is not working, an error will pop up saying "device_id undefined"
        # with sr.Microphone(device_index=device_id, sample_rate=sample_rate, chunk_size=chunk_size) as source:
        # wait for a second to let the recognizer adjust the
        # energy threshold based on the surrounding noise level
        r.adjust_for_ambient_noise(source)
        print("Listening ...")
        # listens for the user's input
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio)
            print("you said: " + text)
            # print Response().reply(text)
            try:
                print(getResponse(text))
            except Exception as e:
                print("Exception")
                print(e)
                continue

        # error occurs when google could not understand what was said

        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")

        except sr.RequestError as e:
            print("""Could not request results from Google
                  Speech Recognition service
                  {0}""".format(e))
