# Acceptance criteria — The Unofficial Guide

Five criteria that say what "working" means for this system, written in unit 1
**before** any results existed.

An acceptance criterion names a target: a number, a count, a rate, or something
a person could plainly observe. *"Retrieval works"* is an opinion. *"For at
least 4 of my 5 test questions, the top results include a chunk containing the
answer"* is a criterion.

Under each one, write a sentence or two on **why that target** and not a
stricter or looser one. A reason that says something about your corpus or your
pipeline earns credit; *"80% seemed reasonable"* does not.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

---

## 1. Retrieved chunks contain the answer

For at least 4 of my 5 test questions, the retrieved chunks include one that
contains the answer.

**Why this target:**
The five questions cover different parts of the campus-life corpus, and each
asks for a specific fact rather than a broad opinion. I allow one miss because
retrieval can still struggle with a less common phrase, but four successful
questions would show that the index is useful for the main test set.

---

## 2. Every answer names a source

Every answer the system produces names at least one source document.

**Why this target:**
The answer pipeline receives the source filename with every retrieved chunk,
and the questions are all grounded in the indexed corpus. Naming a source for
all five answers should therefore be achievable; a missing source would point
to an answer-format or generation problem rather than a lack of documents.

---

## 3. The relevance gate stops out-of-corpus questions

When I ask a question my documents clearly don't cover, the relevance gate
stops it and the system returns "I don't have enough information about that" —
in at least 4 of 5 tries.

<!-- The five questions are the ones in `OUT_OF_SCOPE` at the bottom of
     `questions.py`, and `run_eval.py` puts them through the gate and writes
     what happened into your run log. Swap them for your own if you'd rather —
     just keep five of them, or the "4 of 5" above has nothing to be 4 of. -->

**Why this target:**
The out-of-scope questions are about unrelated topics such as Mongolia, Rust,
and engine maintenance, while the selected corpus is about university life.

---

## 4. Something about your chunks

At least 4 of 5 sampled chunks will read as a complete thought, with no
sentence cut in half at either end.



**Why this target:**
The campus-life documents are mostly one to three short paragraphs, and useful
information often sits in a single sentence. Preserving complete thoughts is
more important here than forcing every chunk to reach the configured character
limit, while allowing one imperfect sample accounts for an occasional boundary
case.


---

## 5. Your choice

For all 5 in-scope questions, the cited source document will contain the fact
used to support the answer, not merely be a document returned by retrieval.



**Why this target:**
Source names are useful only when they let a reader verify the answer. The
questions each ask for a concrete fact, so checking the cited document is
possible; requiring all five keeps attribution reliable across the full test
set rather than accepting plausible-looking but unsupported citations.


---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 2 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath it, like this:

         ## 1. Retrieved chunks contain the answer

         For at least 4 of my 5 test questions, the retrieved chunks include
         one that contains the answer.

         **Why this target:** ...

         > **Revised in unit 2:** For at least 4 of 5 questions, the top three
         > results contain the answer.
         >
         > **Why revised:** I couldn't judge "the chunks include one that
         > contains the answer" the same way twice — I scored two questions
         > differently on Monday than on Wednesday. The new version is
         > something I can actually check.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "I said 4 of 5 but got 2 of 5, so 2 of 5 is more realistic."

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.

     The whole reason the originals stay visible is so someone can see what you
     said before you knew the answer.
     ───────────────────────────────────────────────────────────────────────── -->
