"""
2512. Reward Top K Students
https://leetcode.com/problems/reward-top-k-students
"""
import collections
from typing import List


class Solution:
    def topStudents(
            self,
            positive_feedback: List[str], negative_feedback: List[str],
            report: List[str], student_id: List[int], k: int) -> List[int]:
        scores = collections.Counter()
        positive_feedback, negative_feedback = map(set, [positive_feedback, negative_feedback])

        for idx in range(len(report)):
            report[idx] = report[idx].replace(',', '').replace('.', '').lower()

        # 2. Scoring
        for sid, txt in zip(student_id, report):
            word_freq = collections.Counter(txt.split())
            scores[sid] = 0;
            for word, cnt in word_freq.items():
                if word in positive_feedback:
                    scores[sid] += (3 * cnt)
                elif word in negative_feedback:
                    scores[sid] -= cnt

        # 3. Ranking
        return sorted(scores.keys(), key=lambda sid: (-scores[sid], sid))[:k]
