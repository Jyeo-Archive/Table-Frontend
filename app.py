from PIL import Image
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def main():
    im = Image.open('mario.png')
    pixels = list(im.getdata())
    width, height = im.size
    pixels = [pixels[i * width:(i + 1) * width] for i in range(height)]
    hexdata = []
    for row in pixels: # just ignore the alpha channel
        hexdata_row = []
        for pixel in row:
            rgb = list(pixel)
            r = rgb[0]; g = rgb[1]; b = rgb[2]
            hexdata_row.append('#{:02x}{:02x}{:02x}'.format(r, g, b))
        hexdata.append(hexdata_row)
    # print(hexdata)
    bgcolor = hexdata[0][0]
    return render_template('index.html', hexdata=hexdata, bgcolor=bgcolor)

if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True, port=5000)
