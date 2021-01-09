import pyttsx3
speaker=pyttsx3.init()
speaker.setProperty('rate', 100)
speaker.save_to_file('hello we are on a interstellar mission to save human kind from its existenc by spreading humankind  on space . be aware of astroids and blackholes ', 'test.mp3')
speaker.runAndWait()


