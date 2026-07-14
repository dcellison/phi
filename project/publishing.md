# Publishing Phi: The Vision and the Order of Operations

*Recorded 2026-07 from a planning conversation. The goal: the manual and the primer as physical books people can buy and learn from. This document is the strategy — what makes it plausible, what the real risk is, and what has to happen in what order.*

## Why this is plausible

There is direct precedent. Toki Pona — one person's small, philosophical constructed language — was published as a modest official book and has sold steadily for over fifteen years, sustained by a community that formed around free online materials first. *Lingua Latina per se illustrata*, the primer's methodological model, has sold continuously since 1955. Language books of this kind are not bestsellers; they are perennials. Graded readers and well-made grammars age well, and a small, passionate audience that replenishes itself is a better fate than most books get.

## The real risk, reframed

The worry is books stagnating on shelves. Books stagnate when the shelf is the first touchpoint — when the book has to introduce the language to a stranger. They do not stagnate when they are the physical artifact of something people already do. For a niche like this, marketing is not advertising; it is the existence of a community before the book exists. Nobody buys a book for a language no one speaks. People buy the beautiful print edition of a language they have already fallen for online.

So the funnel is already mostly built, and it is free by design: the web explorer for wandering the lexicon, the primer readable online, curious people working through chapter one and wanting more. The book is not the introduction to Phi. It is the keepsake for people the website already converted.

## The first domino has fallen

Phi is now public. The repository is open, GitHub Pages builds the site from every merge to `main`, and the explorer and primer are available at [dcellison.github.io/phi](https://dcellison.github.io/phi/).

Public access removes the technical gate, but it does not supply recurring readers. Community, audience, and print still depend on use rather than availability alone.

## Two structural advantages

**The object.** In this niche, the physical book sells as an object. People buy gorgeous language and writing-system books who will never learn the contents. Phi's owner is a graphic designer, and the design language already exists: Art Nouveau by principle, Fraunces and Gentium, bone paper and green-black ink, one vine of ornament. A print manual in that dress gets bought for its beauty and read for its ideas.

**The angle.** Phi has a positioning no other conlang holds cleanly: a language designed to make you slow down. That pitch reaches meditation, mindfulness, and slow-living readers who would never visit a conlang forum. The mindfulness angle is the bridge out of the niche, and it is not marketing spin — it is literally the design brief the language was built to.

## Production: one source of truth, in print too

The repo is already the single source of truth, validated in CI. The print pipeline should compile from the same files: Markdown to typeset pages (Typst or LaTeX, the same font families as the web), so that web, print, and canon cannot diverge. The manual cannot drift from the lexicon because they build from the same place. This pipeline is buildable now and can be exercised long before any ISBN exists — a beautiful PDF is also a fine intermediate artifact.

## The order of operations

1. **Finish the primer.** Complete: the graded chapters and capstone are published on the site.
2. **Make the hosting call.** Complete: the public repository deploys to GitHub Pages.
3. **Let the community form** around the free material. This is the marketing. It cannot be rushed and does not need to be.
4. **Build the print pipeline** from the repo when the material stabilizes; circulate the PDF.
5. **Print** when there are people waiting for the object, with the book as keepsake rather than introduction.

The sequence now waits at the third step: recurring use.
