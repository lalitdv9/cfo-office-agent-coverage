# CLAUDE.md

Instructions for Claude when working in this repository.

## What this repo is

Released artifacts for the paper *Capability Is Not Deployability: The Office of
the CFO as a Distinct, Under-Benchmarked Domain for AI Agents*. Every number in
the paper must be derivable from the files here. See `README.md` for the file
map and `protocol.md` for the registered protocol.

An earlier version was reviewed and not accepted. The reviewers' points are
tracked in Linear and the reasoning is recorded in Notion; use those, do not
recreate them (see below).

## Ground rules (apply to all work)

1. **Run `python3 recount.py` before and after any change** to a CSV, a note or
   a count. It must exit 0 or the paper and data disagree. If a change makes it
   fail on purpose (for example resolving screening records), update the script
   and the manuscript numbers together and say so in the commit.
2. **Never invent evidence.** Every coded cell needs an exact quotation and
   section in `notes/`. If a paper cannot be read in full, mark it pending; do
   not code it from the abstract.
3. **Date every negative claim** ("no dedicated benchmark identified as of
   <month year>"). When the search window moves, update the date everywhere.
4. **Keep AI-assisted work disclosed.** Search, screening and coding done by
   Claude must be recorded in `protocol.md` (what was done, what context the
   coder saw). A human second coder is still owed (see Linear).
5. **No model identifiers** in commits, notes, file contents or tracker items.
6. Edit CSVs by script or careful diff, never by hand-reformatting the file.

## Where things are tracked

| Need | Tool | Why |
|---|---|---|
| Work to do, status, owners, deadlines | **Linear** | One issue per unit of work, with a clear done-state |
| Reasoning, decisions, long-form writing, meeting notes | **Notion** | Durable, searchable, shareable prose |
| Data, code, protocol, evidence notes | **This repo (git)** | The source of truth for results |

Rule of thumb: if it has a "done" state, it is a Linear issue. If it explains
*why*, it is a Notion page. If it is a result, it lives in git. Link all three
to each other; never copy content between them.

This project already exists in both tools. **Find and update the existing items;
never create a parallel project, page or duplicate issue.**

- Linear: the current project is `CFO-office paper — resubmission round 2`
  (find it with `list_projects`). The earlier round's project is archived; do
  not edit it.
- Notion: the round-2 decision log, found by searching
  `resubmission round 2: decision log`.
- Status (2026-10-06): the resource-paper path was chosen. The open items are
  tracked as issues in the round-2 project; read them before starting work.
- **Keep private matters out of this repo.** This repo is public and is
  mirrored anonymously for reviewers. The tracker workspaces also hold
  unrelated items: never copy them into commits, `CLAUDE.md`, notes or any
  released file, never paste issue IDs or tracker names into released files,
  and do not read unrelated items.
- **The manuscript source stays out of this repo** (`paper/` is gitignored) so
  that double-blind review is not compromised.

## Linear conventions

**Create or update issues only when the user asks or the task clearly calls for
it. Search first (`list_issues`) to avoid duplicates.**

- **One issue per review point or work unit**, titled with a verb:
  `Resolve 48 unresolved screening records`, not `Search recall`.
- **Description template:**
  - *Why* (quote the reviewer point or limitation, name the reviewer)
  - *Done when* (checkable acceptance criteria, usually "`recount.py` passes
    and paper numbers updated")
  - *Files touched* (paths in this repo)
  - *Links* (Notion page, commit or PR)
- **Labels:** `search-recall`, `coding-validity`, `taxonomy`, `governance-rule`,
  `writing`, `benchmark-build`, `admin`.
- **Priority** follows how many reviewers raised it: 4 reviewers = Urgent/High,
  2 = Medium, 1 = Low.
- **Parent issue** per rejection round (e.g. `Revision round N`)
  with sub-issues for each item.
- **Status flow:** Backlog -> Todo -> In Progress -> In Review -> Done. Move an
  issue to Done only after `recount.py` passes on the final commit.
- Reference the issue ID in branch names and commit messages
  (`ABC-12: resolve screening records 1-24`).
- Comment on the issue when a decision changes scope. Do not close issues for
  work that was skipped; mark them Canceled with the reason.

## Notion conventions

**Create pages only for durable content, and say where you created them.** If
no parent page is given, create a private draft and tell the user.

Update the existing paper page rather than creating new structure. Put
decisions and their reasons there (date, decision, alternatives, reason, linked
Linear issue, linked commit). Only add a child page when content is too long for
the row, such as a per-reviewer response page or venue notes. If the user wants
a fuller hub, propose it first.

Page rules:
- Start every page with a one-line summary, then the date and last editor.
- Link to the Linear issue and to the repo path or commit, never paste data.
- Update the existing page rather than creating a near-duplicate; search first.

## Workflow for a typical task

1. Find or create the Linear issue; set it In Progress.
2. Read the relevant Notion decision-log entries so past rulings are respected.
3. Do the work in the repo on the designated branch; run `recount.py`.
4. Commit with the issue ID. Do not open a PR unless asked.
5. Add a Decision-log entry in Notion if any scope, claim or number changed.
6. Comment on the Linear issue with the commit link and move it to In Review.

## Safety and etiquette

- Linear and Notion posts are visible to others. Confirm with the user before
  posting to shared spaces, sending messages, or deleting anything.
- Never paste credentials, tokens or private reviewer correspondence beyond
  what the user supplied for this project.
- If Linear or Notion access fails (not authorized), say so plainly and keep
  the content in a local markdown draft under the repo instead of dropping it.
- Report outcomes faithfully: if `recount.py` fails or a step was skipped,
  say that in the issue comment.
