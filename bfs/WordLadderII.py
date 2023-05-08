'''
126. Word Ladder II
https://leetcode.com/problems/word-ladder-ii/
'''
import collections
import itertools
from typing import List

from test_tool import assert_value


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        word_hash = collections.defaultdict(set)
        hash_word = collections.defaultdict(set)

        wordList.append(beginWord)

        for word in wordList:
            for i in range(len(word)):
                word_hash_str = word[:i] + '_' + word[i + 1:]
                word_hash[word].add(word_hash_str)
                hash_word[word_hash_str].add(word)

        begin_queue = collections.deque([beginWord])
        end_queue = collections.deque([endWord])

        begin_seen = set()
        end_seen = set()
        begin_path = collections.defaultdict(set)
        end_path = collections.defaultdict(set)
        res = []

        begin_seen.add(beginWord)
        end_seen.add(endWord)

        def get_path(path_map, word):
            path = []
            queue = collections.deque([[word]])
            while queue:
                size = len(queue)
                for _ in range(size):
                    combo = queue.popleft()
                    if not path_map[combo[-1]]:
                        path.append(combo)
                        continue
                    for word_next in path_map[combo[-1]]:
                        combo_next = combo[:]
                        combo_next.append(word_next)
                        queue.append(combo_next)
            return path

        def bfs(queue, src_seen, dest_seen, src_path, dest_path):
            combos = []
            size = len(queue)
            seen = set()
            for _ in range(size):
                word = queue.popleft()
                for hash_str in word_hash[word]:
                    for word_next in hash_word[hash_str]:
                        if word == word_next:
                            continue
                        if word_next in src_seen:
                            continue
                        if word_next in dest_seen:
                            forward_path = [path[::-1] for path in get_path(src_path, word)]
                            backward_path = get_path(dest_path, word_next)
                            m, n = len(forward_path), len(backward_path)
                            for x, y in itertools.product(range(m), range(n)):
                                combo = forward_path[x][:]
                                combo.extend(backward_path[y])
                                combos.append(combo)
                            continue
                        if word_next not in seen:
                            queue.append(word_next)
                        seen.add(word_next)
                        src_path[word_next].add(word)
            src_seen |= seen
            return combos

        while begin_queue and end_queue:
            res = bfs(begin_queue, begin_seen, end_seen, begin_path, end_path)
            if res:
                return res
            res = bfs(end_queue, end_seen, begin_seen, end_path, begin_path)
            if res:
                res = [p[::-1] for p in res]
                return res
        return []

    def _findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordList = set(wordList)
        if endWord not in wordList:
            return []
        parents = collections.defaultdict(list)
        curr_level = {beginWord}
        while curr_level:
            next_level = set()
            wordList -= curr_level
            for word in curr_level:
                for i in range(len(word)):
                    for c in range(ord('a'), ord('a') + 26):
                        c = chr(c)
                        next_word = f'{word[:i]}{c}{word[i + 1:]}'
                        if next_word in wordList:
                            next_level.add(next_word)
                            parents[next_word].append(word)
            if endWord in next_level:
                break

            curr_level = next_level

        curr_level = [(endWord, [])]
        res = []

        while curr_level:
            prev_level = []
            for word, suffix in curr_level:
                if word == beginWord:
                    suffix.insert(0, word)
                    res.append(suffix)
                    continue
                for parent in parents[word]:
                    prev_suffix = suffix.copy()
                    prev_suffix.insert(0, word)
                    prev_level.append((parent, prev_suffix))
            if res:
                break
            curr_level = prev_level

        return res


