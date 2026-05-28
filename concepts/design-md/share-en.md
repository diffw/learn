---
concept: Design.md
slug: design-md
type: share
language: en
created_at: 2026-05-18
based_on: reports/2026-05-08-deep-dive.md
platform: x.com / linkedin
---

# A New Canvas for Designers: Reading Google's DESIGN.md

For the first time in 20 years, I'm questioning whether "UX Designer" is still a real role.

Not because AI is taking my work — but because I open Figma less and less.

I'm building Cap4u (a real-time captioning app for non-native English speakers on phone calls), and my daily work has shifted to writing Markdown, configuring Claude Code, and reviewing AI-generated code. Figma files feel like intermediate artifacts I draw for myself, rather than something anyone actually implements from.

A quiet worry kept growing: as a designer, am I gradually losing global control over how the product looks?

Then Google Labs Code open-sourced something called `DESIGN.md` in April 2026.

---

## 1. This isn't another tool

My first reaction was "great, another design system framework." After reading the spec, I realized this isn't a tool. It's a **protocol**.

It defines a standard Markdown file format:

- The front part is machine-readable YAML (colors, typography, spacing, component tokens)
- The body is human-readable Markdown (design rationale, do's and don'ts)

One file, read by both the designer and the AI agent. You write it once, and Claude Code, Cursor, Google Stitch, or any future AI tool can generate UI consistent with your brand.

Simple to the point of skepticism: that's it?

---

## 2. It's part of a bigger wave

Stepping back, DESIGN.md isn't isolated. It belongs to the 2025-2026 wave of "AI engineering protocol files":

```text
AGENTS.md     Dec 2025 — OpenAI / Google / Cursor / Sourcegraph / Factory
              donated to the Linux Foundation
              -> what agents can and can't do in this repo

SKILL.md      Anthropic / Agent Skills standard
              -> how agents should complete specific task types

DESIGN.md     April 2026, Google Labs
              -> what visual language agents should use when generating UI

program.md    March 2026, Karpathy autoresearch
              -> what discipline agents should follow when running experiments
```

The common pattern: **humans write Markdown, agents read Markdown, tooling validates it.**

We're transitioning from the 2024 chaos of "show AI a Figma screenshot and hope" to the 2026 discipline of "feed AI a structured design protocol."

---

## 3. A counterintuitive find: Cap4u was already doing this

After reading the spec, I browsed my own Cap4u repo and found something surprising.

My `.vibe-doc/design-token.json` (170 lines) + `design-system.md` (v1.3) + `.agents/rules/shared/design-defaults.md`, taken together, are **more complete than DESIGN.md's current alpha spec.**

Three things DESIGN.md alpha is missing — Cap4u already has all of them:

| Dimension | DESIGN.md alpha | Cap4u |
|---|---|---|
| Negative Defaults (what NOT to do) | ✗ | ✓ |
| Appearance Policy (system / fixedLight) | ✗ | ✓ |
| Decision Order (priorities when rules conflict) | ✗ | ✓ |

I always thought I was being dragged along by the AI era. Turns out I (with Codex and Claude Code's help) had independently figured out three layers DESIGN.md is still trying to standardize.

That reframed how I think about being a designer in the AI era.

---

## 4. Designers don't disappear. The canvas changes.

After reading DESIGN.md, I'm convinced:

```text
Disappearing:
  Figma operators who make mocks for developers to translate
  People who polish brand guideline PDFs
  People who only decorate inside tools

Emerging:
  Designers who can read/write protocols like DESIGN.md
  Designers who maintain "what not to do" rules
  Designers who define agent boundaries in AGENTS.md

In short:
  Designers are no longer "people who draw pictures."
  They are "people who define rules."
```

For me personally: **the 10 years of design system work I did in Figma transfers fully to DESIGN.md. The skill doesn't disappear. The medium changes.**

Figma file → DESIGN.md. Dragging rectangles → writing token references. Same activity at the core: **using a structured representation to define what the product should look like.**

---

## 5. Takeaways worth saving

A checklist I'm keeping for myself. If you only read this section, take these seven:

**1. DESIGN.md isn't a new document. It's "the medium of design moving from images to rules."**
A decade of Figma design system work doesn't disappear — it changes form. Figma file → DESIGN.md. The skill transfers fully.

**2. Before writing DESIGN.md, write a "vibe prompt" first.**
Skipping the vibe and asking AI to "make me a design system" produces something correct but bland. Spend 5-10 lines defining what you want and what you absolutely don't want (e.g., "no blue-purple gradients, no cyan-on-dark, no glassmorphism"). Then ask AI to propose tokens.

**3. For cross-platform products, don't name tokens with web-isms like H1 / H2.**
Use semantic names like `display-large / headline-medium / body-medium`. H1 is HTML vocabulary — iOS doesn't have it. iOS uses `largeTitle` — web doesn't. Map per-platform in your runtime layer.

**4. Strict enforcement requires 5 layers, not one layer maximized.**
`Agent reads it → runtime constraints → CI lint → visual regression → code review`. Miss any one and it gets bypassed. Highest ROI: hook `npx @google/design.md lint` into CI. 2 hours of work, permanent value.

**5. In the AI era, DESIGN.md is a designer's canvas, not a post-mortem.**
Old flow: Figma → design system → code (DESIGN.md as after-the-fact summary).
New flow: DESIGN.md → AI generates UI → review → revise DESIGN.md (DESIGN.md as the primary canvas).
This inversion is quietly happening to a lot of indie devs — most just haven't named it.

**6. DESIGN.md alpha hasn't converged on Dark Mode or Negative Defaults.**
Don't wait for the spec to tell you. Define it yourself. Cap4u uses `color.light.* / color.dark.* / liveCallAdaptive.*` namespaces — more engineering-grade than the current alpha approach.

**7. UX designers don't disappear. They transform.**
No longer "people who draw pictures" — "people who define rules." The concrete work: write down all five layers — tokens, rationale, negative defaults, decision order, runtime SSOT. Miss any layer and AI will fill in whatever it wants.

---

## 6. Closing

Before reading DESIGN.md, I worried that design in the AI coding era would become loose and incoherent.

After reading it, I'm more optimistic than before. **A structured design protocol lets a designer define one global, persistent visual contract** — and have AI agents respect it across sessions, tools, and platforms. That wasn't possible in the Figma era.

If you have a Figma file or a scattered set of tokens lying around, here's a 2-hour weekend project: consolidate them into a single DESIGN.md and drop it in your repo root.

Where to start:

- Official spec: `github.com/google-labs-code/design.md`
- 454 public design systems to fork: `designmd.app`
- Awesome list: `github.com/VoltAgent/awesome-design-md`

And I'm curious: how are you managing design in your AI coding workflow right now? Reply, I'd love to hear.

More soon.
