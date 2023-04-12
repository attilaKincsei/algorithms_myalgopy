# https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle
# In javascript:
# function shuffle_array(deck) {
#     var j, x, i;  // i: the index of the clicked card (from 0 to X * 2).
#     for (i = deck.length - 1; i > 0; i--) {
#         j = Math.floor(Math.random() * (i + 1));
#         x = deck[i];
#         deck[i] = deck[j];
#         deck[j] = x;
#     }
#     return deck;
# }