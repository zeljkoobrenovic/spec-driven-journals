import io, json, os, sys, concurrent.futures as cf
sys.path.insert(0, "/Users/zeljkoobrenovic/PycharmProjects/spec-driven-journals/_wiring")
from generate_icons import call_gemini_image
from PIL import Image
OUT = sys.argv.pop(1) if len(sys.argv) > 1 and os.path.isdir(sys.argv[1]) else os.path.dirname(os.path.abspath(__file__)) + "/out"
M = json.load(open(os.path.dirname(os.path.abspath(__file__)) + "/icon_motifs.json"))
only = sys.argv[1:] or list(M)
def prompt(m):
    return (f"A simple app-style icon of {m}. One single object only, centered, filling about 80% of the square. "
            "Bold black line art with very thick uniform strokes and rounded ends, readable at 64 pixels: at most four or five shapes, "
            "no small details, no thin lines, no hatching, no background scene. Pure white background, black only, no gray, no color, "
            "no shading, no text, no letters, no numbers, no border, no frame, no circle around the object.")
def run(k):
    p = prompt(M[k]).replace("no text, no letters, ", "no text, ") if k == "glossary" else prompt(M[k])
    data = call_gemini_image(os.environ["GEMINI_API_KEY"], p)
    im = Image.open(io.BytesIO(data)).convert("RGB")
    s = min(im.size); im = im.crop(((im.width-s)//2, (im.height-s)//2, (im.width+s)//2, (im.height+s)//2)).resize((512, 512), Image.LANCZOS)
    im.save(f"{OUT}/{k}.png"); return k
with cf.ThreadPoolExecutor(6) as ex:
    for f in cf.as_completed([ex.submit(run, k) for k in only]):
        try: print("ok", f.result())
        except Exception as e: print("ERR", e)
