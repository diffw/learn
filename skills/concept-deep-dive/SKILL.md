---
name: concept-deep-dive
description: Research a concept, method, framework, pattern, protocol, or mental model in depth and save the finished report into this learning repository. Use when the user asks to learn, study, compare, explain, or deep-dive a new concept such as "Honest Agent", "Agentic Loop", "帮我调研 X", or "我想系统学习一个新方法".
---

# Concept Deep Dive

## Workflow

1. Read `concept-deep-dive-prompt-v5.md` and treat it as the default report structure.
2. Read `rules/research-workflow.md`, `rules/source-quality.md`, `rules/report-style.md`, and `rules/report-filing.md`.
3. Extract the runtime inputs:
   - concept
   - optional domain
   - optional target repository or local project path for section 8
4. Resolve the output path before writing anything:

```bash
python3 scripts/prepare_concept_report.py --concept "Honest Agent" --root . --json
```

5. Research the concept using the prompt's 0-8 structure.
6. Save the report under `concepts/<slug>/reports/`.
7. Only after the file exists on disk, reply to the user with the saved path and a short summary.

## Decision Rules

- If the user provides a custom prompt, use it instead of `concept-deep-dive-prompt-v5.md`, but keep this repository's filing rules.
- If the user names only the concept, leave `domain` empty rather than guessing.
- If section 8 applies, read [references/repo-analysis-policy.md](references/repo-analysis-policy.md) before evaluating the repository.
- If no real target repository is available for section 8, keep the section and explicitly state that the repository analysis could not be completed.
- Do not force the current learning repository to become the section 8 target unless it is obviously the intended project.

## Research Rules

- Browse the web for any current, unstable, or source-sensitive information, especially in sections 5 and 7.
- Prefer primary sources: papers, official docs, official repositories, maintainer notes, release notes.
- Keep the report in Chinese unless the user explicitly requests another language.
- Distinguish facts from inferences. When a claim is inferred, label it clearly.
- If reliable information cannot be found, say so directly instead of filling the gap with generic prose.
- Treat report depth as the default. Unless the user asks for brevity, target a long-form report, typically 10000+ Chinese characters when reliable sources support it.
- In paper sections, explain problem setting, method design, validation logic, findings, limits, and influence. Do not collapse a paper into one short paragraph.

## Output Rules

- Save every finished report with the frontmatter defined in `rules/report-filing.md`.
- Preserve the prompt's numbered structure instead of rewriting it into a different outline.
- Reuse an existing concept slug folder when present.
- Use ASCII for all process, logic, state, and map expressions, such as `A -> B -> C` and `input -> process -> output`.
