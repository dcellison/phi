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

let result = "";
for (entry in input) {
    let pos = input[entry];
    if (pos in swap) {
        result += `${swap[pos]}, `;
    }
}

if (result.length == 0)
    return "> [!WARNING] WARNING\n" +
           "> Missing part of speech tag " +
           "e.g. \"noun\", \"verb\".";
return(`*${result.slice(0, -2)}*`);