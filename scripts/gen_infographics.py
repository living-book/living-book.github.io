#!/usr/bin/env python3
"""Stage 3 driver: generate START/END infographics for Laws 02-18 via Nano Banana.

Idempotent: skips images that already exist. Run from repo root:
    python3 scripts/gen_infographics.py [--only law-07-defensiveness] [--force]
"""
import argparse
import subprocess
import sys
from pathlib import Path

GENIMAGE = "/home/sanjayg4/.claude/plugins/marketplaces/ibrahim-plugins/scripts/genimage.py"
OUTDIR = Path("docs/books/laws-of-human-nature/infographics")

STYLE = (
    "Editorial magazine infographic, navy #1a2f4a and gold #c9a227 on cream #f2efe6, "
    "clean flat illustration, generous whitespace, sans-serif headers, crisp legible text."
)

# slug, num, title, directive, figure (name + dates), trap (visual metaphor), trap_labels(2),
# stakes_labels(2), arc (before, shift, after), lesson, outcome, strategies(6), warnings(4)
LAWS = [
    dict(slug="law-02-narcissism", num=2, title="The Law of Narcissism",
         directive="Transform Self-Love into Empathy",
         figure="Joseph Stalin (1878-1953)",
         trap="a man gazing into a mirror that reflects only himself while people behind him fade to grey",
         trap_labels=["Self-absorption", "Deaf to others"],
         stakes_labels=["Isolation", "Paranoia"],
         arc=("Deep narcissism", "Turn attention outward", "Radical empathy"),
         lesson="Unchecked self-love turns paranoid", outcome="Empathy builds real power",
         strategies=["Know the spectrum", "Spot deep narcissists", "Practice empathy",
                     "Mirror moods", "Read nonverbals", "Seek outside views"],
         warnings=["Conversation hogging", "Rage at criticism", "Zero curiosity", "Constant victimhood"]),
    dict(slug="law-03-role-playing", num=3, title="The Law of Role-Playing",
         directive="See Through People's Masks",
         figure="Milton Erickson (1901-1980)",
         trap="a smiling theater mask held in front of a shadowed face at a business meeting",
         trap_labels=["Polished mask", "Hidden intent"],
         stakes_labels=["Deceived", "Manipulated"],
         arc=("Face value", "Trained observation", "Reading people"),
         lesson="Bodies leak what words hide", outcome="Read cues others miss",
         strategies=["Watch first moments", "Note micro-expressions", "Hear the tone",
                     "Observe under stress", "Wear your best mask", "Manage your cues"],
         warnings=["Too-perfect charm", "Words defy body", "Forced smiles", "Inconsistent stories"]),
    dict(slug="law-04-compulsive-behavior", num=4, title="The Law of Compulsive Behavior",
         directive="Determine the Strength of People's Character",
         figure="Howard Hughes (1905-1976)",
         trap="a man repeating the same circular path, each loop deepening a groove in the ground",
         trap_labels=["Repeated pattern", "Same ending"],
         stakes_labels=["Wrong partners", "Repeat disasters"],
         arc=("Charmed by surface", "Study track record", "Judge character"),
         lesson="Patterns repeat under pressure", outcome="Character is destiny",
         strategies=["Check track record", "Watch under stress", "Ignore charm",
                     "Test with tasks", "Know your pattern", "Choose strong character"],
         warnings=["Serial failed deals", "Blames everyone", "Chaos follows them", "Charm over substance"]),
    dict(slug="law-05-covetousness", num=5, title="The Law of Covetousness",
         directive="Become an Elusive Object of Desire",
         figure="Coco Chanel (1883-1971)", portrait="an elegant flat illustration silhouette of a 1920s fashion designer with pearl necklace, no facial likeness",
         trap="a hand reaching for an object behind glass that glows brighter the further it recedes",
         trap_labels=["Grass is greener", "Wanting the absent"],
         stakes_labels=["Chronic dissatisfaction", "Chasing mirages"],
         arc=("Overexposure", "Strategic absence", "Object of desire"),
         lesson="Absence sharpens desire", outcome="Mystery became an empire",
         strategies=["Create distance", "Stay half-hidden", "Use absence",
                     "Stir imagination", "Never overexpose", "Know your own wanting"],
         warnings=["Always available", "Overexplaining", "Chasing approval", "Novelty addiction"]),
    dict(slug="law-06-shortsightedness", num=6, title="The Law of Shortsightedness",
         directive="Elevate Your Perspective",
         figure="Isaac Newton (1643-1727)",
         trap="a crowd rushing toward a golden bubble about to burst while one figure watches from a hill",
         trap_labels=["Panic reaction", "Crowd fever"],
         stakes_labels=["Ruined fortunes", "Compounding errors"],
         arc=("Reactive present", "The long view", "Strategic patience"),
         lesson="Even genius joins manias", outcome="Distance reveals consequences",
         strategies=["Zoom out first", "Delay reactions", "Track consequences",
                     "Ignore mania", "Set far goals", "Weigh second effects"],
         warnings=["Urgency addiction", "Trend chasing", "Instant reaction", "Ignoring aftermath"]),
    dict(slug="law-07-defensiveness", num=7, title="The Law of Defensiveness",
         directive="Soften People's Resistance by Confirming Their Self-Opinion",
         figure="Lyndon B. Johnson (1908-1973)",
         trap="a man pushing hard against a closed door while an open side door glows beside it",
         trap_labels=["Direct pushing", "Walls rising"],
         stakes_labels=["Resistance", "Lost allies"],
         arc=("Forcing arguments", "Confirm self-image", "Willing agreement"),
         lesson="People defend their self-image", outcome="Validation opened every door",
         strategies=["Confirm autonomy", "Affirm intelligence", "Validate goodness",
                     "Listen deeply", "Ask their advice", "Let them conclude"],
         warnings=["Winning arguments", "Correcting publicly", "Unsolicited advice", "Talking past no"]),
    dict(slug="law-08-self-sabotage", num=8, title="The Law of Self-Sabotage",
         directive="Change Your Circumstances by Changing Your Attitude",
         figure="Anton Chekhov (1860-1904)",
         trap="a man painting dark clouds onto his own window while the sky outside is clear",
         trap_labels=["Hostile lens", "Self-made ceiling"],
         stakes_labels=["Shrunken life", "Fulfilled fears"],
         arc=("Constricted attitude", "Radical acceptance", "Expansive life"),
         lesson="Attitude colors every event", outcome="Love replaced bitterness",
         strategies=["Audit your lens", "Reframe adversity", "Assume abundance",
                     "Drop grudges", "Act despite fear", "Choose expansion"],
         warnings=["Expecting betrayal", "Rehearsing failure", "Blaming fate", "Hoarding grievances"]),
    dict(slug="law-09-repression", num=9, title="The Law of Repression",
         directive="Confront Your Dark Side",
         figure="Richard Nixon (1913-1994)",
         trap="a polished public figure casting a long jagged shadow that acts on its own",
         trap_labels=["Buried impulses", "Leaking shadow"],
         stakes_labels=["Self-destruction", "Projection"],
         arc=("Denied shadow", "Face the dark side", "Integrated power"),
         lesson="The repressed returns destructively", outcome="Integration beats eruption",
         strategies=["Name your shadow", "Watch projections", "Mine dark energy",
                     "Show controlled edge", "Accept ambivalence", "Create, not repress"],
         warnings=["Too-good persona", "Sudden outbursts", "Harsh judging", "Secret behaviors"]),
    dict(slug="law-10-envy", num=10, title="The Law of Envy",
         directive="Beware the Fragile Ego",
         figure="Mary Shelley (1797-1851)",
         trap="a friend smiling while their shadow holds a raised dagger behind their back",
         trap_labels=["Masked resentment", "Poisoned praise"],
         stakes_labels=["Sabotage", "Betrayal"],
         arc=("Blind to envy", "Detect the signals", "Deflect and disarm"),
         lesson="Envy hides behind friendship", outcome="Vigilance saved her work",
         strategies=["Spot micro-signals", "Downplay success", "Deflect attention",
                     "Convert enviers", "Avoid triggering", "Own your envy"],
         warnings=["Backhanded compliments", "Joy at your setbacks", "Sudden coldness", "Copying then competing"]),
    dict(slug="law-11-grandiosity", num=11, title="The Law of Grandiosity",
         directive="Know Your Limits",
         figure="Michael Eisner (b. 1942)", portrait="a symbolic flat illustration of a confident executive silhouette in a suit at a boardroom window, city skyline beyond, no facial likeness",
         trap="a man on a pedestal built of past trophies, leaning over a cliff edge to reach a crown",
         trap_labels=["Success high", "Inflated self"],
         stakes_labels=["Overreach", "Public fall"],
         arc=("Grandiose inflation", "Realistic assessment", "Grounded ambition"),
         lesson="Success inflates until it blinds", outcome="Limits are leverage",
         strategies=["Credit luck", "Measure real skill", "Stay hands-on",
                     "Welcome critics", "Raise goals slowly", "Channel grand visions"],
         warnings=["Believing your press", "Dismissing critics", "Ever-bigger bets", "Losing details"]),
    dict(slug="law-12-gender-rigidity", num=12, title="The Law of Gender Rigidity",
         directive="Reconnect to the Masculine or Feminine Within You",
         figure="Queen Elizabeth I (1533-1603)",
         trap="a figure locked inside a rigid suit of armor shaped like a gender symbol",
         trap_labels=["Rigid role", "Half a self"],
         stakes_labels=["Blind spots", "Brittle identity"],
         arc=("Rigid gender role", "Embrace inner other", "Fluid wholeness"),
         lesson="She ruled with both energies", outcome="Wholeness outplayed rivals",
         strategies=["Find inner other", "Flex your style", "Blend firm and warm",
                     "Study the opposite", "Drop role scripts", "Use full range"],
         warnings=["Performing toughness", "Fear of softness", "One-note style", "Mocking difference"]),
    dict(slug="law-13-aimlessness", num=13, title="The Law of Aimlessness",
         directive="Advance with a Sense of Purpose",
         figure="Martin Luther King Jr. (1929-1968)",
         trap="a man drifting on a raft pulled by many small currents going nowhere",
         trap_labels=["Drifting", "Borrowed goals"],
         stakes_labels=["Wasted years", "Crowd-following"],
         arc=("Aimless drift", "Discover the calling", "Purpose-driven force"),
         lesson="Purpose found him in crisis", outcome="A calling organizes a life",
         strategies=["Mine childhood signals", "Define the calling", "Set micro-goals",
                     "Use deadlines", "Ignore side paths", "Renew in lulls"],
         warnings=["Chronic restlessness", "Serial reinvention", "Others' dreams", "Purpose by committee"]),
    dict(slug="law-14-conformity", num=14, title="The Law of Conformity",
         directive="Resist the Downward Pull of the Group",
         figure="Philip Zimbardo (b. 1933)", portrait="a symbolic flat illustration of a researcher silhouette observing figures behind glass, no facial likeness",
         trap="rows of identical grey paper figures all leaning the same direction while one bright gold figure stands upright apart",
         trap_labels=["Group trance", "Borrowed opinions"],
         stakes_labels=["Moral collapse", "Lost judgment"],
         arc=("Group trance", "Social intelligence", "Independent mind"),
         lesson="Good people follow groups down", outcome="Awareness resists the pull",
         strategies=["Notice group moods", "Keep outside friends", "Test group beliefs",
                     "Resist status games", "Speak early dissent", "Exit toxic groups"],
         warnings=["Echo chambers", "Fear of dissent", "Status obsession", "Us-versus-them talk"]),
    dict(slug="law-15-fickleness", num=15, title="The Law of Fickleness",
         directive="Make Them Want to Follow You",
         figure="George Marshall (1880-1959)",
         trap="a leader on a pedestal as the crowd beneath simultaneously cheers and saws at the legs",
         trap_labels=["Fickle crowd", "Conditional loyalty"],
         stakes_labels=["Abandonment", "Coup"],
         arc=("Demanded loyalty", "Earned authority", "Willing followers"),
         lesson="Authority is earned daily", outcome="Service made them follow",
         strategies=["Lead by example", "Deliver results", "Share credit",
                     "Stay slightly distant", "Adapt your style", "Never take loyalty for granted"],
         warnings=["Demanding respect", "Hogging credit", "Playing favorites", "Ignoring the mood"]),
    dict(slug="law-16-aggression", num=16, title="The Law of Aggression",
         directive="See the Hostility Behind the Friendly Facade",
         figure="John D. Rockefeller (1839-1937)",
         trap="a handshake where one arm casts the shadow of a coiled snake",
         trap_labels=["Friendly surface", "Hidden hostility"],
         stakes_labels=["Blindsided", "Outmaneuvered"],
         arc=("Naive trust", "Spot the aggressor", "Channeled assertion"),
         lesson="Aggression wears a smile", outcome="Assertion, not eruption",
         strategies=["Watch actions not words", "Track pressure patterns", "Set firm lines",
                     "Counter calmly", "Channel your aggression", "Never show panic"],
         warnings=["Boundary testing", "Charm then squeeze", "Sudden generosity", "Allies going quiet"]),
    dict(slug="law-17-generational-myopia", num=17, title="The Law of Generational Myopia",
         directive="Seize the Historical Moment",
         figure="Benjamin Franklin (1706-1790)",
         trap="a man reading yesterday's newspaper while a new dawn rises unnoticed behind him",
         trap_labels=["Era blindness", "Outdated maps"],
         stakes_labels=["Irrelevance", "Missed waves"],
         arc=("Generation trance", "Read the zeitgeist", "Shape the moment"),
         lesson="He read each era's spirit", outcome="Timing turned into power",
         strategies=["Name your era's spirit", "Study the young", "Question era values",
                     "Mix generations", "Spot the turning", "Act on the wave"],
         warnings=["Golden-age nostalgia", "Dismissing the young", "Era-bound tastes", "Fighting the tide"]),
    dict(slug="law-18-death-denial", num=18, title="The Law of Death Denial",
         directive="Know How to Make Use of Mortality",
         figure="William James (1842-1910)",
         trap="a man drawing curtains against a window shaped like an hourglass",
         trap_labels=["Denied mortality", "Numbed living"],
         stakes_labels=["Deferred life", "Shallow days"],
         arc=("Death denial", "Mortality awareness", "Urgent aliveness"),
         lesson="Facing death woke him up", outcome="Deadlines make life vivid",
         strategies=["Meditate on limits", "Feel the deadline", "Cut trivial time",
                     "Deepen connections", "Act on postponed dreams", "Savor the present"],
         warnings=["Living someday", "Numbing routines", "Avoiding the topic", "Time-wasting spirals"]),
]


