import timeit
"""
Given an arbitrary ransom note string and another string containing letters from all the magazines, 
write a function that returns true if the ransome note can be constrcuted from the magazines
otherwise return false

each individual letter in the magazine can only be used once in the ransom note

"""

# O(n + m) = O(N) where n is number of letters in ransom, m is number of letters in mag_string
# Space is O(1) since the hash map is limited by how many valid letters there are (26 if only lower case)
def ransom_note(ransom_note, mag_string):
    # Can use defaultdict from collections to initialize to int if you want
    letters = {}
    for char in mag_string:
        try:
            letters[char] += 1
        except KeyError:
            letters[char] = 1

    for char in ransom_note:
        try:
            if letters[char] == 0:
                return False
            else:
                letters[char] -= 1
        except KeyError:
            return False
    return True

# O(n * m + k) where n is chars in ransom, m is chars in mag, k is iterations for replace. O(1) space
def ransom_note_brute_force(ransom_note, mag_string):
    for note_char in ransom_note:
        if note_char not in mag_string:
            return False
        else:
            mag_string = mag_string.replace(note_char, "", 1)
    return True

assert not ransom_note("a", "b")
assert not ransom_note("aa", "ab")
assert ransom_note("aa", "aab")

assert not ransom_note_brute_force("a", "b")
assert not ransom_note_brute_force("aa", "ab")
assert ransom_note_brute_force("aa", "aab")

