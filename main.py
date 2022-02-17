from pydub import AudioSegment

def getAudioObj(audiofile):
  original = AudioSegment.from_wav(audiofile)
  return original

# reverse a audio
def  reverseAudio(audiofile):
  original = getAudioObj(audiofile)
  reversed = original.reverse()
  reversed.export('reversed.wav')
  reversed = reversed + 15  # 15 units higher volume

# crop to 2 sec
def copAudio(audiofile, sec):
  original = getAudioObj(audiofile)
  unit = sec*1000
  first_two = original[0:unit]
  first_two.export('first_two.wav')


#merge 2 audios
def mergeAudio(a1, a2):
  original = getAudioObj(a1)
  reversed = original.reverse()
  reversed.export('reversed.wav')
  reversed = reversed + 15 
  merged = original * 2 + AudioSegment.silent(1000) + reversed
  merged.export('merged.wav')
#mergeAudio("beat.wav", "merged.wav")

# overlay 2 audios
def overlap(a1, a2):
  a1Obj = getAudioObj(a1)
  a2Obj = getAudioObj(a2)
  mixed = a1Obj.overlay(a2Obj)
  mixed.export("overlay.wav")
#overlap("beat.wav", "sax.wav")

# add low pass filter
def low_filter(audio):
  audioObj = getAudioObj(audio)
  beat_low = audioObj.low_pass_filter(2000)
  beat_low.export("lowbeat.wav")
#low_filter("beat.wav")

  
# add low pass filter and left ear only
def low_filter_left(audio):
    audioObj = getAudioObj(audio)
    beat_low = audioObj.low_pass_filter(2000)
    beat_left = beat_low.pan(-1)  # -1 for left ; 1 for right
    beat_left.export("lowbbeatleft.wav")
#low_filter_left("beat.wav")
