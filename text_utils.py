import re
from collections import Counter

def process_text(text):
    words = re.findall(r'\b\w+\b', text.lower())
    return Counter(words)

def find_word_contexts(text, target_word, left_len=5, right_len=5, cut_length=False):
    target_word = target_word.lower()
    results = []

    # Разбить текст на предложения
    sentences = re.split(r'(?<=[.!?])\s*', text)
    for i, sentence in enumerate(sentences):
        words = re.findall(r'\b\w+\b', sentence.lower())
        indices = [idx for idx, word in enumerate(words) if word == target_word]

        for idx in indices:
            full_index = sum(len(re.findall(r'\b\w+\b', s)) for s in sentences[:i]) + idx

            if cut_length:
                left_start = max(0, idx - left_len)
                right_end = min(len(words), idx + right_len + 1)
                context_words = words[left_start:right_end]
            else:
                all_words = re.findall(r'\b\w+\b', text.lower())
                left_start = max(0, full_index - left_len)
                right_end = min(len(all_words), full_index + right_len + 1)
                context_words = all_words[left_start:full_index] + [all_words[full_index]] + all_words[full_index+1:right_end]

            left_context = context_words[:left_len]
            right_context = context_words[left_len+1:]
            center = context_words[left_len]

            results.append({
                'left': ' '.join(left_context),
                'center': center,
                'right': ' '.join(right_context)
            })

    return results