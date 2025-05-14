NLP Проект: Анализ текста и вычисление TF-IDF

Этот проект содержит две основные части:

- text_utils.py: содержит функции для обработки текста, поиска слов и вывода их контекста.
- tf_idf_class.py: реализация подсчёта TF, IDF и TF-IDF.

Также приложен файл `examples.ipynb`, демонстрирующий работу кода на реальном тексте из произведения «Улисс» Джеймса Джойса.

 Функционал

 text_utils.py
- `process_text(text)` — считает частоту слов в тексте.
- `find_word_contexts(text, word, left_len, right_len, cut_length)` — находит все упоминания слова с указанным контекстом.

 tf_idf_class.py
- `get_tf(word, doc_index)` — возвращает Term Frequency.
- `get_idf(word, doc_index)` — возвращает Inverse Document Frequency.
- `get_tf_idf(word, doc_index, ignore_stopwords)` — возвращает TF-IDF, учитывая или игнорируя стопслова.

 Требования
- Python 3.8+
- Библиотеки: `requests`, `re`, `collections`, `math`

 Установка
```bash
pip install requests