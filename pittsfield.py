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
# Code is CANULEVER
puzzlePieces = []
addLabel(puzzlePieces, 0x001100, "C________")
addLabel(puzzlePieces, 0x110000, "___U_____")
addLabel(puzzlePieces, 0x000011, "_A_______")
addLabel(puzzlePieces, 0x111100, "__N______")
addLabel(puzzlePieces, 0x001111, "_____E___")
addLabel(puzzlePieces, 0x110011, "______V__")
addLabel(puzzlePieces, 0x110101, "________R")
addLabel(puzzlePieces, 0x011101, "_______E_")
addLabel(puzzlePieces, 0x010111, "____L____")

blank.x = 18
blank.y = 12
for i in puzzlePieces:
	i.x = 5
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
