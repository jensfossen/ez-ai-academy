# Install in Cursor

Cursor supports Agent Skills in personal and project directories. A personal installation makes the Academy available across projects.

## macOS or Linux

```bash
mkdir -p "$HOME/.cursor/skills"
git clone https://github.com/jensfossen/ez-ai-academy.git "$HOME/.cursor/skills/ai-academy"
```

## Windows PowerShell

```powershell
New-Item -ItemType Directory -Force "$HOME\.cursor\skills" | Out-Null
git clone https://github.com/jensfossen/ez-ai-academy.git "$HOME\.cursor\skills\ai-academy"
```

In Cursor chat, type `/` and select `ai-academy`. You can also ask naturally to start EZ AI Academy.

For a project-only install, clone the repository to `.cursor/skills/ai-academy` or `.agents/skills/ai-academy` in that project. Cursor can also discover compatible Claude and Codex skill directories.

## Cursor IDE chat vs Cloud Agent

These are different surfaces. Do not treat a Cloud Agent result as an IDE native-UI Pass. Rich-UI work is tracked in [#24](https://github.com/jensfossen/ez-ai-academy/issues/24). Research notes: [`RICH_UI.md`](RICH_UI.md).

**Cursor IDE chat** is the reference surface. Prefer the host ask-questions picker when the host attaches it (Plan Mode family; forum/host alias AskQuestion), and in-chat video when the IDE can play a lesson link. Neither is a published skill-author API, and the picker is not guaranteed in every Agent chat — details in [`RICH_UI.md`](RICH_UI.md). Do not invent private markup. If a native control is missing, use the Markdown numbered-list and link fallbacks.

**Cursor Cloud Agent** uses Markdown fallbacks only. Cloud Agents may load `SKILL.md` from a checkout of this repository, or from a personal install after enabling **Settings → Agents → Sync Skills**. Cloud Agent chat uses numbered-list choices (native tappable cards are unavailable). Offer lesson video as an external link plus the text alternative; in-chat playback is not available. Image acceptance is a markdown image plus alt text, or a meaningful description; inline raster display is UI-dependent and not guaranteed.

To update later, run `git pull` inside the installed `ai-academy` directory.

Source: [Cursor — Agent Skills](https://cursor.com/docs/skills). Last verified 2026-09-09. IDE ask-questions and in-chat-video research remains open on [#24](https://github.com/jensfossen/ez-ai-academy/issues/24).
