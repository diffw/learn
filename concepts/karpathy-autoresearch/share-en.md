---
concept: Karpathy autoresearch
slug: karpathy-autoresearch
type: share
language: en
created_at: 2026-05-04
based_on: reports/2026-05-03-deep-dive.md
platform: x.com / linkedin
---

# A UX Designer Reads Karpathy's autoresearch

A few days ago I opened `karpathy/autoresearch` — the repo that hit 30k stars in a week — read for three minutes, and closed the tab.

The README said "requires NVIDIA H100." The code was full of PyTorch. Words like `val_bpb` and `Muon optimizer` flew past me. My honest first reaction was: *not for me, come back later*.

But I had a problem stuck on my desk. I'm building Cap4u — a real-time captioning and translation app for non-native speakers making English phone calls — and I have 30+ quality metrics I need to keep tuning. Hand-tweaking one parameter, running a real call, eyeballing the result, and trying the next one… I was lucky to test two ideas a night.

So I went back. This time I didn't close the tab.

Looking back, that was the first time I — a UX designer with no engineering background — actually understood the architecture of a deep technical project. I want to write down what I learned. **The methodology behind autoresearch has almost nothing to do with hardware. The core idea can be borrowed by anyone who isn't writing training code.**

---

## A quick note on who Karpathy is

Worth covering, because the reception of this project is inseparable from his personal credibility.

Andrej Karpathy: Stanford PhD (advised by Fei-Fei Li, who created ImageNet), founding member of OpenAI in 2015, Director of AI at Tesla from 2017-2022 leading the Autopilot neural network, founder of the AI education company Eureka Labs in 2024.

What made him a household name for outsiders like me wasn't the titles. It was the teaching. Stanford's CS231n is widely treated as the entry point for deep learning. His YouTube "Build GPT from Scratch" / "Build a Tokenizer from Scratch" series — multi-hour videos where he writes everything live — is required watching in the field. And the code: nanoGPT (300 lines that actually train a GPT), micrograd (100 lines of working backprop), llm.c (LLM training in pure C so you can see every matrix multiply), nanochat.

The pattern is consistent: **take something that looks intimidating, and rewrite it in a few hundred lines you can read end-to-end.**

For non-engineers, Karpathy is one of a small number of people whose existence makes it feel possible to keep learning AI without being a PhD. autoresearch is the latest entry in that pattern.

## What this thing actually is

Karpathy released autoresearch in March 2026. He was working on nanochat (a tiny LLM training framework) and had hand-optimized it pretty well. But he had a hunch there was more.

His insight: *coding agents like Codex and Claude Code can already write PyTorch. Why not let one of them sit overnight, modify the training script, run 5-minute experiments, and keep only the wins?*

He let it run for two days. ~700 experiments. ~20 real improvements. 11% total speedup. Including one bug that he himself had missed — a missing scalar in the QK-Norm implementation that was making attention too uniform across heads. **A bug a senior researcher couldn't see, an agent found by blind iteration.**

Shopify's CEO Tobi Lütke ran the same protocol on his own search model. 37 experiments overnight. A 0.8B model that beat his hand-tuned 1.6B baseline by 19%.

The repo went from zero to 78k+ stars in a month.

---

## How it works (the part that matters)

Here's the entire system in one picture:

```text
program.md      <- the rulebook the human writes
prepare.py      <- read-only: scoring function + data
train.py        <- the only file the agent is allowed to edit
results.tsv     <- one line per experiment
```

The agent loop:

```text
read state -> propose hypothesis -> edit train.py
     ^                                     |
     |                                     v
keep / discard <- score <- run 5-minute training
```

Karpathy's tagline for this: **"one GPU, one file, one metric."**

The trick isn't the GPU or the file. It's the **one metric**.

---

## What I actually learned: it's an anti-cheating system

I needed two days to understand why the rules are so strict.

I assumed "one metric" was for simplicity. It isn't. **It's so the agent can't con itself.**

Think about hiring a barista to make better coffee. If you tell them "make better coffee," they'll secretly redefine "better" — *I think it tastes better* — and report 95/100 every cup. You take a sip. It's terrible.

If instead you say *"I define the rubric. I own the scale. I own the espresso machine. You can only change grind weight, water temperature, and extraction time"* — there's nowhere left to cheat. The only path forward is actually making better coffee.

autoresearch does exactly this:

```text
evaluate_bpb is locked inside prepare.py    -> agent can't redefine the metric
single number (val_bpb)                     -> no "different angle" excuses
fixed 5-minute budget                       -> can't win by training longer
agent never pauses                          -> every decision logged via git
```

This isn't *make the AI smarter*. It's *make it impossible for the AI to lie to you*.

