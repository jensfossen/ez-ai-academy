# Harness setup

EZ AI Academy uses one shared `SKILL.md` and one shared curriculum. These guides only map that package into each host's supported skill location and invocation pattern.

| Harness | Install guide | Start command |
|---|---|---|
| Codex | [`codex/INSTALL.md`](codex/INSTALL.md) | `$ai-academy` |
| Claude Code | [`claude-code/INSTALL.md`](claude-code/INSTALL.md) | `/ai-academy` |
| Cursor | [`cursor/INSTALL.md`](cursor/INSTALL.md) | Choose `ai-academy`, `ez-ai-academy`, or `start` from the `/` menu |
| Microsoft Copilot Cowork | [`microsoft-copilot-cowork/INSTALL.md`](microsoft-copilot-cowork/INSTALL.md) | Ask to start EZ AI Academy |
| Grok Bot | [`grok-bot/INSTALL.md`](grok-bot/INSTALL.md) | In Teacher, ask to start (create Teacher only if you are not already in that chat) |

The curriculum must not be copied into an adapter. If a host needs different UI, paths, or packaging, adapt only those host-specific mechanics.

Cursor slash aliases (`/ez-ai-academy`, `/start`) are checkout project skills. They are not in the Cowork ZIP. Cowork still uses natural language (“Start EZ AI Academy as a new learner.”).

Installed copies do not auto-update. Each install guide has a **Stay current** section (`git pull`, fresh clone, Cowork ZIP re-upload, or Grok Bot Teacher re-read / `git pull`). What changed for learners: [`content/RELEASE_NOTES.md`](../content/RELEASE_NOTES.md).

Grok Bot’s learner interface is a **Teacher** bot that follows root `SKILL.md` — not a skills-folder clone and not a curriculum fork. Create Teacher only when you are not already in that chat. Academy only (not Personal OS / Family OS). Install contract / To run — not a Pass ([#53](https://github.com/jensfossen/ez-ai-academy/issues/53)).

Cursor Foundations acceptance has been validated via Cloud Agent with Markdown choice and image fallbacks ([#10](https://github.com/jensfossen/ez-ai-academy/issues/10)); that run did not test the IDE `/` menu. Cursor IDE chat vs Cloud Agent, plus video/choice-card research: [`cursor/INSTALL.md`](cursor/INSTALL.md), [`cursor/RICH_UI.md`](cursor/RICH_UI.md), [#24](https://github.com/jensfossen/ez-ai-academy/issues/24).

Claude Code in-pane Learn onboarding (competitive research, not a Foundations run): [`../ui/competitive-learn-claude-code.md`](../ui/competitive-learn-claude-code.md). [#14](https://github.com/jensfossen/ez-ai-academy/issues/14) remains blocked / not a Pass.

These instructions were last checked against vendor documentation on **2026-09-07** (Grok Bot: **2026-09-10**). Harness behavior changes quickly; record any deviation with the harness version in the [test matrix](../tests/harness-matrix.md).
