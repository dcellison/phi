let result = "*";
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
        result += (swap[pos] + " ");
    }
}

if (result.length == 1) return "";

return(result.slice(0, -1) + "*");
