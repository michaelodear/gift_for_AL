#!/usr/bin/env python3
"""
generate_clips.py - build the Act 3 objection.lol .objection files OFFLINE.
Usage:  python3 generate_clips.py --name "Anthea Lee"
Then in objection.lol Maker: Project -> Load each .objection, Export MP4.
Needs poses.json in the same folder, and: pip install objectionpy

Music rides on inline [#bgm<id>] tags in frame text (no network, nothing to crash).
Tracks used: Trial=2, Cornered=4, Crossexamining=13, Congratulations=16, Truth2001=17.

Clips (DRAFT - assembled Act 3):
  clip1_opening    Judge/Edgeworth/Phoenix  - session -> seven-victim charge -> HOLD IT -> recess
  clip2_objection  Phoenix/Edgeworth        - the forged-trace OBJECTION
  reveal1a_who     Phoenix                  - it's a frame; the three suspects
  reveal1b_standin Phoenix/Edgeworth        - only the joke suspect aligns; the panic story
  reveal2_prod     Phoenix/Judge/Edgeworth  - confession; built-for-her; the roll-call; the Buyer
  clip4_verdict    Judge/Polly              - NOT GUILTY + Gidget (Polly) cameo
"""
import argparse, json, base64

from objectionpy import assets
# offline stubs so bg/char lookups don't hit the network; music uses raw [#bgm] tags, never assets.Music
assets.Background._requestData = classmethod(lambda cls, i: (True, {"name": f"bg{i}", "url": "", "deskUrl": "", "isWide": False}))
assets.Character._requestData  = classmethod(lambda cls, i: (True, {"name": f"char{i}"}))
from objectionpy.objection import Scene
from objectionpy.frames import Frame, FrameCharacter
from objectionpy.assets import Character, Background

POSES = json.load(open("poses.json"))
CHAR  = {n: Character(d["id"]) for n, d in POSES.items()}

BG = {"defense": 189, "prosecution": 194, "judge": 192, "witness": 197}
HOLDIT, OBJECTION, TAKETHAT = 2, 1, 3

J, E, P, PY = "The Judge", "Miles Edgeworth", "Phoenix Wright", "Polly"
def bgm(i): return f"[#bgm{i}]"

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
        F(J, "Stand",          bgm(2) + f"Court is now in session for the trial of {name}. On all seven counts.", "judge"),
        F(E, "Confident Smirk", "The prosecution is ready, Your Honour. Frankly, over-ready.", "prosecution"),
        F(E, "Point",           "Seven victims. Seven countries. A signature so exact it reads like a calling card \u2014 each one killed by the very food that shares the name of the place they died.", "prosecution"),
        F(E, "Stand",           "A mob fixer crushed under a runaway cheese wheel on a hill road in Edam. A spacefaring billionaire face-down in a brine barrel in Kalamata. A drinks-startup \u201cdisruptor\u201d poured into the floor of his own launch party in Tequila. A crypto founder buried to the collar in beans in Lima.", "prosecution"),
        F(E, "Confident Smirk", "The world did not mourn them. A mobster, a huckster, a billionaire who wanted off the planet \u2014 no great loss, the papers agreed.", "prosecution"),
        F(E, "Desk Slam",       "But no loss is not no crime. Seven murders remain seven murders.", "prosecution"),
        F(E, "Point",           "For two years this killer left nothing. No print, no trace. Until Sydney. The seventh \u2014 a star auctioneer, shucked on the harbour rocks like the morning's catch. The signature, intact.", "prosecution"),
        F(E, "Stand",           "But this time they were careless. Beside the body, something that does not fit the pattern at all: a Chinese-noodle takeaway container. And in the file from that scene \u2014 a single, flawless DNA profile.", "prosecution"),
        F(E, "Confident Smirk", "It belongs to the defendant. The prosecution needs one match. It has it, clean, on the record.", "prosecution"),
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
        F(P, "Point",     bgm(13) + "OBJECTION! Look at the edges of that trace.", "defense", bubble=OBJECTION),
        F(P, "Desk Slam", "A real read is a mess at both ends. This one is flawless corner to corner.", "defense"),
        F(P, "Confident", "Nobody recovered this sequence. Somebody built it.", "defense"),
        F(E, "Cornered",  bgm(4) + "...You're alleging the trace is synthetic.", "prosecution"),
        F(P, "Stand",     "I'm alleging it was forged from scratch \u2014 built to read as my client, and swapped into the file for whatever was really pulled from that scene.", "defense"),
    ])

