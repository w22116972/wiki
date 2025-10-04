# Google Technical Writing Guide

## Table of Contents
- [Choice of words](#choice-of-words)
  - [Choose strong verbs](#choose-strong-verbs)
  - [Use `following` to introduce list or table](#use-following-to-introduce-list-or-table)
  - [Use imperative verbs first in numbered list](#use-imperative-verbs-first-in-numbered-list)
  - [Prefer active voice to passive voice](#prefer-active-voice-to-passive-voice)
- [Rewriting sentences](#rewriting-sentences)
  - [Convert some long sentences to lists](#convert-some-long-sentences-to-lists)
  - [Minimize certain adjectives and adverbs](#minimize-certain-adjectives-and-adverbs)
  - [Reduce there is/are](#reduce-there-isare)
  - [Reduce extraneous words](#reduce-extraneous-words)
  - [Place conditions before instructions, not after](#place-conditions-before-instructions-not-after)
- [Structure](#structure)
  - [Effective opening sentence in any paragraph](#effective-opening-sentence-in-any-paragraph)
  - [Focus each paragraph on a single topic + Focus each sentence on a single idea](#focus-each-paragraph-on-a-single-topic--focus-each-sentence-on-a-single-idea)
  - [Note: which vs that in subordinate clauses](#note-which-vs-that-in-subordinate-clauses)
- [References](#references)

## Choice of words

### Choose strong verbs
Reduce imprecise, weak, generic verbs
- be: is, are... (Not always bad)
  - (X) We ~~are~~ very careful to **ensure**...
  - (O) We carefully ensure...
- occur
  - (X) The error ~~occurred~~
  - (O) The error **crashed** the system
- have/has
  - (X) When a variable declaration doesn't ~~have~~ a datatype
  - (O) When a variable declaration doesn't **specify** a datatype
- happen
  - (X) This error message ~~happens~~ when...
  - (O) The system **generates** this error message when...

### Use `following` to introduce list or table

(O) The following table contains the...

### Use imperative verbs first in  numbered list

(O) The steps to create a new project are:
1. **Open** the project
2. **Click** the New button
3. **Enter** the project name

### Prefer active voice to passive voice

No examples.

---
## Rewriting sentences

### Convert some long sentences to lists
- (X) To alter the usual flow of a loop, you may use either a **break** statement (which hops you out of the current loop) or a **continue** statement (which skips past the remainder of the current iteration of the current loop)
- (O) To alter the usual flow of a loop, call one of the following statements:
  - A **break** statement hops you out of the current loop
  - A **continue** statement skips past the remainder of the current iteration of the current loop

### Minimize certain adjectives and adverbs

- (X) Setting this flag makes the application run **screamingly** fast.
- (O) Setting this flag makes the application run **225-250%** faster

### Reduce there is/are

- (X) **~~There is~~** a variable called `met_trick` that stores the current accuracy.
- (O) The variable `met_trick` stores the current accuracy.
- (X) **T~~here is~~** no guarantee that the updates will be received in sequential order.
- (O) Clients might not receive the updates in sequential order.
- (X) **~~There is~~** no creator stack for the main thread.
- (O) The main thread does not provide a creator stack.

### Reduce extraneous words

- (X) provides a detailed description of → (O) describes
- (X) at this point in time → (O) now
- (X) determine the location of → (O) find
- (X) is able to → (O) can

### Place conditions before instructions, not after.

- (X) See [link to other document] for more information.
- (O) For more information, see [link to other document].

- (X) Click Delete if you want to delete the entire document.
- (O) To delete the entire document, click Delete.

---

## Structure

### Effective opening sentence in any paragraph.

Opening sentence is theme of paragraph.

### Focus each paragraph on a single topic + Focus each sentence on a single idea

A paragraph should represent an independent unit of logic. Don't describe what will happen in a future topic or what happened in a past topic.

**Reduce subordinate clause if it didn't extend the single idea but branch off into a separate idea.**

- (X) The late 1950s was a key era for programming languages because IBM introduced Fortran in 1957 and John McCarthy introduced Lisp the following year, which gave programmers both an iterative way of solving problems and a recursive way.
- (O) The late 1950s was a key era for programming languages. IBM introduced Fortran in 1957. John McCarthy invented Lisp the following year. Consequently, by the late 1950s, programmers could solve problems iteratively or recursively.

### Note: which vs that in subordinate clauses

- which: nonessential subordinate clauses
- that: essential subordinate clause that the sentence can't live without

Example
- Python is an interpreted language, which Guido van Rossum invented.
- Fortran is perfect for mathematical calculations that don't involve linear algebra.

If you read a sentence aloud and hear a pause just before the subordinate clause, then use `which` .

---
## References

- https://developers.google.com/tech-writing
- https://developers.google.com/style

