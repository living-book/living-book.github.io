#!/usr/bin/env python3
"""Stage 3: Lakatos — Scientific Research Programmes infographics. Run from repo root."""
import argparse, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from gen_infographics import STYLE, gen

OUTDIR = Path("docs/books/scientific-research-programmes/infographics")

CH = [
    dict(slug="concept-01-the-problem", num=1, title="Rescuing Rationality",
         move="Judge Trajectories, Not Snapshots",
         problem="a judge freezing a single frame of a running race and declaring the leader, ignoring the race still unfolding",
         problem_labels=["Snapshot verdict", "Ignored trajectory"],
         episode="a portrait of Isaac Newton beside a telescope, anomalies swirling around a serene planetary system",
         episode_caption="Newton: born refuted, most successful",
         stakes_labels=["Truth by crowd", "Rationality lost"],
         arc=("Snapshot appraisal", "Judge the series", "Rational trajectory"),
         lesson="Great science lived in anomalies", outcome="Rationality lives in trajectories",
         strategies=["Appraise series", "Ignore snapshots", "Track novel successes",
                     "Separate today's flaws", "Watch the growth curve", "Reconstruct rationally"],
         warnings=["One-refutation verdicts", "Is-X-dead debates", "Present-moment judging", "Mob-psychology fear"]),
    dict(slug="concept-02-sophisticated-falsificationism", num=2, title="Sophisticated Falsificationism",
         move="No Falsification Without a Better Rival",
         problem="a boxer refusing to leave the ring until a stronger challenger actually climbs through the ropes",
         problem_labels=["Theory alone", "Never refuted solo"],
         episode="the astronomer Le Verrier calculating an unseen planet's position, Neptune appearing exactly there",
         episode_caption="Neptune found by auxiliary",
         stakes_labels=["Grievance piles", "No decision"],
         arc=("Evidence-alone refutation", "Rival required", "Theory succession"),
         lesson="Rivals refute; evidence alone can't", outcome="Better theory digests the anomaly",
         strategies=["Build the rival", "Retain old wins", "Corroborate novelty",
                     "Blame the auxiliaries", "Wait for competition", "Crown crucial-tests late"],
         warnings=["Grievance lists", "Refute without replacing", "Duhem ignored", "Hindsight crownings"]),
    dict(slug="concept-03-research-programme", num=3, title="The Research Programme",
         move="Model Endeavors as Programmes",
         problem="a medieval castle: an inner keep ringed by expendable outer walls and a written battle plan on a table",
         problem_labels=["Core plus belt", "Battle plan"],
         episode="a diagram of the Newtonian programme: three laws at the center, optics and perturbations as outworks",
         episode_caption="Newton's programme dissected",
         stakes_labels=["Foundation churn", "Panic pivots"],
         arc=("Isolated theories", "Structured campaign", "Long programme"),
         lesson="The programme, not the theory, is judged", outcome="Structure gives staying power",
         strategies=["State the hard core", "Map the belt", "Follow the heuristic",
                     "Belt-adjust calmly", "Spot real vs fake pivots", "Appraise the whole"],
         warnings=["Core relitigated", "Belt panic as crisis", "No development plan", "Foundations churned"]),
    dict(slug="concept-04-hard-core", num=4, title="The Hard Core",
         move="Protect Foundations by Decision",
         problem="a fortress keep sealed by an explicit written decree, all attacks redirected to the outer walls",
         problem_labels=["Irrefutable by choice", "Deflect to belt"],
         episode="the chemist Prout's law of whole-number atomic weights, defended for a century against contrary measurements",
         episode_caption="Prout's core, vindicated by isotopes",
         stakes_labels=["Foundations shift", "No deep results"],
         arc=("Foundations up for grabs", "Core fixed by decision", "Rational tenacity"),
         lesson="Fixing foundations lets depth grow", outcome="A century's dogmatism paid off",
         strategies=["Declare the core", "Route criticism to belt", "Protect by policy",
                     "Divide labor over time", "Calendar core reviews", "Define degeneration signals"],
         warnings=["Core under daily attack", "Unexamined protection", "Pseudo-science shielding", "No expiry set"]),
    dict(slug="concept-05-protective-belt", num=5, title="The Protective Belt",
         move="Route Anomalies to the Periphery",
         problem="concentric shields around a core, each outer ring taking arrows so the center stays untouched",
         problem_labels=["Adjustable auxiliaries", "Absorbs the hits"],
         episode="a split scene: Neptune predicted and found versus the phantom planet Vulcan searched for and never found",
         episode_caption="Neptune triumph vs Vulcan decay",
         stakes_labels=["Ad hoc debt", "Endless patching"],
         arc=("Anomaly as threat", "Anomaly as work item", "Content-increasing fixes"),
         lesson="Belt absorbs; fixes must predict new facts", outcome="Neptune progressed, Vulcan degenerated",
         strategies=["Map the belt", "Grade each fix", "Demand new predictions",
                     "Route blame first", "Spot your Vulcan", "Avoid ad hoc debt"],
         warnings=["Backward-only fixes", "Repeated patching", "Blame the core", "No novel content"]),
    dict(slug="concept-06-positive-heuristic", num=6, title="The Positive Heuristic",
         move="Plan the Sequence of Better Models",
         problem="an architect's phased blueprint: a crude sketch, then refined drafts, each planned before the last is built",
         problem_labels=["Planned agenda", "Scheduled anomalies"],
         episode="Newton's model sequence: a point-sun, then planets, then spinning bulging spheroids, unrolling in order",
         episode_caption="Newton's planned curriculum",
         stakes_labels=["Reactive scramble", "Complaint queue"],
         arc=("Reactive science", "A battle plan", "Programmed development"),
         lesson="The plan schedules its own anomalies", outcome="Models improve on a curriculum",
         strategies=["Draft the model sequence", "Lift one idealization", "Ignore scheduled anomalies",
                     "Plan, don't react", "Autonomy from noise", "Watch the plan run dry"],
         warnings=["Backlog not roadmap", "Every anomaly reorders", "No idealization plan", "Heuristic exhausted"]),
    dict(slug="concept-07-progressive-vs-degenerating", num=7, title="Progressive vs Degenerating",
         move="Predict Novelty, Don't Explain Away",
         problem="two runners: one sprinting ahead of the finish tape, one trudging behind it inventing excuses",
         problem_labels=["Predicts novelty", "Explains after"],
         episode="Einstein's predicted light-bending confirmed by Eddington, beside Marxism patching failed predictions",
         episode_caption="Einstein progresses, Marxism degenerates",
         stakes_labels=["Pseudo-science", "Sunk-cost hype"],
         arc=("Snapshot content", "Score the shifts", "Trajectory verdict"),
         lesson="Novelty predicted vs excuses offered", outcome="Trajectory, not content, demarcates",
         strategies=["Score last five shifts", "Count novel facts", "Audit hyped tech",
                     "Demand improbable predictions", "Run quarterly reviews", "Allow recovery"],
         warnings=["Five excuses running", "Roadmap hides decay", "Accommodation only", "No novel calls"]),
    dict(slug="concept-08-no-instant-rationality", num=8, title="No Instant Rationality",
         move="Verdicts Are Retrospective; Keep Honest Score",
         problem="a scoreboard whose numbers only become legible in a rear-view mirror as the game recedes",
         problem_labels=["Slow rationality", "Hindsight verdicts"],
         episode="the Michelson-Morley ether experiment, crowned crucial only decades later after Einstein's rise",
         episode_caption="Crucial only in hindsight",
         stakes_labels=["False verdicts", "Cooked books"],
         arc=("Instant-verdict myth", "Slow appraisal", "Honest scorekeeping"),
         lesson="Crucial experiments crowned in hindsight", outcome="Bet freely, but keep honest score",
         strategies=["Date your verdicts", "Name the gamble", "Show the score",
                     "Allow rational disagreement", "Defer to the future", "Never cook books"],
         warnings=["Real-time obituaries", "Denied poor records", "Instant coronations", "Score concealed"]),
    dict(slug="concept-09-history-and-methodology", num=9, title="History and Methodology",
         move="Test Methodologies Against History",
         problem="a rulebook being weighed on a scale against the vast archive of scientific history",
         problem_labels=["Methodology as programme", "History as test"],
         episode="Lakatos's page with rational reconstruction in the main text and real deviations in the footnotes",
         episode_caption="History in the footnotes",
         stakes_labels=["Standards regress", "Blind history"],
         arc=("Ungrounded standards", "Self-application", "Historically tested"),
         lesson="Judge methodology by rationality recovered", outcome="Philosophy meets the archive",
         strategies=["Apply to itself", "Maximize internal history", "Keep the footnotes",
                     "Test against best calls", "Measure the residue", "Reconstruct honestly"],
         warnings=["Framework forbids best calls", "No footnote discipline", "History ignored", "Standards unexamined"]),
]