# assert_value([["hit", "hot", "dot", "dog", "cog"], ["hit", "hot", "lot", "log", "cog"]],
#              Solution().findLadders,
#              beginWord="hit", endWord="cog", wordList=["hot", "dot", "dog", "lot", "log", "cog"])
# assert_value([],
#              Solution().findLadders,
#              beginWord="hit", endWord="cog", wordList=["hot", "dot", "dog", "lot", "log"])
# assert_value([["red", "ted", "tad", "tax"], ["red", "ted", "tex", "tax"], ["red", "rex", "tex", "tax"]],
#              Solution().findLadders,
#              beginWord="red", endWord="tax", wordList=["ted", "tex", "red", "tax", "tad", "den", "rex", "pee"])
assert_value([["magic", "manic", "mania", "maria", "marta", "marty", "party", "parry", "perry", "peary", "pearl"],
              ["magic", "manic", "mania", "maria", "maris", "paris", "parks", "perks", "peaks", "pears", "pearl"],
              ["magic", "manic", "mania", "maria", "marta", "marty", "marry", "merry", "perry", "peary", "pearl"],
              ["magic", "manic", "mania", "maria", "marta", "marty", "marry", "parry", "perry", "peary", "pearl"],
              ["magic", "manic", "mania", "maria", "maris", "marks", "parks", "perks", "peaks", "pears", "pearl"]],
             Solution().findLadders,
             beginWord="magic", endWord="pearl",
             wordList=["flail", "halon", "lexus", "joint", "pears", "slabs", "lorie", "lapse", "wroth", "yalow",
                       "swear", "cavil", "piety", "yogis", "dhaka", "laxer", "tatum", "provo", "truss", "tends",
                       "deana", "dried", "hutch", "basho", "flyby", "miler", "fries", "floes", "lingo", "wider",
                       "scary", "marks", "perry", "igloo", "melts", "lanny", "satan", "foamy", "perks", "denim",
                       "plugs", "cloak", "cyril", "women", "issue", "rocky", "marry", "trash", "merry", "topic",
                       "hicks", "dicky", "prado", "casio", "lapel", "diane", "serer", "paige", "parry", "elope",
                       "balds", "dated", "copra", "earth", "marty", "slake", "balms", "daryl", "loves", "civet",
                       "sweat", "daley", "touch", "maria", "dacca", "muggy", "chore", "felix", "ogled", "acids",
                       "terse", "cults", "darla", "snubs", "boats", "recta", "cohan", "purse", "joist", "grosz",
                       "sheri", "steam", "manic", "luisa", "gluts", "spits", "boxer", "abner", "cooke", "scowl",
                       "kenya", "hasps", "roger", "edwin", "black", "terns", "folks", "demur", "dingo", "party",
                       "brian", "numbs", "forgo", "gunny", "waled", "bucks", "titan", "ruffs", "pizza", "ravel",
                       "poole", "suits", "stoic", "segre", "white", "lemur", "belts", "scums", "parks", "gusts",
                       "ozark", "umped", "heard", "lorna", "emile", "orbit", "onset", "cruet", "amiss", "fumed",
                       "gelds", "italy", "rakes", "loxed", "kilts", "mania", "tombs", "gaped", "merge", "molar",
                       "smith", "tangs", "misty", "wefts", "yawns", "smile", "scuff", "width", "paris", "coded",
                       "sodom", "shits", "benny", "pudgy", "mayer", "peary", "curve", "tulsa", "ramos", "thick",
                       "dogie", "gourd", "strop", "ahmad", "clove", "tract", "calyx", "maris", "wants", "lipid",
                       "pearl", "maybe", "banjo", "south", "blend", "diana", "lanai", "waged", "shari", "magic",
                       "duchy", "decca", "wried", "maine", "nutty", "turns", "satyr", "holds", "finks", "twits",
                       "peaks", "teems", "peace", "melon", "czars", "robby", "tabby", "shove", "minty", "marta",
                       "dregs", "lacks", "casts", "aruba", "stall", "nurse", "jewry", "knuth"])
