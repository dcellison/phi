# phonotactics

## groups

| group | pattern
| ----- | -------
| C     | `h/l/m/n/p/s/t/w`
| B     | `pl/tw/sp/st/sl/sw/`
| F     | `ph/th/sh/wh`
| V     | `a/e/i/o/u`
| D     | `[VV]^aa^ee^ii^oo^uu`

## word patterns

### nouns

* this pattern produces soft words of two to four syllables. it gives nouns a
  more airy feel.
* for words that extend an existing verb, half of this pattern can be combined
  with the verb. so if we have a verb `tenu` it could be combined with a noun
  segment: `shuotenu`. the first part retains the noun formatting.

`[F][V/D][F][V/D]`
examples:
```
thuwhio whowhe whoathi phushu thaphoi whiwhu phiathie whepheo thishui whusheo
```

### verbs

* this pattern produces words of two to three syllables. these words include
  plosives and blends, reflecting that verbs are more utilitarian.

`[C/B/F][V/D][C/F][V]`
examples:
```
thishe tenu shiota shuso plewha pleosho phiule potha thunu phowhe plawhi suile
```

### parts of speech

* these words will be used for everything else in the language, like particles,
  pronouns, or prepositions.

`[F][D]`
```
phae phai phao phau phea phei pheo pheu phia phie
phio phiu phoa phoe phoi phou phua phue phui phuo
shae shai shao shau shea shei sheo sheu shia shie
shio shiu shoa shoe shoi shou shua shue shui shuo
thae thai thao thau thea thei theo theu thia thie
thio thiu thoa thoe thoi thou thua thue thui thuo
whae whai whao whau whea whei wheo wheu whia whie
whio whiu whoa whoe whoi whou whua whue whui whuo
```

`[C][D]`
```
hae hai hao hau hea hei heo heu hia hie hio hiu hoa hoe hoi hou hua hue hui huo
lae lai lao lau lea lei leo leu lia lie lio liu loa loe loi lou lua lue lui luo
mae mai mao mau mea mei meo meu mia mie mio miu moa moe moi mou mua mue mui muo
nae nai nao nau nea nei neo neu nia nie nio niu noa noe noi nou nua nue nui nuo
pae pai pao pau pea pei peo peu pia pie pio piu poa poe poi pou pua pue pui puo
sae sai sao sau sea sei seo seu sia sie sio siu soa soe soi sou sua sue sui suo
tae tai tao tau tea tei teo teu tia tie tio tiu toa toe toi tou tua tue tui tuo
wae wai wao wau wea wei weo weu wia wie wio wiu woa woe woi wou wua wue wui wuo
```

`[F][V]`
```
pha phe phi pho phu
sha she shi sho shu
tha the thi tho thu
wha whe whi who whu
```

`[C][V]`
```
ha he hi ho hu
la le li lo lu
ma me mi mo mu
na ne ni no nu
pa pe pi po pu
sa se si so su
ta te ti to tu
wa we wi wo wu
```