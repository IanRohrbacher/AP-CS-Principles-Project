import pygame
import pygame.freetype
import random
import pickle

pygame.init()

restart = True

# uncomment below to reset the best score
# pickle.dump(0, open("best_score.p", "wb"))

while restart:
    # constants
    SCREEN_WIDTH = 375
    SCREEN_HEIGHT = 667
    SPACE = 0
    SPACE_TWO = 0
    count = 2
    ROUND = 13
    score_sum = 0
    move_over = 0
    add_more = 0
    add_more_two = 0
    move_over_two = 0
    all_dice = 0
    kind_count = 0
    scoreboard_lg_sm = 0
    more_bonus = 0
    locked_total = 0
    left_total = 0
    right_total = 0
    yahtzee_total = 0
    number_of_yahtzee = 0
    bonus_total = 0
    final_total = 0
    best_score = pickle.load(open("best_score.p", "rb"))
    best_text = "Best: "
    SIZE = SCREEN_WIDTH, SCREEN_HEIGHT
    SCREEN = pygame.display.set_mode(SIZE)
    DICE_GREEN = (91, 242, 70)
    DICE_RED = (240, 84, 84)
    READY = (16, 222, 72)
    UNREADY = (245, 0, 0)
    WHITE = (232, 232, 232)
    BLACK = (34, 40, 49)
    GREY = (163, 163, 163)
    BLUE = (25, 141, 230)
    ROLL = (211, 9, 234)
    FONT = pygame.freetype.SysFont('Comic Sans MS', 50)
    SMALL_FONT = pygame.freetype.SysFont('Comic Sans MS', 35)
    SMALLER_FONT = pygame.freetype.SysFont('Comic Sans MS', 20)
    SMALLISH_FONT = pygame.freetype.SysFont('Comic Sans MS', 30)
    SMALLEST_FONT = pygame.freetype.SysFont('Comic Sans MS', 10)
    running = False
    start = True
    startup = True
    run_game = False
    game_end = False
    next_round = False
    first_yahtzee = False
    end_turn_switch = False
    selected = False
    bonus_flip = False
    yahtzee_if_true = False
    yahtzee_feature = True
    once = True
    restart = False

    # lists of positions
    # list of positions for the five dice
    dice_positions = [((SCREEN_WIDTH / 4 * 1.5 - 30), (SCREEN_HEIGHT / 4 * 3 - 30), 60, 60),
                      ((SCREEN_WIDTH / 4 * 2.5 - 30), (SCREEN_HEIGHT / 4 * 3 - 30), 60, 60),
                      ((SCREEN_WIDTH / 4 - 30), (SCREEN_HEIGHT / 8 * 7 - 30), 60, 60),
                      ((SCREEN_WIDTH / 4 * 2 - 30), (SCREEN_HEIGHT / 8 * 7 - 30), 60, 60),
                      ((SCREEN_WIDTH / 4 * 3 - 30), (SCREEN_HEIGHT / 8 * 7 - 30), 60, 60)]

    # list of positions for the five dice
    number_positions = [((SCREEN_WIDTH / 4 * 1.5 - 13), (SCREEN_HEIGHT / 4 * 3 - 20), 60, 60),
                        ((SCREEN_WIDTH / 4 * 2.5 - 13), (SCREEN_HEIGHT / 4 * 3 - 20), 60, 60),
                        ((SCREEN_WIDTH / 4 - 13), (SCREEN_HEIGHT / 8 * 7 - 20), 60, 60),
                        ((SCREEN_WIDTH / 4 * 2 - 13), (SCREEN_HEIGHT / 8 * 7 - 20), 60, 60),
                        ((SCREEN_WIDTH / 4 * 3 - 13), (SCREEN_HEIGHT / 8 * 7 - 20), 60, 60)]

    # lists of words
    # list to show if dice is red or green / red = true and green = false
    red_or_green = ["red", "red", "red", "red", "red"]

    # the score to see if it can be straights
    continue_score = [False, False, False, False, False, False]

    # for the score buttons to see if it is selected or not
    scoreboard_buttons_onoff = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    # lists of words for the scoreboard
    score_words_one = ["Aces", "Twos", "Threes", "Fours", "Fives", "Sixes", "Bonus"]
    score_words_two = ["3 of a Kind", "4 of a Kind", "Full House", "SM Straight", "LG Straight", "Chance", "Yahtzee"]
    score_words_under_one = ["Total of All Ones", "Total of All Twos", "Total of All Threes", "Total of All Fours",
                             "Total of All Fives", "Total of All Sixes", "If 1-6 > 62 Score 35"]
    score_words_under_two = ["Total of All Dice", "Total of All Dice", "Score 25", "Score 30", "Score 40",
                             "Add All Dice",
                             "Bonus Yahtzee"]

    # list for number storage
    # list to store the dice numbers
    dice_number = [0, 0, 0, 0, 0]

    # list to store 3, 4, and 5 of a kind
    number_count = [0, 0, 0, 0, 0, 0, 0]

    # shapes
    # shape constants
    start_button = pygame.Rect((SCREEN_WIDTH / 2) - (250 / 2), SCREEN_HEIGHT / 2 - 30, 250, 60)
    roll_button = pygame.Rect(SCREEN_WIDTH / 4 - 77.5, SCREEN_HEIGHT / 50 * 29, 155, 60)
    end_turn = pygame.Rect(SCREEN_WIDTH / 4 * 3 - 77.5, SCREEN_HEIGHT / 50 * 29, 155, 60)
    restart_button = pygame.Rect((SCREEN_WIDTH / 6), (SCREEN_HEIGHT / 5) + 360, 118, 50)
    quit_button = pygame.Rect((SCREEN_WIDTH / 6) * 3 + 7, (SCREEN_HEIGHT / 5) + 360, 118, 50)
    # image
    background = pygame.image.load("using.png")
    # the five dice
    dice_rect_one = pygame.Rect(dice_positions[0])
    dice_rect_two = pygame.Rect(dice_positions[1])
    dice_rect_three = pygame.Rect(dice_positions[2])
    dice_rect_four = pygame.Rect(dice_positions[3])
    dice_rect_five = pygame.Rect(dice_positions[4])
    # the 13 buttons in the scoreboard and there numbers
    scoreboard_positions = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    scoreboard_numbers = [0, 0, 0, 0, 0, 0, "X", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    locked_scoreboard_numbers = [0, 0, 0, 0, 0, 0, "X", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    add_to_list = 21
    for f in range(6):
        scoreboard_positions[f] = ((SCREEN_WIDTH / 2 - 40), (int(add_to_list)), 35, 35)
        SPACE += 46
        add_to_list = (21 + SPACE)
    SPACE = 0
    add_to_list = 21
    for g in range(6):
        scoreboard_positions[g + 6] = ((SCREEN_WIDTH - 55), (int(add_to_list)), 35, 35)
        SPACE += 46
        add_to_list = (21 + SPACE)
    SPACE = 0
    ACES = pygame.Rect(scoreboard_positions[0])
    TWOS = pygame.Rect(scoreboard_positions[1])
    THREES = pygame.Rect(scoreboard_positions[2])
    FOURS = pygame.Rect(scoreboard_positions[3])
    FIVES = pygame.Rect(scoreboard_positions[4])
    SIXES = pygame.Rect(scoreboard_positions[5])
    THREE_KIND = pygame.Rect(scoreboard_positions[6])
    FOUR_KIND = pygame.Rect(scoreboard_positions[7])
    FULL_HOUSE = pygame.Rect(scoreboard_positions[8])
    SM_STRAIGHT = pygame.Rect(scoreboard_positions[9])
    LG_STRAIGHT = pygame.Rect(scoreboard_positions[10])
    CHANCE = pygame.Rect(scoreboard_positions[11])
    YAHTZEE = pygame.Rect(SCREEN_WIDTH - 55, 297, 35, 35)
    YAHTZEEB1 = pygame.Rect(SCREEN_WIDTH - 96, 297, 17.5, 17.5)
    YAHTZEEB2 = pygame.Rect(SCREEN_WIDTH - 96, 315, 17.5, 17.5)
    YAHTZEEB3 = pygame.Rect(SCREEN_WIDTH - 78, 297, 17.5, 17.5)
    YAHTZEEB4 = pygame.Rect(SCREEN_WIDTH - 78, 315, 17.5, 17.5)
    BONUS = pygame.Rect((SCREEN_WIDTH / 2 - 40), 297, 35, 35)

    # list for conveniences
    dice_rect = [dice_rect_one, dice_rect_two, dice_rect_three, dice_rect_four, dice_rect_five]
    scoreboard_buttons = [ACES, TWOS, THREES, FOURS, FIVES, SIXES, BONUS, THREE_KIND, FOUR_KIND, FULL_HOUSE,
                          SM_STRAIGHT,
                          LG_STRAIGHT, CHANCE, YAHTZEE, YAHTZEEB1, YAHTZEEB2, YAHTZEEB3, YAHTZEEB4]

    # functions
    def score16():
        global score_sum, kind_count
        # print("score16 running")
        for d in range(7):
            for k in range(5):
                if dice_number[k] == d:
                    #                print("yes " + str(d))
                    score_sum += d
                    kind_count += 1
                scoreboard_numbers[d - 1] = score_sum
                number_count[d - 1] = kind_count
            kind_count = 0
            score_sum = 0


    def _345kind():
        global number_count, kind_count, all_dice, yahtzee_if_true
        # print("_345kind running")
        for n in range(6):
            if number_count[n] == 3 or number_count[n] == 4 or number_count[n] == 5:
                scoreboard_numbers[7] = all_dice
            if number_count[n] == 4 or number_count[n] == 5:
                scoreboard_numbers[8] = all_dice
            if number_count[n] == 5:
                scoreboard_numbers[13] = 50
                yahtzee_if_true = True
        # print("Yahtzee If True: " + str(yahtzee_if_true))
        # print("Yahtzee: " + str(yahtzee))
        # print("Number Count: " + str(number_count))
        kind_count = 0


    def smlg_straight():
        global scoreboard_lg_sm, continue_score, dice_number
        # print("smlg_straight running")
        sorted_dice = dice_number.copy()
        sorted_dice.sort()
        print(str(sorted_dice) + " Sorted Dice")
        for s in range(6):
            for u in range(5):
                if sorted_dice[u] == 1:
                    continue_score[0] = True
                if sorted_dice[u] == 2 and (continue_score[0] or not continue_score[0]):
                    continue_score[1] = True
                if sorted_dice[u] == 3 and (continue_score[1] or not continue_score[1]):
                    continue_score[2] = True
                if sorted_dice[u] == 4 and continue_score[2]:
                    continue_score[3] = True
                if sorted_dice[u] == 5 and continue_score[3]:
                    continue_score[4] = True
                if sorted_dice[u] == 6 and continue_score[4]:
                    continue_score[5] = True
            for q in range(6):
                if continue_score[q]:
                    scoreboard_lg_sm += 1
                elif not continue_score[q] and not (scoreboard_lg_sm == 4 or scoreboard_lg_sm == 5):
                    scoreboard_lg_sm = 0
                # print(scoreboard_lg_sm)
            if scoreboard_lg_sm == 4:
                scoreboard_numbers[10] = 30
            if scoreboard_lg_sm == 5:
                scoreboard_numbers[11] = 40
                scoreboard_numbers[10] = 30
            # print(continue_score)
            continue_score = [False, False, False, False, False, False]
            scoreboard_lg_sm = 0
        # print(scoreboard_lg_sm)
        # print(continue_score)


    def full_house():
        global number_count, all_dice
        # print("full_house running")
        for i in range(6):
            if number_count[i] == 3:
                for m in range(6):
                    if number_count[m] == 2:
                        scoreboard_numbers[9] = 25
        #    print(number_count)
        number_count = [0, 0, 0, 0, 0, 0, 0]
        all_dice = 0


    def chance():
        global all_dice
        # print("chance running")
        for h in range(5):
            all_dice += dice_number[h]
        scoreboard_numbers[12] = all_dice


    def bonus_yahtzee_feature():
        global yahtzee_feature, event, run_game, next_round, running, ROUND, once, all_dice
        while yahtzee_feature:
            for o in range(7):
                if dice_number[0] == o:
                    if scoreboard_buttons_onoff[o - 1] == 1:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()

                        if scoreboard_buttons_onoff[7] == 1 and scoreboard_buttons_onoff[8] == 1 and \
                                scoreboard_buttons_onoff[9] == 1 and scoreboard_buttons_onoff[10] == 1 and \
                                scoreboard_buttons_onoff[11] == 1 and scoreboard_buttons_onoff[11] == 1:
                            if scoreboard_buttons_onoff[0] == 1 and scoreboard_buttons_onoff[1] == 1 and \
                                    scoreboard_buttons_onoff[2] == 1 and scoreboard_buttons_onoff[3] == 1 and \
                                    scoreboard_buttons_onoff[4] == 1 and scoreboard_buttons_onoff[5] == 1:
                                yahtzee_feature = False
                            else:
                                print("zero")

                                for v in range(6):
                                    if scoreboard_buttons_onoff[v] != 1:
                                        highlight_on(scoreboard_numbers[v], v)

                                for h in range(6):
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        if pygame.Rect.collidepoint(scoreboard_buttons[h], pygame.mouse.get_pos()):
                                            if not scoreboard_buttons_onoff[h] == 1:
                                                for m in range(6):
                                                    if not scoreboard_buttons_onoff[m] == 1:
                                                        highlight_off(m)
                                                        highlight_on(scoreboard_numbers[h], h)
                                                        yahtzee_feature = False

                        else:
                            print("Right Side Function")
                            for j in range(6):
                                if scoreboard_buttons_onoff[7 + j] != 1:
                                    scoreboard_numbers[9] = 25
                                    scoreboard_numbers[10] = 30
                                    scoreboard_numbers[11] = 40
                                    highlight_on(scoreboard_numbers[7 + j], (7 + j))

                            for s in range(6):
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    if pygame.Rect.collidepoint(scoreboard_buttons[7 + s], pygame.mouse.get_pos()):
                                        if not scoreboard_buttons_onoff[7 + s] == 1:
                                            for k in range(6):
                                                if not scoreboard_buttons_onoff[7 + k] == 1:
                                                    highlight_off(7 + k)

                                            scoreboard_numbers[9] = 25
                                            scoreboard_numbers[10] = 30
                                            scoreboard_numbers[11] = 40

                                            print(str(scoreboard_numbers) + " LOOOK")
                                            highlight_on(scoreboard_numbers[7 + s], (7 + s))
                                            yahtzee_feature = False

                    else:
                        print("Left Side Function")
                        highlight_on(scoreboard_numbers[o - 1], o - 1)

                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()

                            if event.type == pygame.MOUSEBUTTONDOWN:
                                if pygame.Rect.collidepoint(scoreboard_buttons[o - 1], pygame.mouse.get_pos()):
                                    yahtzee_feature = False


    def yahtzee_shift():
        global first_yahtzee, more_bonus, number_of_yahtzee
        if number_of_yahtzee < 4:
            if first_yahtzee and yahtzee_if_true:
                bonus_yahtzee_feature()
                number_of_yahtzee += 1
            elif locked_scoreboard_numbers[13] == 50:
                first_yahtzee = True
        print(str(first_yahtzee) + " First Yahtzee")


    def bonus():
        global bonus_flip, locked_total
        for w in range(6):
            locked_total += int(locked_scoreboard_numbers[w])
            # print(str(locked_scoreboard_numbers[w]) + " Adding Locked Total")
            if locked_total > 62:
                bonus_flip = True
        # print(str(locked_total) + " Locked Total")
        # print(str(bonus_flip) + " Bonus Flip")
        locked_total = 0


    def add_total():
        global scoreboard_positions
        score16()
        chance()
        smlg_straight()
        _345kind()
        full_house()
        bonus()
        print(scoreboard_numbers)


    def render_score():
        global SPACE, move_over, add_more, scoreboard_buttons_onoff, bonus_flip, SPACE_TWO, move_over_two, add_more_two
        SPACE = 0
        for j in range(2):
            for v in range(7):
                pygame.draw.rect(SCREEN, WHITE, scoreboard_buttons[v + add_more])
                if v + add_more == 6:
                    if not bonus_flip:
                        SMALLER_FONT.render_to(SCREEN, ((SCREEN_WIDTH / 2 - 32) + move_over, 30 + SPACE),
                                               str(locked_scoreboard_numbers[v + add_more]), (255, 0, 0))
                    elif bonus_flip:
                        locked_scoreboard_numbers[6] = 35
                        pygame.draw.lines(SCREEN, (0, 255, 0), False, (
                            (SCREEN_WIDTH / 2 - 32, 40 + SPACE),
                            (SCREEN_WIDTH / 2 - 27, 50 + SPACE),
                            (SCREEN_WIDTH / 2 - 17, 30 + SPACE)
                        ), width=3)
                elif scoreboard_buttons_onoff[v + add_more] == 0:
                    SMALLER_FONT.render_to(SCREEN, ((SCREEN_WIDTH / 2 - 32) + move_over, 30 + SPACE),
                                           str(scoreboard_numbers[v + add_more]), GREY)
                elif scoreboard_buttons_onoff[v + add_more] == 2 or scoreboard_buttons_onoff[v + add_more] == 1:
                    SMALLER_FONT.render_to(SCREEN, ((SCREEN_WIDTH / 2 - 32) + move_over, 30 + SPACE),
                                           str(locked_scoreboard_numbers[v + add_more]), BLACK)
                if v < 2:
                    # print(str(scoreboard_buttons_onoff) + " scoreboard_buttons_onoff")
                    if scoreboard_buttons_onoff[v + 14 + add_more_two] == 0 and not yahtzee_if_true and first_yahtzee:
                        pygame.draw.lines(SCREEN, UNREADY, False, (
                            (SCREEN_WIDTH - (91.5 - move_over_two), SCREEN_HEIGHT / 2 - (26 - SPACE_TWO)),
                            (SCREEN_WIDTH - (88.5 - move_over_two), SCREEN_HEIGHT / 2 - (23 - SPACE_TWO)),
                            (SCREEN_WIDTH - (83.5 - move_over_two), SCREEN_HEIGHT / 2 - (33 - SPACE_TWO))
                        ), width=2)
                    elif scoreboard_buttons_onoff[v + 14 + add_more_two] == 0 and yahtzee_if_true and first_yahtzee:
                        pygame.draw.lines(SCREEN, GREY, False, (
                            (SCREEN_WIDTH - (91.5 - move_over_two), SCREEN_HEIGHT / 2 - (26 - SPACE_TWO)),
                            (SCREEN_WIDTH - (88.5 - move_over_two), SCREEN_HEIGHT / 2 - (23 - SPACE_TWO)),
                            (SCREEN_WIDTH - (83.5 - move_over_two), SCREEN_HEIGHT / 2 - (33 - SPACE_TWO))
                        ), width=2)
                    elif scoreboard_buttons_onoff[v + 14 + add_more_two] == 2 \
                            or scoreboard_buttons_onoff[v + 14 + add_more_two] == 1:
                        pygame.draw.lines(SCREEN, READY, False, (
                            (SCREEN_WIDTH - (91.5 - move_over_two), SCREEN_HEIGHT / 2 - (26 - SPACE_TWO)),
                            (SCREEN_WIDTH - (88.5 - move_over_two), SCREEN_HEIGHT / 2 - (23 - SPACE_TWO)),
                            (SCREEN_WIDTH - (83.5 - move_over_two), SCREEN_HEIGHT / 2 - (33 - SPACE_TWO))
                        ), width=2)
                SPACE += 46
                SPACE_TWO += 18
            SPACE = 0
            SPACE_TWO = 0
            move_over = 173
            add_more = 7
            add_more_two = 2
            move_over_two = 18
        add_more = 0
        add_more_two = 0
        move_over = 0
        move_over_two = 0
        pygame.display.flip()


    def highlight(diceNumber, on_or_off):
        global SPACE, move_over, add_more, first_yahtzee
        pygame.draw.rect(SCREEN, WHITE, scoreboard_buttons[diceNumber])
        if diceNumber < 14:
            for j in range(2):
                for v in range(7):
                    if on_or_off and diceNumber == (v + add_more):
                        # print("highlight")
                        pygame.draw.rect(SCREEN, (233, 255, 50), scoreboard_buttons[diceNumber])
                        SMALLER_FONT.render_to(SCREEN, ((SCREEN_WIDTH / 2 - 32) + move_over, 30 + SPACE),
                                               str(scoreboard_numbers[v + add_more]), BLACK)
                    elif not on_or_off and diceNumber == (v + add_more):
                        # print("unhighlight")
                        pygame.draw.rect(SCREEN, WHITE, scoreboard_buttons[diceNumber])
                        SMALLER_FONT.render_to(SCREEN, ((SCREEN_WIDTH / 2 - 32) + move_over, 30 + SPACE),
                                               str(scoreboard_numbers[v + add_more]), GREY)
                    SPACE += 46
                SPACE = 0
                move_over = 173
                add_more = 7
        elif diceNumber > 13 and first_yahtzee and yahtzee_if_true:
            for k in range(2):
                for d in range(2):
                    if on_or_off and diceNumber == d + add_more + 14:
                        # print("highlight")
                        pygame.draw.rect(SCREEN, (233, 255, 50), scoreboard_buttons[diceNumber])
                        pygame.draw.lines(SCREEN, BLACK, False, (
                            (SCREEN_WIDTH - (91.5 - move_over), SCREEN_HEIGHT / 2 - (26 - SPACE)),
                            (SCREEN_WIDTH - (88.5 - move_over), SCREEN_HEIGHT / 2 - (23 - SPACE)),
                            (SCREEN_WIDTH - (83.5 - move_over), SCREEN_HEIGHT / 2 - (33 - SPACE))
                        ), width=2)
                    elif not on_or_off and diceNumber == d + add_more + 14:
                        # print("unhighlight")
                        pygame.draw.rect(SCREEN, WHITE, scoreboard_buttons[diceNumber])
                        pygame.draw.lines(SCREEN, GREY, False, (
                            (SCREEN_WIDTH - (91.5 - move_over), SCREEN_HEIGHT / 2 - (26 - SPACE)),
                            (SCREEN_WIDTH - (88.5 - move_over), SCREEN_HEIGHT / 2 - (23 - SPACE)),
                            (SCREEN_WIDTH - (83.5 - move_over), SCREEN_HEIGHT / 2 - (33 - SPACE))
                        ), width=2)
                    SPACE += 18
                SPACE = 0
                add_more = 2
                move_over = 18
        add_more = 0
        move_over = 0
        pygame.display.flip()


    def dice(number, color):
        pygame.draw.rect(SCREEN, color, dice_rect[number])
        if str(color) == "(237, 80, 96)":
            red_or_green[number] = "red"
        if str(color) == "(91, 242, 70)":
            red_or_green[number] = "green"


    def rolling():
        global dice_number
        for i in range(5):
            if red_or_green[i] == "red":
                dice(i, DICE_RED)
                random_number = random.randint(1, 6)
                if random_number == dice_number[i]:
                    add_or_subtract = random.randint(1, 2)
                    # print(add_or_subtract)
                    if random_number == 6:
                        random_number -= 1
                    elif random_number == 1:
                        random_number += 1
                    elif add_or_subtract == 1:
                        random_number += 1
                    elif add_or_subtract == 2:
                        random_number -= 1
                FONT.render_to(SCREEN, number_positions[i], str(random_number), BLACK)
                dice_number[i] = random_number
                pygame.display.flip()


    def rolling_animation():
        global sudo_random_number, dice_number
        for n in range(10):
            pygame.time.wait(100)
            rolling()
        add_total()


    def change_color(number):
        if red_or_green[number] == "red":
            pygame.draw.rect(SCREEN, DICE_GREEN, dice_rect[number])
            red_or_green[number] = "green"
        else:
            pygame.draw.rect(SCREEN, DICE_RED, dice_rect[number])
            red_or_green[number] = "red"
        FONT.render_to(SCREEN, number_positions[number], str(dice_number[number]), BLACK)
        pygame.display.flip()


    def blank_scoreboard():
        global SPACE
        # main scoreboard
        pygame.draw.lines(SCREEN, BLACK, True, ((15, 15), (SCREEN_WIDTH - 15, 15), (SCREEN_WIDTH - 15, 336), (15, 336)))
        for a in range(7):
            pygame.draw.line(SCREEN, BLACK, (15, 15 + SPACE), (SCREEN_WIDTH - 15, 15 + SPACE))
            SMALLER_FONT.render_to(SCREEN, (23, 24 + SPACE), score_words_one[a], BLACK)
            SMALLEST_FONT.render_to(SCREEN, (23 + 15, 45 + SPACE), score_words_under_one[a], BLACK)
            SMALLER_FONT.render_to(SCREEN, (SCREEN_WIDTH / 2 + 5, 24 + SPACE), score_words_two[a], BLACK)
            SMALLEST_FONT.render_to(SCREEN, (SCREEN_WIDTH / 2 + 15, 45 + SPACE), score_words_under_two[a], BLACK)
            pygame.draw.lines(SCREEN, BLACK, True, (
                (SCREEN_WIDTH / 2 - 41, 20 + SPACE), (SCREEN_WIDTH / 2 - 5, 20 + SPACE),
                (SCREEN_WIDTH / 2 - 5, 56 + SPACE),
                (SCREEN_WIDTH / 2 - 41, 56 + SPACE)))
            pygame.draw.lines(SCREEN, BLACK, True, (
                (SCREEN_WIDTH - 56, 20 + SPACE), (SCREEN_WIDTH - 20, 20 + SPACE), (SCREEN_WIDTH - 20, 56 + SPACE),
                (SCREEN_WIDTH - 56, 56 + SPACE)))
            SPACE += 46
        pygame.draw.line(SCREEN, BLACK, (SCREEN_WIDTH / 2, 15), (SCREEN_WIDTH / 2, 336))
        pygame.draw.lines(SCREEN, BLACK, True, (
            (SCREEN_WIDTH - 97, 296),
            (SCREEN_WIDTH - 61, 296),
            (SCREEN_WIDTH - 61, 332),
            (SCREEN_WIDTH - 97, 332)))
        pygame.draw.line(SCREEN, BLACK, (SCREEN_WIDTH - 97, 314), (SCREEN_WIDTH - 61, 314))
        pygame.draw.line(SCREEN, BLACK, (SCREEN_WIDTH - 79, 296), (SCREEN_WIDTH - 79, 332))
        # scoreboard buttons
        for r in range(14):
            if scoreboard_buttons_onoff[r] == 0:
                pygame.draw.rect(SCREEN, WHITE, scoreboard_buttons[r])
            for u in range(4):
                # 1 top left/2 bottom left/3 top right/4 bottom right
                pygame.draw.rect(SCREEN, WHITE, scoreboard_buttons[14 + u])


    def highlight_on(locked_score, number):
        global end_turn_switch, selected
        end_turn_switch = True
        pygame.draw.rect(SCREEN, READY, end_turn)
        SMALL_FONT.render_to(SCREEN, (SCREEN_WIDTH / 4 * 3 - 74, SCREEN_HEIGHT / 100 * 60), "End Turn",
                             BLACK)
        scoreboard_buttons_onoff[number] = 2
        locked_scoreboard_numbers[number] = locked_score
        selected = True
        highlight(number, True)


    def highlight_off(number):
        global end_turn_switch, selected
        end_turn_switch = False
        pygame.draw.rect(SCREEN, UNREADY, end_turn)
        SMALL_FONT.render_to(SCREEN, (SCREEN_WIDTH / 4 * 3 - 74, SCREEN_HEIGHT / 100 * 60,), "End Turn",
                             BLACK)
        scoreboard_buttons_onoff[number] = 0
        locked_scoreboard_numbers[number] = 0
        highlight(number, False)
        selected = False


    def check_for_scoreboard(q):
        global locked_scoreboard_numbers, scoreboard_numbers, selected, yahtzee_if_true
        if q != 6:
            if q < 14:
                if not selected:
                    if scoreboard_buttons_onoff[q] == 0:
                        highlight_on(scoreboard_numbers[q], q)
                elif selected:
                    if scoreboard_buttons_onoff[q] == 2:
                        highlight_off(q)
                    elif scoreboard_buttons_onoff[q] == 0:
                        for e in range(18):
                            if scoreboard_buttons_onoff[e] == 2:
                                highlight_off(e)
                                highlight_on(scoreboard_numbers[q], q)
                # print(str(scoreboard_buttons_onoff) + " ON OFF ONE")
                # print(str(locked_scoreboard_numbers) + " Locked Scoreboard Numbers")
            if first_yahtzee and yahtzee_if_true and q > 13:
                if not selected:
                    if scoreboard_buttons_onoff[q] == 0:
                        highlight_on(100, q)
                        # print("ready " + str(scoreboard_buttons_onoff))
                elif selected:
                    if scoreboard_buttons_onoff[q] == 2:
                        highlight_off(q)
                    elif scoreboard_buttons_onoff[q] == 0:
                        for e in range(18):
                            if scoreboard_buttons_onoff[e] == 2:
                                highlight_off(e)
                                highlight_on(100, q)
                        # print("not ready " + str(scoreboard_buttons_onoff))
                # print(selected)
            print(str(locked_scoreboard_numbers) + " Locked Scoreboard Numbers")
            print(str(scoreboard_numbers) + " Scoreboard Numbers")
            print(str(scoreboard_buttons_onoff) + " scoreboard_buttons_onoff")
        pygame.display.flip()


    def end_screen():
        global SCREEN_WIDTH, SCREEN_HEIGHT, locked_scoreboard_numbers, left_total, right_total, yahtzee_total, \
            bonus_flip, bonus_total, final_total, best_score, best_text
        bonus()
        render_score()
        # end screen transplant
        size = (((SCREEN_WIDTH / 3 * 2) + 25), ((SCREEN_HEIGHT / 3 * 2) + 25))
        end_square = pygame.Surface(size)
        end_square.set_alpha(185)
        pygame.draw.rect(end_square, BLACK, end_square.get_rect(), 1)
        SCREEN.blit(end_square, (((SCREEN_WIDTH / 2) - (((SCREEN_WIDTH / 3 * 2) + 25) / 2)),
                                 ((SCREEN_HEIGHT / 2) - (((SCREEN_HEIGHT / 3 * 2) + 25) / 2))))

        # getting and showing totals
        for s in range(6):
            left_total += locked_scoreboard_numbers[s]
        for o in range(6):
            right_total += locked_scoreboard_numbers[o + 7]
        for q in range(5):
            yahtzee_total += locked_scoreboard_numbers[q + 13]
        if bonus_flip:
            bonus_total = 35
        final_total = (left_total + right_total + yahtzee_total + bonus_total)

        if int(final_total) > int(best_score):
            best_score = final_total
            best_text = "New Best: "
            pickle.dump(int(best_score), open("best_score.p", "wb"))

        distance = 65
        SMALL_FONT.render_to(SCREEN, ((SCREEN_WIDTH / 6), SCREEN_HEIGHT / 6),
                             "Left Total: " + str(left_total), (255, 255, 255))
        SMALL_FONT.render_to(SCREEN, ((SCREEN_WIDTH / 6), (SCREEN_HEIGHT / 6) + distance),
                             "Right Total: " + str(right_total), (255, 255, 255))
        SMALL_FONT.render_to(SCREEN, ((SCREEN_WIDTH / 6), (SCREEN_HEIGHT / 6) + (distance * 2)),
                             "Bonus: " + str(bonus_total), (255, 255, 255))
        SMALL_FONT.render_to(SCREEN, ((SCREEN_WIDTH / 6), (SCREEN_HEIGHT / 6) + (distance * 3)),
                             "Yahtzees: " + str(yahtzee_total), (255, 255, 255))
        SMALL_FONT.render_to(SCREEN, ((SCREEN_WIDTH / 6), (SCREEN_HEIGHT / 6) + (distance * 4)),
                             "Total: " + str(final_total), (255, 255, 255))
        SMALL_FONT.render_to(SCREEN, ((SCREEN_WIDTH / 6), (SCREEN_HEIGHT / 6) + (distance * 5)),
                             str(best_text) + str(best_score), (255, 255, 255))

        # buttons to end or restart
        pygame.draw.rect(SCREEN, BLUE, restart_button)
        pygame.draw.rect(SCREEN, BLUE, quit_button)
        SMALLISH_FONT.render_to(SCREEN, ((SCREEN_WIDTH / 5) - 7, (SCREEN_HEIGHT / 5) + 372, 118, 50),
                                "Restart", (255, 255, 255))
        SMALL_FONT.render_to(SCREEN, ((SCREEN_WIDTH / 6) * 3 + 27, (SCREEN_HEIGHT / 5) + 370, 118, 50),
                             "Quit", (255, 255, 255))

        pygame.display.flip()


    SCREEN.blit(background, (0, 0))
    pygame.draw.rect(SCREEN, BLACK, start_button)
    FONT.render_to(SCREEN, (SCREEN_WIDTH / 2 - 80, SCREEN_HEIGHT / 2 - 20), "START", WHITE)

    pygame.display.flip()
    # screen before ready to start

    while start:
        for event in pygame.event.get():
            # X closes the games window
            if event.type == pygame.QUIT:
                start = False

            # when click down check if its the start button, if not nothing happens
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.Rect.collidepoint(start_button, pygame.mouse.get_pos()):
                    run_game = True
                    start = False

    while run_game:
        while ROUND != 0:
            if ROUND != 0:
                running = True
                print("rounds left " + str(ROUND))

            while running:
                # top right X closes the games window
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run_game = False
                        running = False
                        ROUND = 0

                    if event.type == pygame.MOUSEBUTTONDOWN:

                        if pygame.Rect.collidepoint(roll_button, pygame.mouse.get_pos()):
                            if count != 0:
                                count -= 1

                                # lets you unselect what was highlighted when you roll
                                yahtzee_if_true = False
                                for y in range(18):
                                    if scoreboard_buttons_onoff[y] == 2:
                                        highlight_off(y)

                                # fixes the right side of the board
                                for t in range(5):
                                    scoreboard_numbers[7 + t] = 0
                                pygame.draw.rect(SCREEN, ROLL, roll_button)
                                FONT.render_to(SCREEN, (SCREEN_WIDTH / 4 - 75, SCREEN_HEIGHT / 100 * 59),
                                               "Rolls:" + str(count), BLACK)

                                pygame.time.wait(100)
                                rolling_animation()
                                render_score()

                        if pygame.Rect.collidepoint(end_turn, pygame.mouse.get_pos()):
                            # print("click end")
                            if end_turn_switch:
                                ROUND -= 1
                                yahtzee_shift()
                                pygame.draw.rect(SCREEN, UNREADY, end_turn)
                                SMALL_FONT.render_to(SCREEN, (SCREEN_WIDTH / 4 * 3 - 74, SCREEN_HEIGHT / 100 * 60,),
                                                     "End Turn", BLACK)
                                for y in range(18):
                                    if scoreboard_buttons_onoff[y] == 2:
                                        scoreboard_buttons_onoff[y] = 1
                                yahtzee_if_true = False
                                end_turn_switch = False
                                running = False
                                selected = False
                                yahtzee_feature = True
                                if ROUND == 0:
                                    game_end = True
                                else:
                                    next_round = True

                        for g in range(5):
                            if pygame.Rect.collidepoint(dice_rect[g], pygame.mouse.get_pos()):
                                change_color(g)
                                # print("click" + str(g))
                                # print(dice_number[g])

                        for p in range(18):
                            if pygame.Rect.collidepoint(scoreboard_buttons[p], pygame.mouse.get_pos()):
                                # print("click score " + str(p))
                                check_for_scoreboard(p)

                # screen setup
                while startup:
                    # background of the display
                    SCREEN.fill(WHITE)
                    # dice
                    dice(0, DICE_RED)
                    dice(1, DICE_RED)
                    dice(2, DICE_RED)
                    dice(3, DICE_RED)
                    dice(4, DICE_RED)
                    # scoreboard made from hand
                    blank_scoreboard()
                    # roll button
                    pygame.draw.rect(SCREEN, ROLL, roll_button)
                    FONT.render_to(SCREEN, (SCREEN_WIDTH / 4 - 75, SCREEN_HEIGHT / 100 * 59), "Rolls:" + str(count),
                                   BLACK)
                    pygame.draw.rect(SCREEN, UNREADY, end_turn)
                    SMALL_FONT.render_to(SCREEN, (SCREEN_WIDTH / 4 * 3 - 74, SCREEN_HEIGHT / 100 * 60,), "End Turn",
                                         BLACK)
                    # rolling for a time
                    rolling_animation()
                    render_score()
                    startup = False

                while next_round:
                    # resets the dice
                    dice(0, DICE_RED)
                    dice(1, DICE_RED)
                    dice(2, DICE_RED)
                    dice(3, DICE_RED)
                    dice(4, DICE_RED)
                    red_or_green = ["red", "red", "red", "red", "red"]
                    # resets the roll button
                    # TESTING BUT IT BACK TO 2 WHEN DONE
                    count = 2
                    pygame.draw.rect(SCREEN, ROLL, roll_button)
                    FONT.render_to(SCREEN, (SCREEN_WIDTH / 4 - 75, SCREEN_HEIGHT / 100 * 59),
                                   "Rolls:" + str(count), BLACK)
                    # resets the scoreboard
                    scoreboard_numbers = [0, 0, 0, 0, 0, 0, "X", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                    for x in range(18):
                        pygame.draw.rect(SCREEN, WHITE, scoreboard_buttons[x])
                    rolling_animation()
                    render_score()
                    next_round = False

        print("done game")
        print(str(game_end) + " Game End")
        once = True
        while game_end:
            if once:
                end_screen()
                once = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.Rect.collidepoint(restart_button, pygame.mouse.get_pos()):
                        restart = True
                        game_end = False
                        run_game = False

                    if pygame.Rect.collidepoint(quit_button, pygame.mouse.get_pos()):
                        pygame.quit()

pygame.quit()