def start_prompt(l):
    return (
        f"Infographic, three vertical editorial panels. Top banner: dark navy bar with "
        f"\"LAW {l['num']}\" in a gold box and title \"{l['title'].upper()}\" in large cream serif capitals. "
        f"LEFT panel header \"THE TRAP\": flat illustration of {l['trap']}, with two small gold label boxes: "
        f"\"{l['trap_labels'][0]}\" and \"{l['trap_labels'][1]}\". "
        f"CENTER panel header \"CASE STUDY\": {l.get('portrait', 'classical editorial portrait of ' + l['figure'])}, caption \"{l['figure']}\" beneath in gold serif. "
        f"RIGHT panel header \"STAKES\": business-setting illustration of the cost, two dark label boxes: "
        f"\"{l['stakes_labels'][0]}\" and \"{l['stakes_labels'][1]}\". "
        f"Bottom: gold label \"FORWARD CALL\" then wide navy arrow containing \"{l['directive'].upper()}\" in cream capitals. "
        + STYLE
    )


def end_prompt(l):
    s = l["strategies"]
    w = l["warnings"]
    return (
        f"Infographic dashboard. Top: dark navy header bar, gold \"LAW {l['num']}\" then "
        f"\"{l['title'].upper()} — TRANSFORMATION\" in cream serif capitals. "
        f"LEFT section \"TRANSFORMATION ARC\": three circles connected by curved arrows — navy circle \"BEFORE: {l['arc'][0]}\", "
        f"gold circle \"SHIFT: {l['arc'][1]}\", coral circle \"AFTER: {l['arc'][2]}\". "
        f"CENTER section \"CASE STUDY\" in a gold-bordered card: {l.get('portrait', 'small round portrait of ' + l['figure'].split(' (')[0])}, caption \"{l['figure'].split(' (')[0]}\", "
        f"gold tag \"LESSON\" with text \"{l['lesson']}\", gold tag \"OUTCOME\" with text \"{l['outcome']}\". "
        f"RIGHT section \"STRATEGY CARDS\": six white cards in a 2x3 grid, each a simple line icon and a short label: "
        + ", ".join(f"\"{x}\"" for x in s) + ". "
        f"BOTTOM row \"WARNING SIGNS\": four red flag icons with labels "
        + ", ".join(f"\"{x}\"" for x in w) + ". "
        + STYLE
    )


def gen(prompt, out, force):
    if out.exists() and not force:
        print(f"skip {out.name}")
        return True
    r = subprocess.run(
        [sys.executable, GENIMAGE, "--prompt", prompt, "--output", str(out),
         "--aspect-ratio", "16:9", "--resolution", "2K"],
        capture_output=True, text=True, timeout=300)
    ok = out.exists()
    print(f"{'ok  ' if ok else 'FAIL'} {out.name}" + ("" if ok else f" :: {r.stdout[-200:]} {r.stderr[-200:]}"))
    return ok


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only")
    ap.add_argument("--force", action="store_true")
    a = ap.parse_args()
    fails = []
    for l in LAWS:
        if a.only and l["slug"] != a.only:
            continue
        for kind, p in (("start", start_prompt(l)), ("end", end_prompt(l))):
            out = OUTDIR / f"{l['slug']}-{kind}.png"
            if not gen(p, out, a.force):
                fails.append(out.name)
    print(f"\ndone. failures: {fails or 'none'}")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
