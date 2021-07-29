from PIL import Image
n=m=1000
img = Image.new('RGB', (n, m), (255, 255, 255))
img.save("empty_map.png", "PNG")
