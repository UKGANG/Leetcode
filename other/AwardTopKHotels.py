"""
Award Top K Hotel
"""
import collections


def awardTopKHotels(positiveKeywords, negativeKeywords, hotelIds, reviews, k):
    # Write your code here
    # 1. Preprocessing
    scores = collections.Counter()
    positiveKeywords, negativeKeywords = map(lambda x: x.lower(), [positiveKeywords, negativeKeywords])
    positiveKeywords, negativeKeywords = map(lambda x: x.split(), [positiveKeywords, negativeKeywords])
    positiveKeywords, negativeKeywords = map(set, [positiveKeywords, negativeKeywords])

    for idx in range(len(reviews)):
        reviews[idx] = reviews[idx].replace(',', '').replace('.', '').lower()

    # 2. Scoring
    for hotel_id, review in zip(hotelIds, reviews):
        word_freq = collections.Counter(review.split())
        for word, cnt in word_freq.items():
            if word in positiveKeywords:
                scores[hotel_id] += (3 * cnt)
            elif word in negativeKeywords:
                scores[hotel_id] -= cnt

    # 3. Ranking
    return sorted(scores.keys(), key=lambda hotel_id: (-scores[hotel_id], hotel_id))[:k]
