import argparse
from . import arrandom


def main():
    parser = argparse.ArgumentParser(description="Arrand: Arabic Random Text Generator")
    parser.add_argument("--min-words", type=int, help="Minimum word count per line")
    parser.add_argument("--max-words", type=int, help="Maximum word count per line")
    parser.add_argument("--max-chars", type=int, help="Maximum characters per line")

    parser.add_argument(
        "-c",
        "--category",
        choices=[
            "aya",
            "hadith",
            "phrase",
            "proverb",
            "poem",
            "paragraph",
            "word",
            "text",
            "nonsense",
        ],
        default="text",
        help="Category of text to generate",
    )
    parser.add_argument(
        "-n",
        "--number",
        type=int,
        default=1,
        help="Number of lines to generate (for sample or nonsense)",
    )
    parser.add_argument("--vocalized", action="store_true", help="Use vocalized text")

    args = parser.parse_args()

    if args.category == "nonsense":
        lines = arrandom.rand_sentences(args.number)
        for line in lines:
            print(line)
    elif args.number == 1:
        # Use category-specific function for single line
        func_map = {
            "aya": arrandom.aya,
            "hadith": arrandom.hadith,
            "phrase": arrandom.phrase,
            "proverb": arrandom.proverb,
            "poem": arrandom.poem,
            "paragraph": arrandom.paragraph,
            "word": arrandom.word,
            "text": arrandom.select,
        }
        func = func_map.get(args.category, arrandom.select)
        print(func(vocalized=args.vocalized))
    else:
        # Use sample() for multiple lines
        lines = arrandom.sample(args.category, args.number, args.vocalized,
                                min_words=args.min_words,
    max_words=args.max_words,
    max_chars=args.max_chars,)
        for line in lines:
            print(line)


if __name__ == "__main__":
    main()
