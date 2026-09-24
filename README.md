# The Unofficial Guide

<!-- Replace this line with your name and which corpus you picked. -->

> **This file is your submission.** Fill it in as you go — most sections get
> written during the milestone that produces them, not at the end.
>
> How the starter works, and every command you'll need, is in `RUNNING.md`.
> Leave that file alone.
>
> **Paste everything as text.** No screenshots, no video. A typed table gets
> full credit; a picture of the same table gets none.
>
> Delete these instruction blocks as you replace them. The `<!-- -->` comments
> are notes to you and don't show up when the page renders — you can leave them
> or remove them.

---

# Unit 1

## What This Does

I picked the campus life corpus. It contains short student posts about dorms, dining halls, classes, rules, so the system is meant to answer practical campus questions like where to do laundry, how meal plan changes work.

The goal is to retrieve the relevant campus life document and answer with a clear fact plus a source.

## Chunking Strategy

**Chunk size:** 800 characters
**Overlap:** 120 characters

I kept the default chunker for Unit 1 because the campus life documents are mostly short posts, often one paragraph and useful facts are usually contained in a single sentence. A chunk size that large is not harmful here because most pages are short enough to stay intact. The overlap helps keep adjacent facts from being split apart when a sentence crosses a boundary.

## Sample Chunks

**Chunk 1** — source: admin_add_drop_deadline.txt#0 — produced by: chunker.py::fallback_split

```
On the add/drop deadline

You can add a course through the end of the second week. Dropping is a longer window — through the end of week six — but a drop after week two shows as a W on your transcript. Nothing anywhere on the registrar's site says this plainly, and students find out from each other.
```

**Chunk 2** — source: `course_biol_160.txt#0` — produced by: `chunker.py::fallback_split`

```
BIOL 160 Cell Biology

I lived here my sophomore year. Format is lecture three times a week with a weekly lab. Assessment: four unit tests and a cumulative final. Not curved.

Expect 9 to 11 hours a week, the heaviest first-year course by reputation.

The one piece of advice: the unit tests come fast, roughly every three weeks; falling behind once is very hard to recover from.
```

**Chunk 3** — source: `course_hist_118_workload.txt#0` — produced by: `chunker.py::fallback_split`

```
Workload for HIST 118 Modern World History

People keep asking so: a lot of reading, about 120 pages a week, but no problem sets. That's real time, not optimistic time.

It's front-loaded — the first month is heavier than the rest, partly because you're learning the format.
```

**Chunk 4** — source: `dining_pellew_dining_hall_followup.txt#0` — produced by: `chunker.py::fallback_split`

```
Re: Pellew Dining Hall

Adding to what people have said about Pellew Dining Hall. The wait figure of 12 to 18 minutes at peak matches what I've seen. If you're trying to eat between classes, go before 11:45 and it's a different building entirely.

Also worth saying: the furthest hall from anywhere, next to the athletics centre. Nobody tells you this at orientation.
```

**Chunk 5** — source: `housing_innisfree_hall.txt#0` — produced by: `chunker.py::fallback_split`

```
Innisfree Hall — what it's actually like

Transferred in last year, so take this with a grain of salt. Built 1991, renovated 2022. Rooms are doubles arranged as pairs sharing one bathroom between two rooms.

The good: the shared-bathroom-between-two-rooms arrangement is the best compromise on campus.

The bad: no air conditioning, which matters for the first three weeks of September.

Laundry costs $1.75 wash, $1.75 dry, app-based. On noise: moderate; the building is L-shaped and the short wing is much quieter.
```

## Sample Answer

**Question:** What are the laundry prices in Innisfree Hall?

**Answer:**

```
Laundry in Innisfree Hall costs $1.75 to wash and $1.75 to dry.

Source: housing_innisfree_hall_laundry.txt (also mentioned in housing_innisfree_hall.txt)
```

**My relevance cutoff:** 0.6

I measured the best distance for five in-corpus questions and five out-of-scope questions. The in-corpus distances stayed between about 0.25 and 0.31, while the out-of-scope questions were all above 0.82, so 0.6 creates a clear gap and correctly refuses unrelated questions without rejecting the corpus questions.

| Question | In corpus? | Best distance |
|---|---|---|
| Is the housing lottery random for everyone? | Yes | 0.2572 |
| What are the laundry prices in Innisfree Hall? | Yes | 0.2542 |
| When can students change their meal plan? | Yes | 0.2788 |
| When is the best time to do laundry in Aldridge Hall? | Yes | 0.3021 |
| Can a student declare an out-of-major course pass/fail after midterms? | Yes | 0.3085 |
| What is the capital of Mongolia? | No | 0.8246 |
| How do I change the oil in a diesel engine? | No | 0.9340 |
| Who won the 1994 World Cup? | No | 0.8859 |
| What is the recommended dosage of ibuprofen for a headache? | No | 0.8442 |
| How do I write a for loop in Rust? | No | 0.8960 |

## How I Used AI

**1.** I asked for help comparing short-post campus documents to long guide documents and for a quick sense of what a chunking strategy should optimize. The answer suggested paragraph-aware splitting, but I checked the actual `campus_life` files and kept the default 800/120 setup because in this corpus the useful facts already sit inside one short paragraph or sentence, so preserving complete thoughts mattered more than aggressive splitting.

**2.** I asked for help interpreting the best-distance numbers from retrieval before choosing a relevance threshold. The first suggestion was too aggressive and would have rejected too many good matches; after comparing the in-corpus and out-of-scope values side by side, I set the cutoff at 0.6 because it cleanly occupied the gap between the two groups.

---

---

# Unit 2

<!-- These sections get ADDED to what's already above. Don't delete or rewrite
     unit 1 — the point is that someone can see what you said before you knew
     how it went. -->

