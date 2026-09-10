# Install in Cursor

## Primary: clone the repository in Cursor

If Cursor is already installed:

1. **New Window → Clone repo** (File → New Window → Clone repo, or the Cursor **Clone repo** option).
2. Paste `https://github.com/jensfossen/ez-ai-academy`.
3. In chat, type `/` and choose `ai-academy` (canonical), `ez-ai-academy`, or `start`. Or ask naturally to start EZ AI Academy. All three load the same root `SKILL.md`.

## Other install paths (optional)

Personal skills-folder and terminal clones are secondary. Use them only if you want the Academy available across projects, a project-only copy, or a git clone outside the Cursor UI.

### Personal skills folder

A personal install at `~/.cursor/skills` makes the Academy available across projects.

**macOS or Linux**

```bash
mkdir -p "$HOME/.cursor/skills"
git clone https://github.com/jensfossen/ez-ai-academy.git "$HOME/.cursor/skills/ai-academy"
```

**Windows PowerShell**

```powershell
New-Item -ItemType Directory -Force "$HOME\.cursor\skills" | Out-Null
git clone https://github.com/jensfossen/ez-ai-academy.git "$HOME\.cursor\skills\ai-academy"
```

Then start the same way: type `/` and choose `ai-academy`, or ask naturally to start EZ AI Academy. A personal global install of `/start` may collide with other projects — **repo checkout is the intended primary install path.**

### Project-only

Clone the repository to `.cursor/skills/ai-academy` or `.agents/skills/ai-academy` in that project. Cursor can also discover compatible Claude and Codex skill directories.

## Stay current

This checkout does not update itself. Curriculum and media change on `main`.

- **Clone repo (primary):** in a terminal at the repository root, run `git pull origin main`. Or open a new window and clone `https://github.com/jensfossen/ez-ai-academy` again.
- **Personal or project skills folder:** run `git pull` inside the installed `ai-academy` directory.
- Start a new chat (or type `/` and choose `ai-academy`, `ez-ai-academy`, or `start` again) so the mentor loads the new `SKILL.md`.
- What changed for learners: [`content/RELEASE_NOTES.md`](../../content/RELEASE_NOTES.md). Updating is optional and never required to finish a lesson you already started.

## Cursor IDE chat vs Cloud Agent

These are different surfaces. Do not treat a Cloud Agent result as an IDE native-UI Pass. Rich-UI work is tracked in [#24](https://github.com/jensfossen/ez-ai-academy/issues/24). Research notes and **Skill wiring** (ask-questions when attached): [`RICH_UI.md`](RICH_UI.md).

**Cursor IDE chat** is the reference surface. Prefer the host ask-questions picker when the host attaches it (Plan Mode family; forum/host alias AskQuestion), and in-chat video when the IDE can play a lesson link. Neither is a published skill-author API, and the picker is not guaranteed in every Agent chat — details in [`RICH_UI.md`](RICH_UI.md). Do not invent private markup. If a native control is missing, use the Markdown numbered-list and link fallbacks.

**Cursor Cloud Agent** uses Markdown fallbacks only. Cloud Agents may load `SKILL.md` from a checkout of this repository, or from a personal install after enabling **Settings → Agents → Sync Skills**. Cloud Agent chat uses numbered-list choices (native tappable cards are unavailable). Offer lesson video as an external link plus the text alternative; in-chat playback is not available. Image acceptance is a markdown image plus alt text, or a meaningful description; inline raster display is UI-dependent and not guaranteed.

## Slash commands (checkout)

When this repository is open in Cursor, Agent discovers:

- `/ai-academy` from the repository-root `SKILL.md` (`name: ai-academy` — canonical skill id). A personal install at `~/.cursor/skills/ai-academy` also registers this command (folder name matches).
- `/ez-ai-academy` from [`.cursor/skills/ez-ai-academy/SKILL.md`](../../.cursor/skills/ez-ai-academy/SKILL.md)
- `/start` from [`.cursor/skills/start/SKILL.md`](../../.cursor/skills/start/SKILL.md)

Cursor lists project skills from `.cursor/skills/<name>/SKILL.md` as `/<name>` (`name` must match the folder). The alias files only tell the mentor to read the root skill and run **Start a learning journey** (or restore from a pasted `AI_ACADEMY_RECORD`). They do not fork curriculum. This is not a harness Pass.

Source: [Cursor — Agent Skills](https://cursor.com/docs/skills) (project skills in `.cursor/skills/`). Last verified 2026-09-10. IDE ask-questions and in-chat-video research remains open on [#24](https://github.com/jensfossen/ez-ai-academy/issues/24).