After 20 years of watching product OKRs get gamed by clever metric redefinitions, this hit me hard. **autoresearch isn't an AI methodology. It's a research methodology, written in code an AI can run.**

---

## What it means for Cap4u

When I went back to look at my own repo, I found something funny: I had already written, months ago (with Codex's help), a 542-line document called `auto-research-call-caption-translation-optimization.md`. It translates Karpathy's protocol into Cap4u terms. It explicitly says *"don't run the original repo — we're not training LLMs, we're optimizing caption policy."*

Which means my real worry — *can Claude Code execute this the way Codex did?* — was the wrong question. The protocol is agent-agnostic. Karpathy's README literally says "any coding agent (Claude, Codex, etc.)."

What I actually lack isn't an agent. **It's a scoring function.**

Cap4u has 30+ metrics defined in a tracker, but no `score-candidate.ts` that turns them into a single number. The machine doesn't have a ruler yet.

My first draft of the 6-week plan was:

```text
Week 1: pick ONE metric, write a minimal score function
Week 2: hand-craft 5 candidate configs, run them manually
Week 3: let Claude Code take over, 20 rounds
Week 4: first overnight run, target 100 candidates
Week 5-6: add a second metric, calibrate
```

But writing this out, I went one level deeper and realized Week 1 should not start that way.

autoresearch can only amplify **what you measure**. If what you measure isn't what the user is actually hurting on, running faster makes things worse. Cap4u has run a few automated sweeps already — using PriMock57 (simulated medical calls), HarperValleyBank (simulated bank), NCSU robocall data as fixtures. We pushed WER from 6.33% down to 5.70%. Sounds great. Real users felt nothing. Reason: those fixtures aren't the calls Cap4u users actually make day to day.

So Week 1 should actually look like this:

```text
Day 1-2: make a real call (any natural scenario), record it
Day 3:   listen back, write down the 5-10 facts that mattered most
         ("she said her name is X / confirmation # Y / time Z / amount W / ...")
Day 4-5: encode those 10 facts into the score function
         score = (facts the captions got right) / (total facts)
         hard gate = confirmation # / amounts / times must be 100%
```

The other 5 weeks stay the same — but the score function is now permanently tied to that one real call's 10 facts. No more public datasets.

The most counterintuitive thing here isn't "don't optimize 30 metrics at once." It's one step earlier: **get the painful real call first. Then talk about the ruler.** One real call from a real user + their own 30-second annotation beats 100 overnight sweeps on public datasets.

Sounds obvious. But I tripped on this exact thing — all my earlier autoresearch runs were essentially "running faster on the wrong track."

---

## Five things I'm taking away

**1. Most "advanced" AI projects have a methodology layer that doesn't require AI knowledge.** The core of autoresearch is research discipline, not neural networks. A PM, a designer, an indie dev — anyone with a problem that has a programmable scoring function can use it.

**2. "Stop the AI from lying to you" is harder than "make the AI smarter."** Every AI workflow should answer the cheating question first. Who owns the rubric? Can it be locked? Then worry about how fast the agent runs.

**3. The H100 requirement is misleading.** I dismissed the project because I don't own a GPU. The original needs a GPU because *its demo scenario* is LLM training. The protocol itself is plain software engineering. I'm running a Cap4u version on my MacBook and Activity Monitor barely notices.

**4. "Running fast on the wrong track" is the failure mode AI tooling hides best.** autoresearch lets you run 100 experiments overnight, but if your score function doesn't encode real user pain, fast just means wrong-faster. I just downgraded my own 6-week plan in section "What it means for Cap4u" — and I only caught it because I was writing it down.

**5. As a designer, I can read this kind of code now.** This one matters more than the other four. Three years ago I couldn't get through a README. Today I can read a 600-line PyTorch project, understand its design philosophy, and port the protocol layer into my own product. **Not because I got smarter. Because AI dropped the bar for "reading code" by an order of magnitude.**

---

## Closing

autoresearch reminded me that for decades, the bottleneck in research was never the ideas. It was the **discipline to keep validating them**. AI won't generate better ideas than you. But it will happily try 100 of yours overnight while you sleep.

Karpathy wrote that discipline into 600 lines of Python so anyone can run it. I'm copying the same discipline into Cap4u — not to make the AI smarter, but so I, as the product judge, can see 100 real results in the morning instead of 5 of my own guesses by the end of a week.

If you have a "I want to optimize this but don't know where to start" problem on your desk, ask yourself three things:

- Can the score be written as a function?
- Can a failure be rolled back instantly?
- Do I have a fixed sample set I can replay?

Three yeses → you can run your own autoresearch.

I'll keep posting as Cap4u's experiment loop comes online. More soon.
