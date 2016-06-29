import json
from sys import argv
if len(argv) < 3:
    print("usage: python build.py <json infile> <html outfile>")
    exit()
try:
    jsonfile = open(argv[1])
    data = json.load(jsonfile)
except IOError:
    print("No such file")
    exit()
except ValueError:
    print("invalid JSON")
    exit()
out = ""
template = open(data['template']["file"],"r").read();
for index,item in enumerate(data['items']):
    vals = data['items'][index]
    if index%2==0:
        out += data["template"]["start"]
        vals["left_right"] = data["template"]["left"]
        out += template.format(**vals)
        if index==len(data['items']) - 1:
            out += data["template"]["end"]
    else:
        vals["left_right"] = data["template"]["right"]
        out += template.format(**vals)
        out += data["template"]["end"]
outline = open(data["outline"]).read()
outfile = open(argv[2],"w")
outfile.write(outline.format(frontend_projects = out))
