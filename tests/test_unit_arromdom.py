import unittest
from arrand import arrandom


class TestArrandom(unittest.TestCase):

    # ----------- Basic random text selection -----------

    def test_aya(self):
        self.assertIsInstance(arrandom.aya(), str)
        self.assertTrue(arrandom.aya().strip())

    def test_hadith(self):
        self.assertIsInstance(arrandom.hadith(), str)
        self.assertTrue(arrandom.hadith().strip())

    def test_phrase(self):
        self.assertIsInstance(arrandom.phrase(), str)
        self.assertTrue(arrandom.phrase().strip())

    def test_paragraph(self):
        self.assertIsInstance(arrandom.paragraph(), str)
        self.assertTrue(arrandom.paragraph().strip())

    def test_poem(self):
        self.assertIsInstance(arrandom.poem(), str)
        self.assertTrue(arrandom.poem().strip())

    def test_word(self):
        self.assertIsInstance(arrandom.word(), str)
        self.assertTrue(arrandom.word().strip())

    def test_proverb(self):
        self.assertIsInstance(arrandom.proverb(), str)
        self.assertTrue(arrandom.proverb().strip())

    # ----------- Vocalized versions -----------

    def test_vocalized_hadith(self):
        result = arrandom.hadith(vocalized=True)
        self.assertIsInstance(result, str)
        self.assertTrue(result.strip())

    def test_vocalized_sample(self):
        lines = arrandom.sample(category="text", max_length=2, vocalized=True)
        self.assertIsInstance(lines, list)
        self.assertEqual(len(lines), 2)
        for line in lines:
            self.assertIsInstance(line, str)
            self.assertTrue(line.strip())

    # ----------- Sample and select -----------

    def test_sample_returns_list(self):
        lines = arrandom.sample(category="text", max_length=3)
        self.assertIsInstance(lines, list)
        self.assertEqual(len(lines), 3)
        for line in lines:
            self.assertIsInstance(line, str)
            self.assertTrue(line.strip())

    def test_sample_invalid_category(self):
        lines = arrandom.sample(category="nonexistent", max_length=1)
        self.assertIsInstance(lines, list)
        self.assertIn("File not found", lines[0])

    def test_sample_zero_lines(self):
        lines = arrandom.sample(category="text", max_length=0)
        self.assertIsInstance(lines, list)
        self.assertEqual(len(lines), 0)

    def test_select(self):
        result = arrandom.select("text")
        self.assertIsInstance(result, str)
        self.assertTrue(result.strip())

    # ----------- Nonsense generation -----------

    def test_rand_sentence(self):
        sentence = arrandom.rand_sentence()
        self.assertIsInstance(sentence, str)
        self.assertGreaterEqual(len(sentence.split()), 1)

    def test_rand_sentences_multiple(self):
        sentences = arrandom.rand_sentences(5)
        self.assertIsInstance(sentences, list)
        self.assertEqual(len(sentences), 5)
        for s in sentences:
            self.assertIsInstance(s, str)
            self.assertTrue(s.strip())

    def test_rand_sentence_empty_dict(self):
        sentence = arrandom.rand_sentence(word_dict={})
        self.assertIsInstance(sentence, str)

    # ----------- Filtering Options (word/char length) -----------

    def test_sample_min_words(self):
        lines = arrandom.sample(category="text", max_length=5, min_words=3)
        self.assertTrue(all(len(line.split()) >= 3 for line in lines))

    def test_sample_max_words(self):
        lines = arrandom.sample(category="text", max_length=5, max_words=10)
        self.assertTrue(all(len(line.split()) <= 10 for line in lines))

    def test_sample_min_and_max_words(self):
        lines = arrandom.sample(category="text", max_length=5, min_words=3, max_words=8)
        for line in lines:
            wc = len(line.split())
            self.assertGreaterEqual(wc, 3)
            self.assertLessEqual(wc, 8)

    def test_sample_max_chars(self):
        lines = arrandom.sample(category="text", max_length=5, max_chars=80)
        for line in lines:
            self.assertLessEqual(len(line), 80)

    def test_sample_filters_return_no_match(self):
        lines = arrandom.sample(category="text", max_length=3, min_words=999)
        self.assertEqual(len(lines), 0)



if __name__ == '__main__':
    unittest.main()
