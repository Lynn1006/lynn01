from adafruit_circuitplayground.express import cpx
import adafruit_fancyled.adafruit_fancyled as fancy

cpx.pixels.auto_write = False  # Update only when we say
cpx.pixels.brightness = 0.25   # make less blinding

palette = [fancy.CRGB(251,126,253),  # pink
           fancy.CRGB(184,22,180),    # purple
           fancy.CRGB(227,37,107),      # violet red
           fancy.CRGB(0,0,0)]          # Black


offset = 0  # Position offset into palette to make it "spin"

while True:
    for i in range(10):
        color = fancy.palette_lookup(palette, offset + i / 9)
        cpx.pixels[i] = color.pack()
    cpx.pixels.show()

    offset += 0.033  # Bigger number = faster spin