#!/usr/bin/env python3
"""
generate_clips.py — build objection.lol .objection files OFFLINE (no API/internet).
Usage:  python3 generate_clips.py --name "Anthea Lee"
Then in the objection.lol Maker: Project -> Load each .objection, then Export MP4.
Needs poses.json (the confirmed pose->ID map) in the same folder, and: pip install objectionpy

Builds the four Act 3 courtroom clips (DRAFT 6):
  clip1_opening    Judge/Edgeworth/Phoenix  — session -> the seven-victim charge -> HOLD IT
  clip2_objection  Phoenix/Edgeworth        — the forged-trace OBJECTION
  clip3_solution   Phoenix/Judge/Edgeworth  — the full frame, name collision, break-in blurt, confession
  clip4_verdict    Judge                    — NOT GUILTY
Long single frames auto-page in the Maker; split later if you want tighter beats.
"""
import argparse, json, base64

# --- make asset lookups resolve offline; the Maker fills real images from the IDs on load ---
from objectionpy import assets
assets.Background._requestData = classmethod(lambda cls, i: (True, {"name": f"bg{i}", "url": "", "deskUrl": "", "isWide": False}))
assets.Character._requestData  = classmethod(lambda cls, i: (True, {"name": f"char{i}"}))
from objectionpy.objection import Scene
from objectionpy.frames import Frame, FrameCharacter
from objectionpy.assets import Character, Background

POSES = json.load(open("poses.json"))
CHAR  = {n: Character(d["id"]) for n, d in POSES.items()}

BG = {"defense": 189, "prosecution": 194, "judge": 192, "witness": 197,
      "cell": 27, "airport": 4, "noodle": 12895}
HOLDIT, OBJECTION, TAKETHAT = 2, 1, 3   # objection.lol bubble types

J, E, P = "The Judge", "Miles Edgeworth", "Phoenix Wright"

def F(char, pose, text, bg, bubble=None):
    return Frame(char=FrameCharacter(CHAR[char], poseId=POSES[char]["poses"][pose]),
                 background=Background(BG[bg]), text=text, bubble=bubble)

def scene(frames):
    s = Scene()
    for f in frames:
        s.frames.append(f)
    return s

# ---------------------------------------------------------------------------
def clip1_opening(name):
    return scene([
        F(J, "Stand",          f"Court is now in session for the trial of {name}. On all seven counts.", "judge"),
        F(E, "Confident Smirk", "The prosecution is ready, Your Honour. Frankly, over-ready.", "prosecution"),
        F(E, "Point",           "Seven victims. Seven countries. And a signature so exact it reads like a calling card \u2014 each one killed by the very food that shares the name of the place they died.", "prosecution"),
        F(E, "Stand",           "A mob fixer crushed under a runaway cheese wheel on a hill road in Edam. A spacefaring billionaire face-down in a brine barrel in Kalamata. A drinks-startup \u201cdisruptor\u201d poured into the floor of his own launch party in Tequila. A crypto founder buried to the collar in beans in Lima.", "prosecution"),
        F(E, "Confident Smirk", "The world did not mourn them. A mobster, a huckster, a billionaire who wanted off the planet \u2014 no great loss, the papers agreed.", "prosecution"),
        F(E, "Desk Slam",       "But no loss is not no crime. Seven murders remain seven murders.", "prosecution"),
        F(E, "Point",           "For two years this killer left nothing. No print, no trace. Until Sydney. The seventh \u2014 a star auctioneer, shucked on the harbour rocks like the morning's catch. The signature, intact.", "prosecution"),
        F(E, "Stand",           "But this time they were careless. Beside the body they left something that does not fit the pattern: a Chinese-noodle takeaway container. And on it \u2014 one clean DNA profile.", "prosecution"),
        F(E, "Confident Smirk", "It belongs to the defendant. The prosecution needs one match. It has it.", "prosecution"),
        F(P, "Point",           "HOLD IT!", "defense", bubble=HOLDIT),
        F(P, "Desk Slam",       "That's my client you're filing under \u201calready decided.\u201d", "defense"),
        F(P, "Stand",           "Wright, for the defence.", "defense"),
        F(P, "Read",            "So let me be sure I follow the charge. Seven murders \u2014 the cheese, the brine, the beans \u2014 none of which you can place on my client.", "defense"),
        F(P, "Read",            "The one thing you can place on them is a takeaway container. Stripped down, the charge is... eating a meal.", "defense"),
        F(P, "Silly",           "A succulent Chinese meal.", "defense"),
        F(E, "Cornered",        "The murder is the charge, Wright. The meal is merely where they got careless.", "prosecution"),
        F(P, "Point",           "Then let's look at the one thing tying my client to any of it. I move to enter the raw DNA read into evidence.", "defense"),
        F(J, "Stand",           "Granted. The court will recess to examine it.", "judge"),
    ])

