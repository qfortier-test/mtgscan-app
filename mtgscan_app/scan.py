

def scan(image, path, azure, rec):
    box_texts = azure.image_to_box_texts(image)
    box_cards = rec.box_texts_to_cards(box_texts)
    rec.assign_stacked(box_texts, box_cards)
    if path:
        box_cards.save_image(image, path)
    deck = rec.box_texts_to_deck(box_texts)
    return deck
