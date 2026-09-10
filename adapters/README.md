# Harness setup

EZ AI Academy uses one shared `SKILL.md` and one shared curriculum. These guides only map that package into each host's supported skill location and invocation pattern.

| Harness | Install guide | Start command |
|---|---|---|
| Codex | [`codex/INSTALL.md`](codex/INSTALL.md) | `$ai-academy` |
| Claude Code | [`claude-code/INSTALL.md`](claude-code/INSTALL.md) | `/ai-academy` |
| Cursor | [`cursor/INSTALL.md`](cursor/INSTALL.md) | Choose `ai-academy`, `ez-ai-academy`, or `start` from the `/` menu |
| Microsoft Copilot Cowork | [`microsoft-copilot-cowork/INSTALL.md`](microsoft-copilot-cowork/INSTALL.md) | Ask to start EZ AI Academy |

The curriculum must not be copied into an adapter. If a host needs different UI, paths, or packaging, adapt only those host-specific mechanics.

Cursor slash aliases (`/ez-ai-academy`, `/start`) are checkout project skills. They are not in the Cowork ZIP. Cowork still uses natural language (“Start EZ AI Academy as a new learner.”).

Installed copies do not auto-update. Each install guide has a **Stay current** section (`git pull`, fresh clone, or Cowork ZIP re-upload). What changed for learners: [`content/RELEASE_NOTES.md`](../content/RELEASE_NOTES.md).

Cursor Foundations acceptance has been validated via Cloud Agent with Markdown choice and image fallbacks ([#10](https://github.com/jensfossen/ez-ai-academy/issues/10)); that run did not test the IDE `/` menu. Cursor IDE chat vs Cloud Agent, plus video/choice-card research: [`cursor/INSTALL.md`](cursor/INSTALL.md), [`cursor/RICH_UI.md`](cursor/RICH_UI.md), [#24](https://github.com/jensfossen/ez-ai-academy/issues/24).

Claude Code in-pane Learn onboarding (competitive research, not a Foundations run): [`../ui/competitive-learn-claude-code.md`](../ui/competitive-learn-claude-code.md). [#14](https://github.com/jensfossen/ez-ai-academy/issues/14) remains blocked / not a Pass.

These instructions were last checked against vendor documentation on **2026-09-07**. Harness behavior changes quickly; record any deviation with the harness version in the [test matrix](../tests/harness-matrix.md).