# Performance tests on 2000 letter sequences
start = timeit.default_timer()
ransom_note("elgjriyktygwsgsqjsjkzhlkebwpdeqgyzwdxlgsglmtxcbkqfehtkgfspwyehllimexwcwppputsazcdbzbanwkqhvejlhvrdculevohwqaxibjtotayhlhswjgjfzfcibnhmmmustfncffadlffsceigbjekcshwcextjbvsjmrmgywalsxolspgayfgabnlegzndxrlvlvrztuvwisofgswkkevgfqpksukwtotcsdhciteebfbatregvoymmsiwozyyvpkdgpaihkzlezepbolgbjzxobqefkioxpwbvadetrpstjpwujwltlaqtpchnnllsqfnsgfjvaattrzzqjwdlrjzwiqpuzfmkxjtuqlikeoidgkckxafyhdwhwbiakqdmmaloelqmufkcxyjeybnlvqmariaczceywzznyczzvfpedxyjhhtoehwawhjlvqmmgsbsjswenvzpyienxyqdiuyuoisbjqgfaagsmtfizobmkpometxpkwpuyaptquxtvngggmessvkybdooidguajlmgroeuymfuwshyxnwuzsfrlzagyjbungddxbtzedgtuvxzcyajkubwtyoyroufsxiaegopqijhuiwknldaclfcetgrpuifedbfquurjebrfvpqulufjjzspqsiimofblzqguekjejctbjthabcubodsxhvjfcgltwqmlwumiqplihdyhpghgpxdtoqjzcxefcmcnzznkpdidhnoiorijonorrwqzanjhiahezynxwqzqlvipxjmmrkbwicewjbbncgkzjfkbwwekrfqvihppittbsirupsidowkrqmffdvjrfshrvycfqwomcokflmppwvfbociwwhrlwyiwoqygxujhcglefiwvbleejaoaqrbztcftcyccmsjivwcuzspbwxdybimandacbzpjxbflmfyhjgzzjjicsbxogswpgoghcwudysvoqdyztmnzcbbgxtbgupvrkelgjriyktygwsgsqjsjkzhlkebwpdeqgyzwdxlgsglmtxcbkqfehtkgfspwyehllimexwcwppputsazcdbzbanwkqhvejlhvrdculevohwqaxibjtotayhlhswjgjfzfcibnhmmmustfncffadlffsceigbjekcshwcextjbvsjmrmgywalsxolspgayfgabnlegzndxrlvlvrztuvwisofgswkkevgfqpksukwtotcsdhciteebfbatregvoymmsiwozyyvpkdgpaihkzlezepbolgbjzxobqefkioxpwbvadetrpstjpwujwltlaqtpchnnllsqfnsgfjvaattrzzqjwdlrjzwiqpuzfmkxjtuqlikeoidgkckxafyhdwhwbiakqdmmaloelqmufkcxyjeybnlvqmariaczceywzznyczzvfpedxyjhhtoehwawhjlvqmmgsbsjswenvzpyienxyqdiuyuoisbjqgfaagsmtfizobmkpometxpkwpuyaptquxtvngggmessvkybdooidguajlmgroeuymfuwshyxnwuzsfrlzagyjbungddxbtzedgtuvxzcyajkubwtyoyroufsxiaegopqijhuiwknldaclfcetgrpuifedbfquurjebrfvpqulufjjzspqsiimofblzqguekjejctbjthabcubodsxhvjfcgltwqmlwumiqplihdyhpghgpxdtoqjzcxefcmcnzznkpdidhnoiorijonorrwqzanjhiahezynxwqzqlvipxjmmrkbwicewjbbncgkzjfkbwwekrfqvihppittbsirupsidowkrqmffdvjrfshrvycfqwomcokflmppwvfbociwwhrlwyiwoqygxujhcglefiwvbleejaoaqrbztcftcyccmsjivwcuzspbwxdybimandacbzpjxbflmfyhjgzzjjicsbxogswpgoghcwudysvoqdyztmnzcbbgxtbgupvrk", "kntckilspmljsltywnsevklatlurprjvctrtdaeoczyalzeitaodwpalyrqflysebszvdyayymslqasydaijphyxbfojzfqinaivufffzassicnvcamdtpmtorqooqhgbnatyvalcbjceeoitrptbuduqwsbgpduubeqadalzydghqsxziirljhzlhwlmwsabdgwxeuzmznrwukivztrheebgzvyqkawvdrgjmiywrzrbszzsofkgdjxwnmzflejaygygmdcllmvpksjdtgkbriotwwkozxoqfumexneswnusioogvzouyjldxgpduffzmrxcmpqqbbytcchbdhgpikrlykdwnnmvlwiinmvrehygezslkybqchmmsbkwiforibcbizwuvhldduhmnfolhoontlkzotniqedqhlzpfblxnbcfdxhycnwigknghfhqpcrcxvpterijggcqchucfffodqrtsdnpdyuwzwufllzzaxrpgtcbyzpnzupywbbtayugajeetwfwcjlthrhxxiorlkvkhcmyfnfeyyffotfofslsyesrospqpbnbvihlwyqvkdsngufheoteyebiikdpexpmeyajdfcgwaczemtplispugytuzyaemlmtgkxgetgfywdiefsrprzhdqhiopezyqsooyrfghjzwpfpdmlylqsdxxdujfkoifhauymhosvzvldqrvviqogukebkfvsmfbpixvwmiiqefogrmvsxhpxwfllgqlcsrrqjsnvashsaaqvmpkzmploflekyonwltoenkvjhxexzogxmqzgknscgundnhgyrofssnpoolbdcmrxehcafpdpyfldcdnqwjchoamxcaxznezmdfawlbnlkntlaazikmwqjjftotsndqnltjogqkybrkdiqlaqxbffrqpnkgbagscvbeidldfuvrqbhmhknhlweysgdosoadzuzkdguwomsbeccczpqryibmvrnydmalxkntckilspmljsltywnsevklatlurprjvctrtdaeoczyalzeitaodwpalyrqflysebszvdyayymslqasydaijphyxbfojzfqinaivufffzassicnvcamdtpmtorqooqhgbnatyvalcbjceeoitrptbuduqwsbgpduubeqadalzydghqsxziirljhzlhwlmwsabdgwxeuzmznrwukivztrheebgzvyqkawvdrgjmiywrzrbszzsofkgdjxwnmzflejaygygmdcllmvpksjdtgkbriotwwkozxoqfumexneswnusioogvzouyjldxgpduffzmrxcmpqqbbytcchbdhgpikrlykdwnnmvlwiinmvrehygezslkybqchmmsbkwiforibcbizwuvhldduhmnfolhoontlkzotniqedqhlzpfblxnbcfdxhycnwigknghfhqpcrcxvpterijggcqchucfffodqrtsdnpdyuwzwufllzzaxrpgtcbyzpnzupywbbtayugajeetwfwcjlthrhxxiorlkvkhcmyfnfeyyffotfofslsyesrospqpbnbvihlwyqvkdsngufheoteyebiikdpexpmeyajdfcgwaczemtplispugytuzyaemlmtgkxgetgfywdiefsrprzhdqhiopezyqsooyrfghjzwpfpdmlylqsdxxdujfkoifhauymhosvzvldqrvviqogukebkfvsmfbpixvwmiiqefogrmvsxhpxwfllgqlcsrrqjsnvashsaaqvmpkzmploflekyonwltoenkvjhxexzogxmqzgknscgundnhgyrofssnpoolbdcmrxehcafpdpyfldcdnqwjchoamxcaxznezmdfawlbnlkntlaazikmwqjjftotsndqnltjogqkybrkdiqlaqxbffrqpnkgbagscvbeidldfuvrqbhmhknhlweysgdosoadzuzkdguwomsbeccczpqryibmvrnydmalx")
print(timeit.default_timer() - start)

