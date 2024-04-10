let result = [];
let swap = {
    "noun": "n.",
    "verb": "v.",
    "adjective": "adj.",
    "adverb": "adv.",
    "pronoun": "pron.",
    "preposition": "prep.",
    "conjunction": "conj.",
    "interjection": "interj.",
}

for (entry in input) {
    let pos = input[entry];
    if (pos in swap) {
        result.push(swap[pos]);
    }
}

return(result);
