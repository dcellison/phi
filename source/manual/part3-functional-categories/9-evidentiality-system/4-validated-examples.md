# Validated Examples

> All examples in this file have been tested and validated using phi's comprehensive validation system.

## Complete Example Library

### Direct Evidence (`hi`)

Examples where the speaker has direct sensory access to the information:

```
hi ne riwhea ta whuru.
DIR inanimate wind present blow
"The wind is blowing." (I can see/feel it directly)
```

```
hi mia ta whemo.
DIR I present think
"I am thinking." (I have direct access to my own thoughts)
```

### Inference (`ro`)

Examples where the speaker deduces information from available evidence:

```
ro he thephoa ta phoni.
INF human person present live
"A person lives." (I can see signs of habitation)
```

```
ro ne raoshea ta waphe phera.
INF inanimate sun present warm is
"The sun is warm." (I can see its effects, feel the heat)
```

### Hearsay (`nu`)

Examples where the speaker has heard information from unspecified sources:

```
nu he thephoa na ne lophui li whesa.
HEAR human person object inanimate art past create
"A person created art." (I heard this from various people)
```

```
nu he thephoa ta whemo.
HEAR human person present think
"A person thinks." (People told me this about someone)
```

```
nu sha na ne noshea li theso.
HEAR they object inanimate food past cook
"They cooked food." (I heard this happened)
```

### Reported Speech (`ti`)

Examples where the speaker attributes information to a specific source:

```
ti he nowhea li shuso mia ta whera.
REP human teacher past say I present learn
"The teacher said I am learning." (Direct quotation/report)
```

```
ti mia li shuso thi ta whera.
REP I past say you present learn
"I said you are learning." (Reporting my own past statement)
```

### Memory (`mu`)

Examples where the speaker recalls information from personal memory:

```
mu mia na ne raoshea li whona.
MEM I object inanimate sun past look
"I looked at the sun." (I remember doing this)
```

```
mu he phiphea li whera.
MEM human child past learn
"The child learned." (I remember witnessing this)
```

### Presumption (`pe`)

Examples where the speaker makes assumptions based on general knowledge:

```
pe ne lashea su whale.
PRES inanimate rain future flow
"It will rain." (Based on weather patterns/expectations)
```

```
pe pi mathai su whuwe.
PRES animate cat future sleep
"The cat will sleep." (This is what cats typically do)
```

## Validation Status

✅ **All examples validated**: These examples have been tested using the 
`test_evidentiality_examples.py` script and confirmed to be grammatically correct.

✅ **Lexicon compliance**: All words have been verified against the authoritative 
phi lexicon using `phi_lexicon_reader.py`.

✅ **Phonotactic compliance**: All words follow proper phi phonotactic patterns 
as verified by `phi_validator.py`.

## Testing Framework

To verify these examples yourself:

```bash
cd source/
python test_evidentiality_examples.py
```

This will run all examples through the comprehensive validation system and 
report any issues.

## Usage Guidelines

### Context Selection

Choose evidentials based on your actual knowledge source:

- Use `hi` only when you have direct sensory evidence
- Use `ro` when you're making logical deductions
- Use `nu` for information from general "word of mouth"
- Use `ti` when you can cite a specific source
- Use `mu` when recalling past direct experiences
- Use `pe` when making educated assumptions

### Register Considerations

- **Formal contexts**: Evidentials are typically required
- **Informal contexts**: May be omitted for brevity
- **Academic/legal writing**: Precision is highly valued

### Common Patterns

- **Narrative**: Mix of `mu` (memory) and `hi` (direct) for personal stories
- **News reporting**: Frequent use of `ti` (reported) and `nu` (hearsay)
- **Scientific writing**: Heavy use of `ro` (inference) and `ti` (cited sources)
- **Weather reports**: Often `pe` (presumption) for predictions

---

*These validated examples form the foundation for understanding phi's evidentiality system in practice.* 