def reveal1a_who(name):
    return scene([
        F(P, "Desk Slam", bgm(13) + "If nobody recovered this profile \u2014 if somebody built it \u2014 then this stopped being a murder a while ago. It's a frame. All that's left is whose hand built it.", "defense"),
        F(P, "Read",      "So I asked my client the ugly question: who would want to watch you go down for this?", "defense"),
        F(P, "Point",     "A surgeon \u2014 or the rumour of one \u2014 who answers no email, keeps no record, and may not, on paper, exist.", "defense"),
        F(P, "Cornered",  "And seek.com. A job board. Five months a postdoc and already the worst thing in her life \u2014 worse, frankly, than the murderer, and the murderer is right there. Anyone who's had to sell themselves to a portal that never writes back has the motive.", "defense"),
        F(P, "Silly",     "And \u2014 to fill the page \u2014 her evil twin. Same face, nastier spelling. We put Xanthea Yee in the folder as a joke.", "defense"),
        F(P, "Point",     "We don't have to guess who built the fake \u2014 we have all three raw reads on file. Pull them. Lay them over the forgery. Not to convict anyone yet \u2014 just to see if a thread looks back.", "defense"),
    ])

def reveal1b_standin(name):
    return scene([
        F(P, "Point",     bgm(4) + "Three reads over the fake. The surgeon \u2014 nothing. seek.com \u2014 nothing; you can't align a profile against a thing with no soul in it. Neither built this.", "defense"),
        F(P, "Desk Slam", "But the joke suspect \u2014 the twin we filed for a laugh \u2014 comes back near-perfect. Every base but a handful.", "defense"),
        F(P, "Stand",     "Which writes the surface of it. Xanthea Yee bled at the Sydney scene, panicked, took her own profile, and swapped the handful of bases that pointed at her \u2014 sliding the result into evidence reading as someone whose name was already almost hers.", "defense"),
        F(P, "Point",     f"One letter added at the front, one changed at the end \u2014 \u201c{name}\u201d becomes \u201cXanthea Yee,\u201d and a rushed lab never looks twice. The same near-miss that dropped a Grocer's mail in my client's inbox.", "defense"),
        F(E, "Cornered",  "...A tidy story, Wright. It is not proof. A near-match to a forgery convicts no one.", "prosecution"),
        F(P, "Thinking",  "No \u2014 it doesn't. A finger pointing isn't a confession. I need her to sign it herself. And nobody scrubs their own DNA for nothing.", "defense"),
        F(P, "Read",      "So stop asking what she changed to frame my client. Ask what she was hiding. Make her trace the reference \u2014 and read it again.", "defense"),
    ])

