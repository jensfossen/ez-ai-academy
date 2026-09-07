# Harness setup

Easy AI Academy uses one shared `SKILL.md` and one shared curriculum. These guides only map that package into each host's supported skill location and invocation pattern.

| Harness | Install guide | Start command |
|---|---|---|
| Codex | [`codex/INSTALL.md`](codex/INSTALL.md) | `$ai-academy` |
| Claude Code | [`claude-code/INSTALL.md`](claude-code/INSTALL.md) | `/ai-academy` |
| Cursor | [`cursor/INSTALL.md`](cursor/INSTALL.md) | Choose `ai-academy` from the `/` menu |
| Microsoft Copilot Cowork | [`microsoft-copilot-cowork/INSTALL.md`](microsoft-copilot-cowork/INSTALL.md) | Ask to start Easy AI Academy |

The curriculum must not be copied into an adapter. If a host needs different UI, paths, or packaging, adapt only those host-specific mechanics.

These instructions were last checked against vendor documentation on **2026-09-07**. Harness behavior changes quickly; record any deviation with the harness version in the [test matrix](../tests/harness-matrix.md).
