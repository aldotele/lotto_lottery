class Prizes:
    # the following dictionary shows the amounts of bet combinations for each amount of matching numbers
    # the index within the list is the bet_type (e.g. amount at index 1 refers to number of ambata)
    # e.g. for 5 extracted numbers, the player might win 5 ambata, 10 ambo, 10 terno, 5 quaterna and 1 cinquina
    # e.g. for 10 extracted numbers, the player might win 10 ambata, 45 ambo, 10 terno, 210 quaterna and 252 cinquina
    combinations = {1: [None, 1],
                    2: [None, 2, 1],
                    3: [None, 3, 3, 1],
                    4: [None, 4, 6, 4, 1],
                    5: [None, 5, 10, 10, 5, 1],
                    6: [None, 6, 15, 20, 15, 6],
                    7: [None, 7, 21, 35, 35, 21],
                    8: [None, 8, 28, 56, 70, 56],
                    9: [None, 9, 36, 84, 126, 126],
                    10: [None, 10, 45, 120, 210, 252]}

    # the following dictionary shows GROSS payout combinations. (NET payout = GROSS - 0.08*GROSS)
    # each key is the amount of placed numbers and the index within the list is the bet_type
    # e.g. doing an ambata with 1 placed number will pay €11.23
    # e.g. doing a cinquina with 5 placed numbers will lead to maximum win of € 6 million
    # e.g. doing an ambata with 10 placed numbers will lead to minimum win of € 1.12
    prizes_table = {1: [None, 11.23],
                    2: [None, 5.61, 250],
                    3: [None, 3.74, 83.33, 4500],
                    4: [None, 2.80, 41.66, 1125, 120000],
                    5: [None, 2.24, 25, 450, 24000, 6000000],
                    6: [None, 1.87, 16.66, 225, 8000, 1000000],
                    7: [None, 1.60, 11.90, 128.57, 3428.57, 285714.28],
                    8: [None, 1.40, 8.92, 80.35, 1714.28, 107142.85],
                    9: [None, 1.24, 6.94, 53.57, 952.38, 47619.04],
                    10: [None, 1.12, 5.55, 37.50, 571.42, 23809.52]}












