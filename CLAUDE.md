# CLAUDE.md

Instructions for Claude when working in this repository.

## What this repo is

Released artifacts for the paper *Capability Is Not Deployability: The Office of
the CFO as a Distinct, Under-Benchmarked Domain for AI Agents*. Every number in
the paper must be derivable from the files here. See `README.md` for the file
map and `protocol.md` for the registered protocol.

The FinNLP 2026 submission was rejected (scores 7/6/6/6/4). The repo is now in
revision for resubmission. The review points are tracked in Linear and the
reasoning is documented in Notion, as described below.

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

Before first use in a session, confirm which Linear team/project and Notion
parent page to use (ask the user once; do not guess). Record the answer below
and keep this file updated:

- Linear team: `TODO: fill in`
- Linear project: `Resubmission: CFO-office agent coverage` (create if missing)
- Notion parent page: `TODO: fill in`

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
- **Parent issue** per rejection round (`Revision after FinNLP 2026 reject`)
  with sub-issues for each item.
- **Status flow:** Backlog -> Todo -> In Progress -> In Review -> Done. Move an
  issue to Done only after `recount.py` passes on the final commit.
- Reference the issue ID in branch names and commit messages
  (`ABC-12: resolve screening records 1-24`).
- Comment on the issue when a decision changes scope. Do not close issues for
  work that was skipped; mark them Canceled with the reason.

### Seed backlog from the reviews

| Issue | Label | Priority | Raised by |
|---|---|---|---|
| Clarify applicability of the four dimensions by agent type and use one wording (required/default/minimum) | governance-rule | High | 7xVT, BgC8, W11j, wcr8 |
| Resolve the 48 unresolved screening records and recount | search-recall | High | B5gB, 7xVT, BgC8, wcr8 |
| Human second coder on a sample; document coding procedure and coder context | coding-validity | High | B5gB, wcr8, 7xVT |
| Cut and refocus the manuscript; lead with the decision rule and empty cells | writing | Medium | W11j, B5gB |
| Re-check taxonomy against current APQC PCF version | taxonomy | Medium | BgC8 |
| Merge contribution 3 into 1 and 2 | writing | Low | B5gB |
| Argue why CFO-specific; note whether four dimensions are sufficient | governance-rule | Low | wcr8 |
| (Optional) Build a runnable tax-provision benchmark task | benchmark-build | Medium | W11j |
| Choose resubmission venue | admin | Medium | self |

## Notion conventions

**Create pages only for durable content, and say where you created them.** If
no parent page is given, create a private draft and tell the user.

Maintain this structure under the parent page:

1. **Revision hub**: one page with the review scores, the themes table above,
   and links to each Linear issue.
2. **Decision log**: one entry per decision, newest first. Each entry has
   *Date, Decision, Alternatives considered, Reason, Linked issue, Linked
   commit*. Log scope choices, taxonomy changes, inclusion rulings and any
   claim that was weakened.
3. **Review responses**: one page per reviewer with the verbatim point, our
   response, and what changed in the paper (section and line).
4. **Protocol changelog**: mirrors deviations recorded in `protocol.md`. The
   repo file is authoritative; Notion explains the reasoning.
5. **Venue notes**: deadlines, page limits, track fit, reviewer norms for each
   candidate venue.

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