## Run Log — Before

<!-- Your five criteria, three runs each. `python run_eval.py --label before`
     runs the questions, puts the OUT_OF_SCOPE ones through the gate, and
     writes it all into results/ for you. Targets come from criteria.md; the
     verdict column is your call.

     Criterion 3 is measured in one deterministic pass rather than three, so
     the same number goes in all three run columns. That's correct, not lazy.

     Milestone 1. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunks contain the answer | 4 of 5 | 5 of 5 | 5 of 5 | 5 of 5 | MET |
| 2. Every answer names a source | 5 of 5 | 5 of 5 | 5 of 5 | 5 of 5 | MET |
| 3. Gate stops out-of-corpus questions | 4 of 5 | 5 of 5 | 5 of 5 | 5 of 5 | MET |
| 4. Sampled chunks are complete thoughts | 4 of 5 | 5 of 5 | 5 of 5 | 5 of 5 | MET |
| 5. Cited sources contain the supporting facts | 5 of 5 | 5 of 5 | 5 of 5 | 5 of 5 | MET |

<!-- Underneath, paste the REAL output for each criterion from one of your
     runs — the actual text your system produced, not a description of it.
     Name the file and function that produced it. -->

Evidence from `results/run_2026-09-23_1738.md`, produced by
`run_eval.py::main` and `run_eval.py::check_out_of_scope`:

- Criterion 1: the retrieved sources included `admin_housing_lottery.txt`,
     `housing_innisfree_hall.txt`, `admin_meal_plan_changes.txt`,
     `housing_aldridge_hall_laundry.txt`, and `admin_pass_fail_option.txt`, which
     contain the answers to the five in-scope questions.
- Criterion 2: representative generated output was:

     ```
     In Innisfree Hall, laundry costs $1.75 to wash and $1.75 to dry.

     Source: housing_innisfree_hall.txt (also found in housing_innisfree_hall_laundry.txt)
     ```

- Criterion 3: `run_eval.py::check_out_of_scope` reported `Refused 5 of 5`.
     The best distances were 0.825, 0.934, 0.886, 0.844, and 0.896, all above
     the 0.6 cutoff.
- Criterion 4: the five sampled chunks in Unit 1 each preserved a complete
     thought and were produced by `chunker.py::fallback_split`.
- Criterion 5: the generated answers cited source documents containing the
     supporting facts, including `admin_housing_lottery.txt`,
     `housing_innisfree_hall.txt`, `admin_meal_plan_changes.txt`,
     `housing_aldridge_hall_laundry.txt`, and `admin_pass_fail_option.txt`.

## Verdicts

<!-- MET or MISSED for each of the five, against the target you wrote last
     unit — not a new one. Plus a sentence on how you decided. That sentence
     matters most where it was close.

     If your target said 4 of 5 and your runs came out 4, 3, 4, that's a MISS.
     The target has to hold, not show up occasionally.

     Milestone 2. -->

| # | Criterion | Verdict | How I decided |
|---|---|---|---|
| 1 | Retrieved chunks contain the answer | MET | The retrieved source lists included the document containing the answer for all five in-scope questions, so the 4-of-5 target was met in every run. |
| 2 | Every answer names a source | MET | Each generated answer in the baseline transcript included a source filename, meeting the 5-of-5 target. |
| 3 | Gate stops out-of-corpus questions | MET | The relevance gate refused all five out-of-corpus questions, exceeding the target of 4 of 5. |
| 4 | Sampled chunks are complete thoughts | MET | All five Unit 1 samples were readable complete thoughts without a sentence cut at either end. |
| 5 | Cited sources contain the supporting facts | MET | The cited documents contained the facts used in all five answers, meeting the 5-of-5 target. |

## Diagnoses

<!-- For each miss: which stage caused it, and how. The stage alone isn't
     enough — you need the mechanism.

     Not a diagnosis: "Question 3 didn't work."
     A diagnosis:     "Question 3 asks about laundry costs. The answer is in
                       one sentence that got split across two chunks, so
                       neither chunk on its own contains it."

     The five stages: loading → chunking → embedding → retrieval → generation.

     Look for a pattern. If three misses all ask about numbers, that's one
     problem, not three.

     Missed nothing? Say so, then say honestly whether your targets were set
     low, and which one you'd tighten and to what.

     Milestone 3. -->

No criterion was missed in the baseline evidence, so there is no failure to
assign to loading, chunking, embedding, retrieval, or generation. The weakest
target is criterion 1: the five questions all retrieved useful source
documents, but the target allowed one of five questions to fail. I would
tighten it to 5 of 5 for the next evaluation because these questions ask for
specific facts that are present in the corpus.

## The Improvement

**What I changed:**

**Why I picked it:**

<!-- Connect it to a specific diagnosis above in one sentence. If you can't,
     you picked a fix because it sounded impressive. -->

### Run Log — After

<!-- Same format, same five criteria, three runs each.
     `python run_eval.py --label after` -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 |  |  |  |  |
| 2. Every answer names a source | 5 of 5 |  |  |  |  |
| 3. Gate stops out-of-corpus questions | 4 of 5 |  |  |  |  |
| 4. | | | | | |
| 5. | | | | | |

**Did it help?**

<!-- Say plainly whether it did, and how you know. If it made things worse,
     say that — a change that backfired, honestly reported, earns full credit
     and is more interesting than one that worked. What matters is that you can
     tell.

     Milestone 4. -->

## What's Still Broken

<!-- For each criterion still missed after your fix: what you'd do about it,
     and why you stopped where you did.

     "I ran out of time" is fine if it's true. Pretending nothing is left is
     not.

     Milestone 5. -->

## What I'd Do Differently

<!-- Knowing what you know now — which of your five criteria would you write
     differently, and why?

     Milestone 5. -->