def start_prompt(c):
    return (f"Infographic, three vertical editorial panels. Top banner: dark navy bar with "
        f"\"CONCEPT {c['num']}\" in a gold box and title \"{c['title'].upper()}\" in large cream serif capitals. "
        f"LEFT panel header \"THE PROBLEM\": flat illustration of {c['problem']}, two small gold label boxes: "
        f"\"{c['problem_labels'][0]}\" and \"{c['problem_labels'][1]}\". "
        f"CENTER panel header \"KEY EPISODE\": editorial illustration of {c['episode']}, caption "
        f"\"{c['episode_caption']}\" beneath in gold serif. "
        f"RIGHT panel header \"THE STAKES\": illustration of the cost, two dark label boxes: "
        f"\"{c['stakes_labels'][0]}\" and \"{c['stakes_labels'][1]}\". "
        f"Bottom: gold label \"CORE MOVE\" then wide navy arrow containing \"{c['move'].upper()}\" in cream capitals. " + STYLE)

def end_prompt(c):
    return (f"Infographic dashboard. Top: dark navy header bar, gold \"CONCEPT {c['num']}\" then "
        f"\"{c['title'].upper()} — THE SHIFT\" in cream serif capitals. "
        f"LEFT section \"THE ARC\": three circles connected by curved arrows — navy circle \"BEFORE: {c['arc'][0]}\", "
        f"gold circle \"SHIFT: {c['arc'][1]}\", coral circle \"AFTER: {c['arc'][2]}\". "
        f"CENTER section \"KEY EPISODE\" in a gold-bordered card: small editorial vignette of {c['episode_caption']}, "
        f"gold tag \"LESSON\" with text \"{c['lesson']}\", gold tag \"OUTCOME\" with text \"{c['outcome']}\". "
        f"RIGHT section \"PRACTICE CARDS\": six white cards in a 2x3 grid, each a simple line icon and a short label: "
        + ", ".join(f"\"{x}\"" for x in c["strategies"]) + ". "
        f"BOTTOM row \"WARNING SIGNS\": four red flag icons with labels "
        + ", ".join(f"\"{x}\"" for x in c["warnings"]) + ". " + STYLE)

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--only"); ap.add_argument("--force", action="store_true")
    a = ap.parse_args(); fails = []
    for c in CH:
        if a.only and c["slug"] != a.only: continue
        for kind, p in (("start", start_prompt(c)), ("end", end_prompt(c))):
            out = OUTDIR / f"{c['slug']}-{kind}.png"
            if not gen(p, out, a.force): fails.append(out.name)
    print(f"\ndone. failures: {fails or 'none'}"); return 1 if fails else 0

if __name__ == "__main__":
    sys.exit(main())