# assert_value([["cet", "cat", "can", "ian", "inn", "ins", "its", "ito", "ibo", "ibm", "ism"],
#               ["cet", "cot", "con", "ion", "inn", "ins", "its", "ito", "ibo", "ibm", "ism"]],
#              Solution().findLadders,
#              beginWord="cet", endWord="ism",
#              wordList=["kid", "tag", "pup", "ail", "tun", "woo", "erg", "luz", "brr", "gay", "sip", "kay", "per", "val",
#                        "mes", "ohs", "now", "boa", "cet", "pal", "bar", "die", "war", "hay", "eco", "pub", "lob", "rue",
#                        "fry", "lit", "rex", "jan", "cot", "bid", "ali", "pay", "col", "gum", "ger", "row", "won", "dan",
#                        "rum", "fad", "tut", "sag", "yip", "sui", "ark", "has", "zip", "fez", "own", "ump", "dis", "ads",
#                        "max", "jaw", "out", "btu", "ana", "gap", "cry", "led", "abe", "box", "ore", "pig", "fie", "toy",
#                        "fat", "cal", "lie", "noh", "sew", "ono", "tam", "flu", "mgm", "ply", "awe", "pry", "tit", "tie",
#                        "yet", "too", "tax", "jim", "san", "pan", "map", "ski", "ova", "wed", "non", "wac", "nut", "why",
#                        "bye", "lye", "oct", "old", "fin", "feb", "chi", "sap", "owl", "log", "tod", "dot", "bow", "fob",
#                        "for", "joe", "ivy", "fan", "age", "fax", "hip", "jib", "mel", "hus", "sob", "ifs", "tab", "ara",
#                        "dab", "jag", "jar", "arm", "lot", "tom", "sax", "tex", "yum", "pei", "wen", "wry", "ire", "irk",
#                        "far", "mew", "wit", "doe", "gas", "rte", "ian", "pot", "ask", "wag", "hag", "amy", "nag", "ron",
#                        "soy", "gin", "don", "tug", "fay", "vic", "boo", "nam", "ave", "buy", "sop", "but", "orb", "fen",
#                        "paw", "his", "sub", "bob", "yea", "oft", "inn", "rod", "yam", "pew", "web", "hod", "hun", "gyp",
#                        "wei", "wis", "rob", "gad", "pie", "mon", "dog", "bib", "rub", "ere", "dig", "era", "cat", "fox",
#                        "bee", "mod", "day", "apr", "vie", "nev", "jam", "pam", "new", "aye", "ani", "and", "ibm", "yap",
#                        "can", "pyx", "tar", "kin", "fog", "hum", "pip", "cup", "dye", "lyx", "jog", "nun", "par", "wan",
#                        "fey", "bus", "oak", "bad", "ats", "set", "qom", "vat", "eat", "pus", "rev", "axe", "ion", "six",
#                        "ila", "lao", "mom", "mas", "pro", "few", "opt", "poe", "art", "ash", "oar", "cap", "lop", "may",
#                        "shy", "rid", "bat", "sum", "rim", "fee", "bmw", "sky", "maj", "hue", "thy", "ava", "rap", "den",
#                        "fla", "auk", "cox", "ibo", "hey", "saw", "vim", "sec", "ltd", "you", "its", "tat", "dew", "eva",
#                        "tog", "ram", "let", "see", "zit", "maw", "nix", "ate", "gig", "rep", "owe", "ind", "hog", "eve",
#                        "sam", "zoo", "any", "dow", "cod", "bed", "vet", "ham", "sis", "hex", "via", "fir", "nod", "mao",
#                        "aug", "mum", "hoe", "bah", "hal", "keg", "hew", "zed", "tow", "gog", "ass", "dem", "who", "bet",
#                        "gos", "son", "ear", "spy", "kit", "boy", "due", "sen", "oaf", "mix", "hep", "fur", "ada", "bin",
#                        "nil", "mia", "ewe", "hit", "fix", "sad", "rib", "eye", "hop", "haw", "wax", "mid", "tad", "ken",
#                        "wad", "rye", "pap", "bog", "gut", "ito", "woe", "our", "ado", "sin", "mad", "ray", "hon", "roy",
#                        "dip", "hen", "iva", "lug", "asp", "hui", "yak", "bay", "poi", "yep", "bun", "try", "lad", "elm",
#                        "nat", "wyo", "gym", "dug", "toe", "dee", "wig", "sly", "rip", "geo", "cog", "pas", "zen", "odd",
#                        "nan", "lay", "pod", "fit", "hem", "joy", "bum", "rio", "yon", "dec", "leg", "put", "sue", "dim",
#                        "pet", "yaw", "nub", "bit", "bur", "sid", "sun", "oil", "red", "doc", "moe", "caw", "eel", "dix",
#                        "cub", "end", "gem", "off", "yew", "hug", "pop", "tub", "sgt", "lid", "pun", "ton", "sol", "din",
#                        "yup", "jab", "pea", "bug", "gag", "mil", "jig", "hub", "low", "did", "tin", "get", "gte", "sox",
#                        "lei", "mig", "fig", "lon", "use", "ban", "flo", "nov", "jut", "bag", "mir", "sty", "lap", "two",
#                        "ins", "con", "ant", "net", "tux", "ode", "stu", "mug", "cad", "nap", "gun", "fop", "tot", "sow",
#                        "sal", "sic", "ted", "wot", "del", "imp", "cob", "way", "ann", "tan", "mci", "job", "wet", "ism",
#                        "err", "him", "all", "pad", "hah", "hie", "aim"])
