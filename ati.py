from binascii import unhexlify

#open audio file as binary
audio = open("macbook1.mp3", "rb")
image = open("pic.png", "wb")

#go to the 33rd byte of audio data, skipping metadat
#audio.seek(32)

#output static image from audio
#add PNG preamble
preamble = ['0x89', '0x50', '0x4E', '0x47', '0x0D', '0x0A', '0x1A', '0x0A']
image.write(unhexlify(''.join(format(i[2:], '>02s') for i in preamble)))

#write the rest of the byte array
data = audio.read()
dataList = list(data)
image.write(unhexlify(''.join(format(i[2:], '>02s') for i in dataList)))
#cleanup
audio.close()
image.close()
