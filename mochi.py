import time
import adafruit_display_text.label
import board
import displayio
import framebufferio
import rgbmatrix
import terminalio

# Delete previous display
displayio.release_displays()
matrix = rgbmatrix.RGBMatrix(
	width=64, bit_depth=4,
	rgb_pins=[
		board.MTX_R1,
		board.MTX_G1,
		board.MTX_B1,
		board.MTX_R2,
		board.MTX_G2,
		board.MTX_B2
	],
	addr_pins=[
		board.MTX_ADDRA,
		board.MTX_ADDRB,
		board.MTX_ADDRC,
		board.MTX_ADDRD
	],
	clock_pin=board.MTX_CLK,
	latch_pin=board.MTX_LAT,
	output_enable_pin=board.MTX_OE
)
display = framebufferio.FramebufferDisplay(matrix, auto_refresh=True)

def addLabel(arr, clr, txt):
	arr.append(adafruit_display_text.label.Label(
		terminalio.FONT,
		color=clr,
		text=txt)
	)
blank = adafruit_display_text.label.Label(
	terminalio.FONT,
	color=0x000000,
	text="Blank"
)
puzzlePieces = []
addLabel(puzzlePieces, 0x001100, "M____")
addLabel(puzzlePieces, 0x000011, "__C__")
addLabel(puzzlePieces, 0x110000, "_O___")
addLabel(puzzlePieces, 0x110011, "____I")
addLabel(puzzlePieces, 0x001111, "___H_")

blank.x = 18
blank.y = 12
for i in puzzlePieces:
	i.x = 18
	i.y = 12

currentPiece = 0
displayBlank = True

while True:
	if displayBlank == True:
		displayBlank = False
	else:
		displayBlank = True
	if currentPiece == len(puzzlePieces):
		currentPiece = 0
	if displayBlank == False:
		display.show(puzzlePieces[currentPiece])
		currentPiece = currentPiece + 1
		print(currentPiece)
	else:
		display.show(blank)
	time.sleep(2)