start2 = timeit.default_timer()
ransom_note_brute_force("elgjriyktygwsgsqjsjkzhlkebwpdeqgyzwdxlgsglmtxcbkqfehtkgfspwyehllimexwcwppputsazcdbzbanwkqhvejlhvrdculevohwqaxibjtotayhlhswjgjfzfcibnhmmmustfncffadlffsceigbjekcshwcextjbvsjmrmgywalsxolspgayfgabnlegzndxrlvlvrztuvwisofgswkkevgfqpksukwtotcsdhciteebfbatregvoymmsiwozyyvpkdgpaihkzlezepbolgbjzxobqefkioxpwbvadetrpstjpwujwltlaqtpchnnllsqfnsgfjvaattrzzqjwdlrjzwiqpuzfmkxjtuqlikeoidgkckxafyhdwhwbiakqdmmaloelqmufkcxyjeybnlvqmariaczceywzznyczzvfpedxyjhhtoehwawhjlvqmmgsbsjswenvzpyienxyqdiuyuoisbjqgfaagsmtfizobmkpometxpkwpuyaptquxtvngggmessvkybdooidguajlmgroeuymfuwshyxnwuzsfrlzagyjbungddxbtzedgtuvxzcyajkubwtyoyroufsxiaegopqijhuiwknldaclfcetgrpuifedbfquurjebrfvpqulufjjzspqsiimofblzqguekjejctbjthabcubodsxhvjfcgltwqmlwumiqplihdyhpghgpxdtoqjzcxefcmcnzznkpdidhnoiorijonorrwqzanjhiahezynxwqzqlvipxjmmrkbwicewjbbncgkzjfkbwwekrfqvihppittbsirupsidowkrqmffdvjrfshrvycfqwomcokflmppwvfbociwwhrlwyiwoqygxujhcglefiwvbleejaoaqrbztcftcyccmsjivwcuzspbwxdybimandacbzpjxbflmfyhjgzzjjicsbxogswpgoghcwudysvoqdyztmnzcbbgxtbgupvrkelgjriyktygwsgsqjsjkzhlkebwpdeqgyzwdxlgsglmtxcbkqfehtkgfspwyehllimexwcwppputsazcdbzbanwkqhvejlhvrdculevohwqaxibjtotayhlhswjgjfzfcibnhmmmustfncffadlffsceigbjekcshwcextjbvsjmrmgywalsxolspgayfgabnlegzndxrlvlvrztuvwisofgswkkevgfqpksukwtotcsdhciteebfbatregvoymmsiwozyyvpkdgpaihkzlezepbolgbjzxobqefkioxpwbvadetrpstjpwujwltlaqtpchnnllsqfnsgfjvaattrzzqjwdlrjzwiqpuzfmkxjtuqlikeoidgkckxafyhdwhwbiakqdmmaloelqmufkcxyjeybnlvqmariaczceywzznyczzvfpedxyjhhtoehwawhjlvqmmgsbsjswenvzpyienxyqdiuyuoisbjqgfaagsmtfizobmkpometxpkwpuyaptquxtvngggmessvkybdooidguajlmgroeuymfuwshyxnwuzsfrlzagyjbungddxbtzedgtuvxzcyajkubwtyoyroufsxiaegopqijhuiwknldaclfcetgrpuifedbfquurjebrfvpqulufjjzspqsiimofblzqguekjejctbjthabcubodsxhvjfcgltwqmlwumiqplihdyhpghgpxdtoqjzcxefcmcnzznkpdidhnoiorijonorrwqzanjhiahezynxwqzqlvipxjmmrkbwicewjbbncgkzjfkbwwekrfqvihppittbsirupsidowkrqmffdvjrfshrvycfqwomcokflmppwvfbociwwhrlwyiwoqygxujhcglefiwvbleejaoaqrbztcftcyccmsjivwcuzspbwxdybimandacbzpjxbflmfyhjgzzjjicsbxogswpgoghcwudysvoqdyztmnzcbbgxtbgupvrk", "kntckilspmljsltywnsevklatlurprjvctrtdaeoczyalzeitaodwpalyrqflysebszvdyayymslqasydaijphyxbfojzfqinaivufffzassicnvcamdtpmtorqooqhgbnatyvalcbjceeoitrptbuduqwsbgpduubeqadalzydghqsxziirljhzlhwlmwsabdgwxeuzmznrwukivztrheebgzvyqkawvdrgjmiywrzrbszzsofkgdjxwnmzflejaygygmdcllmvpksjdtgkbriotwwkozxoqfumexneswnusioogvzouyjldxgpduffzmrxcmpqqbbytcchbdhgpikrlykdwnnmvlwiinmvrehygezslkybqchmmsbkwiforibcbizwuvhldduhmnfolhoontlkzotniqedqhlzpfblxnbcfdxhycnwigknghfhqpcrcxvpterijggcqchucfffodqrtsdnpdyuwzwufllzzaxrpgtcbyzpnzupywbbtayugajeetwfwcjlthrhxxiorlkvkhcmyfnfeyyffotfofslsyesrospqpbnbvihlwyqvkdsngufheoteyebiikdpexpmeyajdfcgwaczemtplispugytuzyaemlmtgkxgetgfywdiefsrprzhdqhiopezyqsooyrfghjzwpfpdmlylqsdxxdujfkoifhauymhosvzvldqrvviqogukebkfvsmfbpixvwmiiqefogrmvsxhpxwfllgqlcsrrqjsnvashsaaqvmpkzmploflekyonwltoenkvjhxexzogxmqzgknscgundnhgyrofssnpoolbdcmrxehcafpdpyfldcdnqwjchoamxcaxznezmdfawlbnlkntlaazikmwqjjftotsndqnltjogqkybrkdiqlaqxbffrqpnkgbagscvbeidldfuvrqbhmhknhlweysgdosoadzuzkdguwomsbeccczpqryibmvrnydmalxkntckilspmljsltywnsevklatlurprjvctrtdaeoczyalzeitaodwpalyrqflysebszvdyayymslqasydaijphyxbfojzfqinaivufffzassicnvcamdtpmtorqooqhgbnatyvalcbjceeoitrptbuduqwsbgpduubeqadalzydghqsxziirljhzlhwlmwsabdgwxeuzmznrwukivztrheebgzvyqkawvdrgjmiywrzrbszzsofkgdjxwnmzflejaygygmdcllmvpksjdtgkbriotwwkozxoqfumexneswnusioogvzouyjldxgpduffzmrxcmpqqbbytcchbdhgpikrlykdwnnmvlwiinmvrehygezslkybqchmmsbkwiforibcbizwuvhldduhmnfolhoontlkzotniqedqhlzpfblxnbcfdxhycnwigknghfhqpcrcxvpterijggcqchucfffodqrtsdnpdyuwzwufllzzaxrpgtcbyzpnzupywbbtayugajeetwfwcjlthrhxxiorlkvkhcmyfnfeyyffotfofslsyesrospqpbnbvihlwyqvkdsngufheoteyebiikdpexpmeyajdfcgwaczemtplispugytuzyaemlmtgkxgetgfywdiefsrprzhdqhiopezyqsooyrfghjzwpfpdmlylqsdxxdujfkoifhauymhosvzvldqrvviqogukebkfvsmfbpixvwmiiqefogrmvsxhpxwfllgqlcsrrqjsnvashsaaqvmpkzmploflekyonwltoenkvjhxexzogxmqzgknscgundnhgyrofssnpoolbdcmrxehcafpdpyfldcdnqwjchoamxcaxznezmdfawlbnlkntlaazikmwqjjftotsndqnltjogqkybrkdiqlaqxbffrqpnkgbagscvbeidldfuvrqbhmhknhlweysgdosoadzuzkdguwomsbeccczpqryibmvrnydmalx")
print(timeit.default_timer() - start2)