def clip2_objection(name):
    return scene([
        F(P, "Point",     "OBJECTION! Look at the edges of that trace.", "defense", bubble=OBJECTION),
        F(P, "Desk Slam", "A real read is a mess at both ends. This one is flawless corner to corner.", "defense"),
        F(P, "Confident", "Nobody recovered this sequence. Somebody built it.", "defense"),
        F(E, "Cornered",  "...You're alleging the trace is synthetic.", "prosecution"),
        F(P, "Stand",     "I'm alleging it was forged from scratch \u2014 to read as my client.", "defense"),
    ])

def clip3_solution(name):
    return scene([
        F(P, "Point",     "TAKE THAT! That \u201cone clean match\u201d was never recovered off the container. It was forged onto it.", "defense", bubble=TAKETHAT),
        F(P, "Stand",     "The real Grocer \u2014 Xanthea Yee, the name you just put on that board \u2014 left her own DNA in Sydney, panicked, and rebuilt the trace to read as someone else. She didn't pick my client at random. She picked the name that was already almost hers.", "defense"),
        F(P, "Read",      f"One letter added to the front. One letter changed at the end. {name} becomes Xanthea Yee. A rushed database doesn't look twice. It didn't.", "defense"),
        F(P, "Desk Slam", "So my client never stumbled into this case. They were cast in it. Handed a part in someone else's production and walked to each mark on cue.", "defense"),
        F(P, "Point",     "Cue one \u2014 a \u201cmisdirected\u201d letter. Sent, not slipped. It put the Grocer's trail in my client's hands and pointed them up it. Which is how they came to be inside an Interpol evidence locker without, strictly speaking, a key\u2014", "defense"),
        F(P, "Damage",    "\u2014which I. did not. mean to say. out loud.", "defense"),
        F(J, "Surprised", "Mr Wright. Did your client break into an Interpol facility?", "judge"),
        F(P, "Cornered",  "The facility was unmanned. The door was \u2014 I'm reliably told \u2014 ajar. That's barely a break-in. That's a firm knock. Not the crime we're here about. Moving on\u2014", "defense"),
        F(P, "Point",     "Cue two \u2014 Tokyo. The one city left unstruck on the Grocer's list, dangled as bait, so whoever was chasing the killer would be standing at the next scene when the net dropped. Cue three \u2014 the container. A signed confession, wrong name, left where it couldn't be missed.", "defense"),
        F(P, "Stand",     "You don't hack Interpol, forge a genome, and stage a lure across three continents on a whim. Someone wrote the shopping list. Someone with a state behind them \u2014 call them the Buyer. The Grocer only ever filled the order.", "defense"),
        F(P, "Confident", "As for the Grocer herself \u2014 she couldn't help the flourish. The same vanity that signed seven kills with the food of the place signed the forgery too. Undo her edits, translate what's left, and she confesses in her own hand \u2014", "defense"),
        F(P, "Desk Slam", "MWAHAHAHA. IT'S-A ME. I'M THE IMPASTA.", "defense"),
        F(P, "Point",     "An imposter. A pasta. Take your pick. Either way \u2014 not my client.", "defense"),
        F(E, "Cornered",  "...A trace built from nothing. And a forger too pleased with herself to keep quiet.", "prosecution"),
        F(E, "Bow",       "The prosecution has no interest in convicting the wrong person. Your Honour \u2014 the state withdraws its match.", "prosecution"),
    ])

def clip4_verdict(name):
    return scene([
        F(J, "Stand",     "With its sole piece of evidence withdrawn, this court finds the defendant...", "judge"),
        F(J, "Positive",  "NOT GUILTY.", "judge"),
        F(J, "Surprised", "...And someone notify Interpol. It appears they're looking for an impasta.", "judge"),
    ])

CLIPS = {
    "clip1_opening":  clip1_opening,
    "clip2_objection": clip2_objection,
    "clip3_solution":  clip3_solution,
    "clip4_verdict":   clip4_verdict,
}

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--name", default="the defendant")
    a = ap.parse_args()
    for fname, fn in CLIPS.items():
        s = fn(a.name)
        b64 = Scene.makeObjectionFile(s.compile())
        path = f"/mnt/user-data/outputs/{fname}.objection"
        open(path, "w").write(b64)
        d = json.loads(base64.b64decode(b64))
        frames = d["groups"][0]["frames"]
        print(f"\n=== {fname}.objection  ({len(frames)} frames) ===")
        for f in frames:
            print(f"  poseId={f['poseId']:>4}  bubble={f['bubbleType']}  bg={f['backgroundId']}  | {f['text'][:48]}")
    print("\nAll four clips written to /mnt/user-data/outputs/.")
