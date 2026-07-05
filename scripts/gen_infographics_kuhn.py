#!/usr/bin/env python3
"""Stage 3 driver: Kuhn — Structure of Scientific Revolutions infographics.

Idempotent. Run from repo root: python3 scripts/gen_infographics_kuhn.py [--only ch-05-...] [--force]
"""
import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from gen_infographics import STYLE, gen  # shared machinery

OUTDIR = Path("docs/books/structure-of-scientific-revolutions/infographics")

# problem = LEFT visual metaphor; episode = CENTER scene (all figures deceased);
# arc/lesson/outcome/strategies/warnings feed the END dashboard.
CH = [
    dict(slug="ch-01-role-for-history", num=1, title="A Role for History",
         move="Let History Correct Your Image of Science",
         problem="a tidy brick wall of 'facts' being built ever higher while its lower rows quietly crumble",
         problem_labels=["Linear myth", "Cumulative illusion"],
         episode="a young physicist at a desk, stunned, reading an ancient Greek manuscript that glows with its own internal order",
         episode_caption="Kuhn reads Aristotle",
         stakes_labels=["Distorted judgment", "Chronological snobbery"],
         arc=("Textbook history", "Read the past on its terms", "Transformed image"),
         lesson="Discarded science was still science", outcome="History reveals how science works",
         strategies=["Read primary sources", "Suspect origin stories", "Judge in context",
                     "Study defeated views", "Question inevitability", "Map real debates"],
         warnings=["Whig history", "Present-day yardsticks", "Hero narratives", "Inevitable-progress talk"]),
    dict(slug="ch-02-route-to-normal-science", num=2, title="The Route to Normal Science",
         move="Acquire a Paradigm, End the Foundation Wars",
         problem="a crowd of scholars shouting across a round table, each holding a different blueprint of the same building",
         problem_labels=["Competing schools", "No accumulation"],
         episode="Benjamin Franklin (1706-1790) demonstrating the Leyden jar to unify rival electricians",
         episode_caption="Franklin unifies electricity",
         stakes_labels=["Wasted energy", "Endless relitigating"],
         arc=("School warfare", "First shared exemplar", "Cumulative work"),
         lesson="Paradigms end foundational debate", outcome="Consolidation unleashes depth",
         strategies=["Find the exemplar", "Stop refounding", "Specialize the audience",
                     "Build on wins", "Adopt shared tools", "Let details rule"],
         warnings=["Every meeting restarts", "Foundations relitigated", "No shared canon", "Audience of everyone"]),
    dict(slug="ch-03-nature-of-normal-science", num=3, title="The Nature of Normal Science",
         move="Honor the Mop-Up Work",
         problem="a gleaming promise-shaped outline being carefully filled in, tile by tiny tile, by focused workers",
         problem_labels=["Unfinished promise", "Endless detail"],
         episode="Pierre-Simon Laplace (1749-1827) at a desk of celestial calculations completing Newton's system",
         episode_caption="Laplace completes Newton",
         stakes_labels=["No precision", "Shallow fields"],
         arc=("Grand promise", "Focused articulation", "Deep precision"),
         lesson="Restriction of vision powers progress", outcome="Precision the paradigm promised",
         strategies=["Extend, then question", "Prize precision", "Fund maintenance",
                     "Deepen the match", "Resist novelty theater", "Finish the promise"],
         warnings=["Disruption demanded daily", "Maintenance despised", "Precision unfunded", "Framework churn"]),
    dict(slug="ch-04-normal-science-as-puzzle-solving", num=4, title="Puzzle-Solving",
         move="Know When the Theory Tests You",
         problem="a scientist assembling an intricate jigsaw whose box lid guarantees the picture exists",
         problem_labels=["Assured solution", "Fixed rules"],
         episode="Henry Cavendish (1731-1810) with a delicate torsion balance measuring the gravitational constant",
         episode_caption="Cavendish weighs the Earth",
         stakes_labels=["Blamed practitioner", "Misread failures"],
         arc=("Testing theories", "Puzzle discipline", "Craft mastery"),
         lesson="Failure blames the solver first", outcome="Skill grows inside constraints",
         strategies=["Label puzzle vs question", "Trust the frame", "Blame calibration",
                     "State hidden rules", "Escalate skill first", "Save doubts for crisis"],
         warnings=["Open questions disguised", "Framework blamed early", "Rules unstated", "Every task existential"]),
    dict(slug="ch-05-priority-of-paradigms", num=5, title="The Priority of Paradigms",
         move="Transmit Craft Through Exemplars",
         problem="a rulebook dissolving into mist while a row of worked examples stands solid as stone",
         problem_labels=["Rules run out", "Examples endure"],
         episode="students at wooden desks solving inclined-plane problems until force itself becomes visible to them",
         episode_caption="Learning physics by exemplar",
         stakes_labels=["Fragmented practice", "Failed onboarding"],
         arc=("Rules-first teaching", "Shared exemplars", "Trained judgment"),
         lesson="Examples run deeper than rules", outcome="Similarity-perception is the knowledge",
         strategies=["Curate gold examples", "Teach by cases", "Test on cases",
                     "Watch case divergence", "Write model solutions", "Apprentice, then codify"],
         warnings=["Definition fights", "Case divergence", "Rulebook onboarding", "Unstatable expertise ignored"]),
    dict(slug="ch-06-anomaly-and-discovery", num=6, title="Anomaly and Discovery",
         move="Instrument Your Expectations",
         problem="a lab wall of precise gauges, one needle trembling outside its marked band while everyone walks past",
         problem_labels=["Violated expectation", "Assimilated to noise"],
         episode="Wilhelm Roentgen (1845-1923) in a darkened lab staring at a screen glowing where nothing should",
         episode_caption="Roentgen chases the glow",
         stakes_labels=["Missed discoveries", "Noise blindness"],
         arc=("Vague expectations", "Precise prediction", "Anomaly visible"),
         lesson="Only sharp expectations get surprised", outcome="Discovery is the follow-up",
         strategies=["Predict precisely", "Budget anomaly time", "Chase the glow",
                     "Resist quick fixes", "Track violations", "Recategorize slowly"],
         warnings=["Everything as noise", "No stated expectations", "Anomalies patched fast", "No chase license"]),
    dict(slug="ch-07-crisis-and-new-theories", num=7, title="Crisis and New Theories",
         move="Map Novelty to the Public Failure",
         problem="an ancient clockwork machine covered in patches, each patch sprouting patches of its own",
         problem_labels=["Chronic anomaly", "Patch upon patch"],
         episode="Nicolaus Copernicus (1473-1543) surrounded by tangled epicycle charts he called a monster",
         episode_caption="Copernicus names the monster",
         stakes_labels=["Stalled field", "Eroded confidence"],
         arc=("Private doubts", "Public breakdown", "Licensed speculation"),
         lesson="Crisis precedes every new theory", outcome="Failure sets novelty's timing",
         strategies=["Find the known failure", "Pitch to the crisis", "Read parallel inventions",
                     "Loosen rules in storms", "Count the patches", "Time the retooling"],
         warnings=["Patches as system", "Failure undiscussable", "Novelty without crisis", "Simultaneous rivals ignored"]),
    dict(slug="ch-08-response-to-crisis", num=8, title="The Response to Crisis",
         move="Replace, Don't Just Reject",
         problem="a man about to leap from a cracking bridge with no other bridge in sight",
         problem_labels=["Rejection alone", "Nowhere to land"],
         episode="Albert Einstein (1879-1955) at a cluttered desk, the ground of classical physics dissolving beneath it",
         episode_caption="Einstein retools physics",
         stakes_labels=["Paralysis", "Lost science"],
         arc=("Anomaly panic", "Build the rival", "Comparative choice"),
         lesson="No exit without an alternative", outcome="Comparison, not complaint, decides",
         strategies=["Build before attacking", "Compare, then choose", "Keep patching meanwhile",
                     "Free the newcomers", "Welcome philosophy", "Stage the transition"],
         warnings=["Complaints without rivals", "Premature abandonment", "Legacy-locked minds", "All-or-nothing bets"]),
    dict(slug="ch-09-nature-and-necessity", num=9, title="Nature and Necessity of Revolutions",
         move="Win by Persuasion, Not Proof",
         problem="two courts in one hall, each judging the other by its own laws, gavel against gavel",
         problem_labels=["Circular debate", "No common measure"],
         episode="two astronomers at the same telescope drawing two different skies in their notebooks",
         episode_caption="Incommensurable worlds",
         stakes_labels=["Talking past", "Endless deadlock"],
         arc=("Shared-rules illusion", "Camps and circularity", "Persuasion campaign"),
         lesson="Paradigm debates cannot be proven", outcome="Demonstrations recruit; proofs don't",
         strategies=["Spot circular metrics", "Translate key terms", "Pilot visible wins",
                     "Recruit respected voices", "Skip knockdown memos", "Plan the campaign"],
         warnings=["Both sides self-scoring", "Terms shifting meaning", "Memo warfare", "Proof expectations"]),
    dict(slug="ch-10-revolutions-as-worldview-change", num=10, title="World-View Change",
         move="Retrain the Eyes, Not Just the Mind",
         problem="one swinging stone casting two different shadows: a struggling fall and a perfect pendulum",
         problem_labels=["Trained seeing", "No neutral view"],
         episode="Galileo Galilei (1564-1642) watching a swinging lamp and seeing periodic motion where others saw descent",
         episode_caption="Galileo sees the pendulum",
         stakes_labels=["Expert blindness", "Invisible objects"],
         arc=("Fixed data illusion", "Gestalt switch", "New world seen"),
         lesson="Paradigms restructure perception itself", outcome="Different training, different world",
         strategies=["Mix trained eyes", "Expect disorientation", "Name your blindspots",
                     "Retrain deliberately", "Distrust raw data talk", "Compare perceptions"],
         warnings=["One lens reviews", "Instant expert certainty", "Switch without retraining", "Neutral-data claims"]),
    dict(slug="ch-11-invisibility-of-revolutions", num=11, title="The Invisibility of Revolutions",
         move="Keep the Unsanitized Record",
         problem="a printing press smoothing a jagged mountain path into a straight paved road on the page",
         problem_labels=["Rewritten past", "Straightened path"],
         episode="John Dalton (1766-1844) beside a textbook that recasts his contested atomism as inevitable destiny",
         episode_caption="Dalton, straightened by textbooks",
         stakes_labels=["Institutional amnesia", "Warped judgment"],
         arc=("Polished history", "Consult raw records", "Honest memory"),
         lesson="Victors erase the revolution", outcome="Raw records guard judgment",
         strategies=["Archive real memos", "Record dead options", "Interview the losers",
                     "Date your certainties", "Reread before betting", "Teach the mess"],
         warnings=["Founding myths only", "Sanitized postmortems", "We-always-knew talk", "No dissent archive"]),
    dict(slug="ch-12-resolution-of-revolutions", num=12, title="The Resolution of Revolutions",
         move="Let Demonstrations and Time Decide",
         problem="a balance scale where one pan holds a proof and the other a crowd slowly walking across",
         problem_labels=["Proof insufficient", "Community tips"],
         episode="Max Planck (1858-1947) writing that new truths win as their opponents are outlived",
         episode_caption="Planck's grim principle",
         stakes_labels=["Wasted persuasion", "Stalled change"],
         arc=("Knockdown-proof hunt", "Early-adopter wins", "Profession tips"),
         lesson="Conversion cascades, proof does not", outcome="Faith plus promise starts every shift",
         strategies=["Arm early adopters", "Produce visible wins", "Route around veterans",
                     "Weigh the five values", "Audit your tenure", "Size faith bets"],
         warnings=["Memo-to-skeptics loops", "Waiting for proof", "Tenure as reasons", "No early bets"]),
    dict(slug="ch-13-progress-through-revolutions", num=13, title="Progress through Revolutions",
         move="Progress From, Not Toward",
         problem="a branching evolutionary tree of instruments growing upward with no crown or finish line",
         problem_labels=["No destination", "Growing power"],
         episode="a naturalist's desk where a map labeled 'to the truth' is replaced by a branching tree of species",
         episode_caption="Darwin's move, applied to knowledge",
         stakes_labels=["False destinations", "Expired fitness"],
         arc=("Truth-approach", "Fitness competition", "Goalless progress"),
         lesson="Later science solves more, aims nowhere", outcome="Capability is the real metric",
         strategies=["Measure solving power", "Drop destination talk", "Guard peer judgment",
                     "Insulate the work", "Refresh by turnover", "Adapt as environments shift"],
         warnings=["Final-answer chasing", "Fitness assumed permanent", "Lay metrics rule", "Progress as destiny"]),
    dict(slug="ch-14-postscript", num=14, title="Postscript 1969",
         move="Map the Disciplinary Matrix",
         problem="a single glowing word 'PARADIGM' splitting into four labeled layers stacked like strata",
         problem_labels=["Overloaded word", "Four layers"],
         episode="a lecture hall blackboard listing generalizations, models, values, exemplars in four gold strata",
         episode_caption="The matrix, itemized",
         stakes_labels=["Confused debates", "Misplaced fights"],
         arc=("One vague word", "Four components", "Legible disagreement"),
         lesson="Most logic fights are value-weightings", outcome="Translation, not bad faith",
         strategies=["Map the four layers", "Locate the fight's layer", "Weight values openly",
                     "Translate, then convert", "Spread the risk", "Repair vocabulary"],
         warnings=["Layer confusion", "Conversion demanded", "Values unexamined", "One-word arguments"]),
]


