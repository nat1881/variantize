import re

#determines loci of consonantal variation
def split_con(word):
    substrings = []
    skip = False
    for index, letter in enumerate(word):
        if skip is True:
            skip = False
            continue
        elif index < len(word) - 1:
            pair = letter + word[index + 1]
            if letter + word[index + 1] in consonant_rules:
                substrings.append(pair)
                skip = True
            elif letter in consonant_rules:
                substrings.append(letter)
            else:
                 substrings.append((letter,))
        elif letter in consonant_rules:
            substrings.append(letter)
        else:
            substrings.append((letter,))
    return substrings

#determines loci of vocalic variation
def split_vow(word):
    substrings = []
    skip = False
    for index, letter in enumerate(word):
        if skip is True:
            skip = False
            continue
        elif index < len(word) - 1:
            pair = letter + word[index + 1]
            if letter + word[index + 1] in vowel_rules:
                substrings.append(pair)
                skip = True
            elif letter in vowel_rules:
                substrings.append(letter)
            else:
                substrings.append((letter,))
        elif letter in vowel_rules:
            substrings.append(letter)
        else:
            substrings.append((letter,))
    return substrings

#alter built-in Cartesian product function so it returns only the first 50 results
def product(*args, repeat=1):
    pools = [tuple(pool) for pool in args] * repeat
    result = [[]]
    for pool in pools:
        result = [x+[y] for x in result for y in pool]
    for prod in result[:50]:
        yield tuple(prod)


whole_word_rules = (("sur","sor"),
                    ("comme","cum"),
                    ("le","li"),
                    ("lui","li"),
                    ("aron","er"),
                    ("sœur", "seror"),
                    ("croyance","creance"),
                    ("ses", "sen"),
                    ("tes", "ten"),
                    ("mes", "men"),
                    ("moi", "mi"),
                    ("ous", "o"),
                    ("les", "li"),
                    ("leur", "lur"),
                    ("château","chastel"),
                    ("isse", "e"),
                    ("bury", "biri"),
                    ("cestre", "chester"),
                    ("icest",'ice'),
                    ("royal", "real"),
                    ("son", "sun"),
                    ("était", "ert"),
                    ("son", "se"),
                    ("mon", "me"),
                    ("ton", "te"),
                    ("et", "e"),
                    ("ou", "u"),
                    )

vowel_rules = {"ai":["ai","a","ae", "e", "ee", "ei", "oi", "at", "ad", "es"],
            "au":["au","a"],
            "e":["e","a","ay", "ea", "ee", "ei", "ey", "e", "et", "y", "ie", "o", "u","ed", "ou"],
            "o":["o","a", "e", "ou", "u", "oe", "os"],
            "a":["a","ai","ay","au", "aau", "e", "o", "at"],
            "ei":["ei","e", "i", "ie", "oy", "oi"],
            "eu":["eu","e", "iw", "ou", "u", "uu", "ol"],
            "i":["i","e", "ee", "ey", "y"],
            "ie":["ie","e", "ee", "ei", "i", "y",],
            "ieu":["ieu","e", "iu", "eu", "u"],
            "oi":["oi","ai","e","i","o", "u", "ei"],
            "ue":["ue","e","eo", "o", "oe", "u", "we"],
            "ae":["ae","ey"],
            "ui":["ui","i","y", "u", "oi", "oy"],
            "ou":["ou","o", "ol", "u"],
            "u":["u","ou","ow", "uu", "yw", "w",],
            "oir":["oir","eir"],
            "onner":["onner","uner"],
            "eur": ["eur", "ur"],
            "y": ["y", "i"],
            "uv":["uv","o"],
            "ais":["ais","ois"],
            "our":["our","or"],
            "sur":["sur","sor"],
            "nie":["nie","ne"],
            "ous":["ous", "o"],
            "aim":["aim","am"],
            "on": ["on", "un"],
            "er": ["er", "e"],
            "ge":["ge", "gie"],
            "en":["en", "on", "a"],
            "ea":["ea","oya"],
            "un":["un", "om", "on"],
            "ua":["ua", "e"],
            "ain":["ain", "ein"],
            "es":["es", "ant"],
            "em":["em", "a"],
            }
