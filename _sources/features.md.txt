## 📚 Documentation & API Usage

The `arrand.arrandom` module provides simple functions to retrieve random Arabic texts across various categories.

### 🧠 Available Functions

| Function                       | Description                          | Supports Vocalized |
| ------------------------------ | ------------------------------------ | ------------------ |
| `aya()`                        | Returns a random Quranic verse       | ✅                  |
| `hadith()`                     | Returns a random Hadith              | ✅                  |
| `phrase()`                     | Returns a random literary phrase     | ✅                  |
| `proverb()`                    | Returns a random Arabic proverb      | ✅                  |
| `poem()`                       | Returns a random line of poetry      | ✅                  |
| `paragraph()`                  | Returns a random paragraph           | ✅                  |
| `word()`                       | Returns a single random Arabic word  | ✅                  |
| `select(category)`             | Generic text selector by category    | ✅                  |
| `sample(category, max_length)` | Returns multiple lines from category | ✅                  |
| `rand_sentence()`              | Generates a nonsense sentence        | ❌                  |
| `rand_sentences(n)`            | Generates multiple nonsense lines    | ❌                  |



### 🔎 Example: Get One Text from Each Category

```python
import arrand.arrandom as rnd

print(rnd.aya())
print(rnd.hadith())
print(rnd.proverb())
print(rnd.phrase())
print(rnd.word())
print(rnd.poem())
print(rnd.paragraph())
```

### 🔄 Example: Get Vocalized Data

```python
print(rnd.aya(vocalized=True))
print(rnd.sample("text", max_length=2, vocalized=True))
```

### 📦 Example: Generate Nonsense Sentences

```python
print(rnd.rand_sentence())
print(rnd.rand_sentences(3))
```

------

### 🗂️ Categories Available

- `"aya"`
- `"hadith"`
- `"phrase"`
- `"proverb"`
- `"poem"`
- `"paragraph"`
- `"word"`
- `"text"`

To retrieve multiple lines, use:

```python
rnd.sample(category="poem", max_length=2)
```

To get a single random line:

```python
rnd.select("proverb")
```

Generate samples with word count control

```python
rnd.arrandom.sample(category="text", max_length=3, min_words=9, max_words=20)
```



## 🖥️ Command Line Interface (CLI)

Once installed, you can use `arrand` directly from the command line:

### 🔧 Basic usage

~~~shell
```bash
arrand
~~~



* Outputs a random Arabic text from the "text" category.

------

### 🗂️ Select a specific category

```bash
arrand --category aya
arrand --category hadith
arrand --category phrase
arrand --category poem
arrand --category proverb
arrand --category paragraph
arrand --category word
```

------

### 🔢 Generate multiple entries

Use `-n` or `--number` to control how many items to generate:

```bash
arrand -c poem -n 3
arrand -c phrase -n 5
```

------

### 🔤 Enable vocalization (tashkeel)

```bash
arrand -c hadith --vocalized
```

------

### 🤪 Generate nonsense sentences

```bash
arrand --category nonsense
arrand -c nonsense -n 2
```

----

### ✂️ Filter text by length

```bash
arrand --category poem --min-words 5 --max-words 10
arrand --category phrase --max-chars 120
```

------

### 🆘 Show help

```bash
arrand --help
```