def start_prompt(c):
    return (
        f"Infographic, three vertical editorial panels. Top banner: dark navy bar with "
        f"\"CHAPTER {c['num']}\" in a gold box and title \"{c['title'].upper()}\" in large cream serif capitals. "
        f"LEFT panel header \"THE PROBLEM\": flat illustration of {c['problem']}, two small gold label boxes: "
        f"\"{c['problem_labels'][0]}\" and \"{c['problem_labels'][1]}\". "
        f"CENTER panel header \"KEY EPISODE\": editorial illustration of {c['episode']}, caption "
        f"\"{c['episode_caption']}\" beneath in gold serif. "
        f"RIGHT panel header \"THE STAKES\": illustration of the cost, two dark label boxes: "
        f"\"{c['stakes_labels'][0]}\" and \"{c['stakes_labels'][1]}\". "
        f"Bottom: gold label \"CORE MOVE\" then wide navy arrow containing \"{c['move'].upper()}\" in cream capitals. "
        + STYLE
    )


def end_prompt(c):
    return (
        f"Infographic dashboard. Top: dark navy header bar, gold \"CHAPTER {c['num']}\" then "
        f"\"{c['title'].upper()} — THE SHIFT\" in cream serif capitals. "
        f"LEFT section \"TRANSFORMATION ARC\": three circles connected by curved arrows — navy circle \"BEFORE: {c['arc'][0]}\", "
        f"gold circle \"SHIFT: {c['arc'][1]}\", coral circle \"AFTER: {c['arc'][2]}\". "
        f"CENTER section \"KEY EPISODE\" in a gold-bordered card: small editorial vignette of {c['episode_caption']}, "
        f"gold tag \"LESSON\" with text \"{c['lesson']}\", gold tag \"OUTCOME\" with text \"{c['outcome']}\". "
        f"RIGHT section \"PRACTICE CARDS\": six white cards in a 2x3 grid, each a simple line icon and a short label: "
        + ", ".join(f"\"{x}\"" for x in c["strategies"]) + ". "
        f"BOTTOM row \"WARNING SIGNS\": four red flag icons with labels "
        + ", ".join(f"\"{x}\"" for x in c["warnings"]) + ". "
        + STYLE
    )


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only")
    ap.add_argument("--force", action="store_true")
    a = ap.parse_args()
    fails = []
    for c in CH:
        if a.only and c["slug"] != a.only:
            continue
        for kind, p in (("start", start_prompt(c)), ("end", end_prompt(c))):
            out = OUTDIR / f"{c['slug']}-{kind}.png"
            if not gen(p, out, a.force):
                fails.append(out.name)
    print(f"\ndone. failures: {fails or 'none'}")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