vowels = [("ai", "ae"), #more vowel rules for combinations with consonant rules
          ("ai","a"),
          ("ai", "ae"),
          ("ai", "e"),
          ("ai","ee"),
          ("ai", "ei"),
          ("ai", "oi"),
          ("ai", "at"),
          ("ai", "ad"),
          ("au","a"),
          ("e", "a"),
          ("e", "ay"),
          ("e","ea"),
          ("e","ee"),
          ("e","ei"),
          ("e","ey"),
          ("e","y"),
          ("e","ie"),
          ("e","o"),
          ("e","u"),
          ("e","ed"),
          ("o","a"),
          ("o","e"),
          ("o","ou"),
          ("o","u"),
          ("o","oe"),
        ("a","ai"),
        ("a","ay"),
        ("a","au"),
        ("a","aau"),
        ("a","e"),
        ("a","o"),
        ("a","at"),
        ("ei","e"),
        ("e","i"),
        ("e","ie"),
        ("e","oy"),
        ("e","oi"),
        ("eu","e"),
        ("eu","iw"),
        ("eu","ou"),
        ("eu","u"),
        ("eu","uu"),
        ("eu", "ol"),
        ("i","e"),
        ("i","ee"),
        ("i","ey"),
        ("i","y"),
        ("ie","e"),
        ("ie","ee"),
        ("ie","ei"),
        ("ie","i"),
        ("ie","y"),
        ("ieu","e"),
        ("ieu","iu"),
        ("ie","eu"),
        ("ie","u"),
        ("oi","ai"),
        ("oi","e"),
        ("oi","i"),
        ("oi","o"),
        ("oi","u"),
        ("oi","ei"),
        ("ue","e"),
        ("ue","eo"),
        ("ue","o"),
        ("ue","oe"),
        ("ue","u"),
        ("ue","we"),
        ("ae","ey"),
        ("ui","i"),
        ("ui","y"),
        ("ui","u"),
        ("ui","oi"),
        ("ui","oy"),
        ("ou","o"),
        ("ou","ol"),
        ("ou","u"),
        ("u","ou"),
        ("u","ow"),
        ("u","uu"),
        ("u","yw"),
        ("u","w"),
        ("oir","eir"),
        ("onner","uner"),
        ("eur", "ur"),
        ("y", "i"),
        ("ouv","oo"),
        ("ais","ois"),
        ("our","or"),
        ("sur","sor"),
        ("nie","ne"),
        ("ous", "o"),
        ("aim","am"),
        ("aron", "arun"),
        ("her", "he"),
        ("ge", "gie"),
        ("len", "lon"),
        ("real","royal"),
        ("un", "om"),
        ("un","on"),
        ("ouan", "oen"),
        ("ain", "ein"),
           ]

consonant_rules = {"ch":["ch","k", "c", "sch"],
            "s":["s","c", "ss", "z", "t", "th", "d", "ze", ""],
            "z":["z","c", "ts", "t"],
            "c":["c","ch", "k", "s", "sc", "qu", "q"],
            "t":["t","d", "th", "", "tt"],
            "qu":["qu","k", "cqu",],
            "r":["r","rr"],
            "rr":["rr","r"],
            "ss":["ss","s", "c"],
            "v":["v","w"],
            "ph":["ph","f"],
            "x":["us", "x"],
            "j":["jh", "j"],
            "chr":["cr", "chr"],
            "g":["gw","gu","w", "k"],
            "er":["er","edr"],
            "q":["q","cq"],
            "mn":["mn","mm"],
            "cy":["cy","chy"],
            "em":["em","en"],
            "n":["n","m", "nn"],
            "m":["m", "n", "mm"],
            "eque":["eque","eske"],
            "l":["l","ll", "u"],
            "hi":["hi","i"],
            "ng":["ng", "n"],
            "nn":["nn", "n"],
            "p":["p", "pp"],
            "nc":["nc", "n"],
            "d": ["d", ""],
            "te":["te", "tet"],
            "ge":["ge", "g"],
            "ll":["ll", "l"],
            "ff":["ff", "f"],
            }


accent = {
    "ô": ["os", "o"],
    "ê": ["es", "e"],
    "é": ["es", "e"],
    "è": ["es", "e"],
    "ë": ["e"],
    "î": ["is", "i"],
    "ç": ["c", "ce"],
    "â": ["as", "a"],
    "ù": ["u"],
    "ï": ["i"],
    "œ": ["oe"],
    "à": ["a"],
    "ü":["u"],
    "û":["u", "us"]
    }

#replace accents in word with historical variants
def accent_filler(word):
    combos = [(c,) if c not in accent else accent[c] for c in word]
    return (''.join(o) for o in product(*combos))

#replace vowel loci of variation with historical variants
def vowel_replace(word):
    combos = []
    for spli in split_vow(word):
        if spli in vowel_rules:
            combos += [vowel_rules[spli]]
        else:
            combos += (spli,)
    return (''.join(o) for o in product(*combos))

#replace consonant loci of variation with historical variants
def consonant_replace(word):
    combos = []
    for spli in split_con(word):
        if spli in consonant_rules:
            combos += [consonant_rules[spli]]
        else:
            combos += (spli,)
    return (''.join(o) for o in product(*combos))


def variantize(word): #returns a list of variants
    list0 = list(accent_filler(word))
    list2 = []
    a = []
    b = []
    c =[]

    for filler in list0[:]:
        vow = list(vowel_replace(filler)) #list of vocalic variants
        con = list(consonant_replace(filler)) #list of consonantal variants

        for og, repl in whole_word_rules[:]:
            if og in filler:
                c1 = filler.replace(og, repl)
                a.append(c1)

        for consonant in con: #apply vowel rules to words with historical consonantal variants
            for ini, fin in vowels[:]:
                if ini in consonant:
                    ergh = consonant.replace(ini, fin)
                    b.append(ergh)
                if len(b)<=25:
                    c = b
                else:
                    c = b[:25]

        list1 = list0 + con + vow +b + c

        for word in list1: #morphological rule applies to all generated forms
            pl = re.sub('$', 's', word)
            list2.append(pl)

        return list(set(list1+list2))