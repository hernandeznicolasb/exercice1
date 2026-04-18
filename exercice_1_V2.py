BLOCK_WIDTH = 100

sentences = {
    1: {"text": "Le code propre facilite la maintenance",       "visible": True},
    2: {"text": "Tester souvent évite beaucoup d erreurs",      "visible": True},
    3: {"text": "Cette phrase ne doit pas s afficher",          "visible": True},
    4: {"text": "Cette phrase ne doit pas s afficher",          "visible": False},
    5: {"text": "Un bon code doit rester simple et clair",      "visible": False},
    6: {"text": "La simplicité améliore la qualité du code",    "visible": True},
    7: {"text": "Refactoriser améliore la compréhension",       "visible": True},
}

blocks = [
    [1],
    [2, 4],
    [3, 5, 6, 7],
]


def print_block(keys):
    spacebetweenline = BLOCK_WIDTH - 2  # espace entre les deux '|'
    print("|" + "-" * spacebetweenline + "|")
    for key in keys:
        value = sentences[key]
        if value["visible"]:
            print("|" + " " * (spacebetweenline - len(value["text"])) + (value["text"].lower()) + "|")
    print("|" + "-" * spacebetweenline + "|")


def display_all_blocks():
    for i, block in enumerate(blocks):
        print_block(block)
        if i < len(blocks) - 1:
            print()


display_all_blocks()