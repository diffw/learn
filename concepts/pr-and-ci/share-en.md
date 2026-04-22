---
concept: PR and CI
slug: pr-and-ci
type: share
language: en
created_at: 2026-04-21
based_on: reports/2026-04-20-deep-dive.md
platform: x.com / linkedin
---

# I Don't Write Code. Here's Why I Still Need PR and CI.

A few days ago, I noticed that my GitHub Actions CI had been failing for three straight days. Billing issue. Easy fix.

But what bothered me wasn't the failure itself — it was that I hadn't even noticed. For three days, code was being pushed to main with zero automated checks, and nothing felt different.

That's when I realized: the absence of a safety net only matters when you fall.

## Some context

I'm a UX designer with 20+ years of experience. Last year, I started building products as a solo indie dev using AI. I now have a macOS app called **Vibe Capture** on the App Store.

Here's the thing — I don't write code. AI does. I make product decisions, define user flows, judge whether something feels right. But when it comes to the actual code? I can't read it, I can't review it, and I definitely can't spot edge cases in it.

So I needed a system that could check the code for me. That's what led me to learn about Pull Requests and Continuous Integration.

## Where these ideas came from

CI dates back to 1996. Kent Beck introduced the practice in Extreme Programming: developers should integrate their code daily instead of working in isolation for weeks and merging at the end. Back then it was pure discipline — no automation at all.

In 2001, ThoughtWorks released CruiseControl, the first CI server. That's when CI went from "a team habit" to "a system that runs automatically." Jenkins and Travis CI followed in 2011. Then in 2019, GitHub Actions embedded CI directly into the code hosting platform — no more wiring up third-party services.

PR has a different origin story. In 2008, GitHub took the Linux kernel community's patch-by-email workflow and turned it into the Pull Request — a visual, commentable, trackable web interface for code review. GitLab later called theirs a Merge Request. Same concept, different name.

These aren't new ideas. CI is nearly 30 years old. PR is nearly 20. They've lasted this long because they solve a real, persistent problem: how do you keep a codebase healthy when multiple changes happen in parallel?

## The actual mechanics

Setting my personal interpretation aside for a moment, here's how PR and CI work in practice:

```
Developer writes code on a feature branch
  -> Creates a PR (describes what changed and why)
  -> CI triggers automatically: pull code -> build -> run tests -> generate report
  -> CI result appears on the PR page (green check / red X)
  -> Reviewer checks the code + CI status
  -> All pass -> merge into main
  -> Anything fails -> fix and resubmit
```

A few key concepts within this flow:

1. **Branch Protection**: rules on the main branch — CI must pass, reviews must be approved, direct pushes are blocked. This is what turns the process from "recommended" to "enforced."
2. **Status Checks**: the pass/fail badge CI reports back to GitHub, displayed directly on the PR page. Green or red, no ambiguity.
3. **Pipeline**: the sequence of automated steps CI runs — install dependencies, compile, run tests, generate coverage reports.

## What I learned (in plain English)

**A Pull Request (PR)** is basically saying: "Hey, I've got some changes. Before they go into the main codebase, let's run some checks and make sure nothing breaks."

**Continuous Integration (CI)** is the automated part — every time code changes, a server pulls the latest version, builds it, runs tests, and reports back: pass or fail.

The two work together: a PR triggers CI, CI results show up on the PR, and you only merge when everything's green.

Think of it this way: PR is the submission process, CI is the automated proofreader. One manages the workflow, the other does the actual checking.

## What I found in my own project

Vibe Capture already had CI set up. A GitHub Actions workflow running builds across three macOS versions (14, 15, and 26), with unit tests and coverage reports. PRs were being used too, with clean branch naming conventions.

Sounds decent, right?

Then I actually audited it. Here's what I found:

1. **The CI had `|| true` at the end of build and test steps.** This means even if the build fails or tests break, CI still reports green. My CI was a decoration — always passing, never actually catching anything.

2. **Multiple commits were pushed directly to main**, bypassing the PR process entirely. No branch protection rules were configured.

3. **All 18 PRs had zero code reviews.** Every single one was self-merged. Which, for a solo developer, is understandable — but it means CI was my *only* real quality gate, and I had accidentally disabled it.

The pattern was clear: **the process existed, but it wasn't enforced.**

It's like having a lock on your door that you never actually turn.

## What I took away from this

**1. When you can't read code, CI is your only technical safety net.**

I can't review code quality through reading. I can't catch logic bugs by intuition. CI — when it actually works — is the one mechanism that doesn't require me to understand code in order to trust it.

**2. PR isn't about me reviewing AI's code. It's about creating checkpoints.**

The value of PRs in my workflow isn't code review. It's: triggering CI automatically, documenting what each change does and why, and making it possible to revert cleanly when something goes wrong.

**3. Process must be system-enforced, not willpower-enforced.**

Solo developers are the most likely to skip process when things get busy. Branch protection rules exist precisely so you can't skip them even when you want to.

**4. Your user perspective is a source of test standards.**

I can't define test cases in code. But I can define what users should see when they open the app, what should happen when they click a button, what "working correctly" looks like from a product perspective. AI can translate those definitions into automated tests. My product instincts become repeatable checks instead of one-time manual verification.

**5. A slow CI that actually catches failures beats a fast CI that's always green.**

Fix the `|| true` first. Optimize for speed later.

## The bigger picture

Engineers have known about PR and CI forever. Me writing about this probably feels like a designer explaining version control at a hackathon.

But I think that's exactly the point. In the age of AI-assisted development, more non-engineers are building real products. The code can be AI-generated, but quality can't be left to chance.

If you're a designer, a PM, or anyone using AI to ship software — and you haven't set up CI yet — you're flying without instruments.

The runway looks clear until it isn't.