def reveal2_prod(name):
    return scene([
        F(P, "Desk Slam", "TAKE THAT! Undo her edits, translate what's underneath, and the forger signs her own work \u2014 the same vanity that named every kill after the dish it was served on.", "defense", bubble=TAKETHAT),
        F(P, "Point",     "MWAHAHAHA. IT'S-A ME. I'M THE IMPASTA.", "defense"),
        F(P, "Confident", "An impostor. A pasta. Take your pick \u2014 either way it's a confession, and not in my client's hand.", "defense"),
        F(P, "Stand",     "But read it again. It doesn't only say who. It says when. You don't forge a record that reads perfectly as my client by snatching a passing name in a panic \u2014 you have to be holding her profile before you start. This was built. In advance. For her.", "defense"),
        F(P, "Desk Slam", bgm(17) + "This was never an accident.", "defense"),
        F(P, "Point",     "A killer who left nothing for two years and seven bodies \u2014 no print, no trace \u2014 suddenly leaves a takeaway tub that \u201cdoesn't fit the pattern,\u201d carrying one flawless profile. Careless is a smudge. That is a signature, laid down on purpose.", "defense"),
        F(P, "Point",     "An email slips to my client's address. A package is misaddressed to the same door. A shopping list surfaces that no careful killer would ever carry \u2014 every city they'd already struck, spelled out to be found.", "defense"),
        F(P, "Desk Slam", "One is an accident. Four is a script. Someone wrote her a part and walked her onto every mark \u2014 straight into an Interpol evidence locker she was handed the key to\u2014", "defense"),
        F(P, "Damage",    "\u2014which I did not. mean. to say. aloud.", "defense"),
        F(J, "Surprised", "Mr Wright. Did your client break into an Interpol facility?", "judge"),
        F(P, "Cornered",  "The door was \u2014 I'm reliably told \u2014 ajar. Barely a facility. Frankly barely a door. And it was never Interpol's \u2014 it was theirs, dressed up as Interpol and logged as a break-in to make her look like precisely what they needed. Moving on\u2014", "defense"),
        F(P, "Stand",     "Because Interpol was never close. One tip in Sydney, and nothing else. The live case file my client chased was fed to her \u2014 a fabricated trail, \u201cRome\u201d painted large to keep real eyes looking the wrong way, and a quiet word to make sure the law was standing on the platform at Fuji the moment she stepped off.", "defense"),
        F(P, "Point",     "You don't fake a genome, forge a case file, and stage a lure across three continents on a whim. Xanthea Yee only filled the order. Someone with a state at their back wrote it \u2014 call them the Buyer.", "defense"),
        F(P, "Confident", "Why my client? He never says. People like the Buyer don't sign that part. She was simply the name the whole thing was built around \u2014 walked to each mark, on cue, and left holding the check.", "defense"),
        F(E, "Damage",    "...A record built from nothing. A forger too pleased with herself to keep quiet. And a defendant who was chosen.", "prosecution"),
        F(E, "Bow",       "The prosecution has no interest in convicting a name someone else selected. Your Honour \u2014 the state withdraws its match.", "prosecution"),
    ])

def clip4_verdict(name):
    return scene([
        F(J, "Stand",     "With its sole piece of evidence withdrawn, this court finds the defendant...", "judge"),
        F(J, "Positive",  bgm(16) + "NOT GUILTY.", "judge"),
        F(J, "Headshake", "...and someone notify Interpol. It appears they're hunting an impasta.", "judge"),
        F(J, "Stand",     "The defence wishes to call... one final witness. Gidget.", "judge"),
        F(PY, "Stand",    "TWEET TWEET \u2014 IT'S-A ME \u2014 IMPASTAAA \u2014 TWEET", "witness"),
        F(J, "Surprised", "...The court thanks Gidget for her testimony. And her service.", "judge"),
    ])

CLIPS = {
    "clip1_opening":    clip1_opening,
    "clip2_objection":  clip2_objection,
    "reveal1a_who":     reveal1a_who,
    "reveal1b_standin": reveal1b_standin,
    "reveal2_prod":     reveal2_prod,
    "clip4_verdict":    clip4_verdict,
}

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--name", default="the defendant")
    ap.add_argument("--outdir", default=".")
    a = ap.parse_args()
    for fname, fn in CLIPS.items():
        s = fn(a.name)
        b64 = Scene.makeObjectionFile(s.compile())
        path = f"{a.outdir}/{fname}.objection"
        open(path, "w").write(b64)
        d = json.loads(base64.b64decode(b64))
        frames = d["groups"][0]["frames"]
        print(f"\n=== {fname}.objection  ({len(frames)} frames) ===")
        for f in frames:
            tag = "[#bgm]" if "[#bgm" in f["text"] else "      "
            print(f"  char={f['characterId']!s:>4} pose={f['poseId']:>4} bub={f['bubbleType']} bg={f['backgroundId']} {tag} | {f['text'][:44]}")
    print("\nAll clips written.")
