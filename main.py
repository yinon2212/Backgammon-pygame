import pygame, os, random
from Player import Player
from Board import Board
from Move import Move
from Turn import Turn
from Ai_player import Ai
from timeit import default_timer as timer

pygame.font.init()

FPS = 60

# Font
FONT = pygame.font.SysFont('timesnewroman',  30)

# The size f the window
WIDTH, HEIGHT = 1044, 581

# COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 242, 0)

# Piece positions for the start of the game for WHITE and RED
WHITE_PLACES = [(25, 20), (25, 76), (25, 132), (25, 188),
                (25, 56), (315, 486), (315, 430), (315, 374), (515, 486), (515, 430), (515, 374), (515, 318),
                (515, 450), (878, 20), (878, 76)]

RED_PLACES = [(25, 486), (25, 430), (25, 374), (25, 318), (25, 450), (310, 20), (310, 76), (310, 132),
              (518, 20), (518, 76), (518, 132), (518, 188), (518, 56), (875, 486), (875, 430)]


# Eaten pieces area
EATEN_AREA_X, EATEN_AREA_Y = 473, 100
EATEN_AREA_WIDTH, EATEN_AREA_HEIGHT = 40, 351


# Images
BOARD = pygame.image.load(os.path.join("images", "board.png"))
RED_PLAYER = pygame.image.load((os.path.join("images", "red.png")))
WHITE_PLAYER = pygame.image.load(os.path.join("images", "white.png"))

NO_MOVES_IMG = pygame.image.load((os.path.join("images", "nomoves.png")))
NO_MOVES_IMG_W, NO_MOVES_IMG_H = 740, 124


# Winner Images
WHITE_WINNER_IMG = pygame.image.load(os.path.join("images", "whitewinner.png"))
RED_WINNER_IMG = pygame.image.load(os.path.join("images", "redwinner.png"))
WINNER_IMG_WIDTH, WINNER_IMG_HEIGHT = 607, 119


# Cubes
CUBE1_X, CUBE1_Y = 983, 194
CUBE2_X, CUBE2_Y = 983, 250
CUBE_W, CUBE_H = 46, 40


# Organize components
ORGANIZE = [0, 0, 0, 5, 5, 7, -5, -5, -2, -2, -2, 0]

# Window
WIN = pygame.display.set_mode((WIDTH, HEIGHT))


pygame.display.set_caption("Backgammon")


def draw(board, turn, winner):
    WIN.blit(BOARD, (0, 0))

    if turn.red_turn:
        WIN.blit(FONT.render("Red", False, RED), (WIDTH - 60, 10))
    else:
        WIN.blit(FONT.render("White", False, WHITE), (WIDTH - 75, 10))

    cube1 = turn.cubes[0]
    cube2 = turn.cubes[1]
    current_cube = turn.chosen_cube

    if turn.source:
        source_row = turn.source.get_row_from()
        source_col = turn.source.get_col_from()
        stack = board.board[source_row][source_col]

        extra_x = 25
        y = 25
        height = 220
        if source_col > 5:
            extra_x = extra_x + 30
        if source_row == 1:
            y = 550
            height = y - height

        final_x = source_col * 75 + extra_x - ORGANIZE[source_col]
        # pygame.draw.rect(WIN, YELLOW, (source_col * 75 + extra_x, y, 75, 10))
        pygame.draw.polygon(WIN, GREEN, [(final_x, y), (final_x + 40 - ORGANIZE[source_col], height), (final_x + 75, y)])

    draw_pieces(board.board, board.red_player.get_pieces())
    draw_pieces(board.board, board.white_player.get_pieces())

    if cube1.get_played():
        pygame.draw.rect(WIN, RED, (CUBE1_X, CUBE1_Y, CUBE_W, CUBE_H))
    if turn.cubes[1].get_played():
        pygame.draw.rect(WIN, RED, (CUBE2_X, CUBE2_Y, CUBE_W, CUBE_H))

    if current_cube == 0:
        pygame.draw.rect(WIN, GREEN, (CUBE1_X, CUBE1_Y, CUBE_W, CUBE_H), 5)
    else:
        pygame.draw.rect(WIN, GREEN, (CUBE2_X, CUBE2_Y, CUBE_W, CUBE_H), 5)

    WIN.blit(FONT.render(str(cube1.get_value()), False, BLACK), (998, 197))
    WIN.blit(FONT.render(str(cube2.get_value()), False, BLACK), (998, 254))

    if turn.destination:
        dest = turn.destination.get("destination")
        extra_x = 25
        y = 20
        if dest.get_col_from() > 5:
            extra_x = extra_x + 30
        if dest.get_row_from() == 1:
            y = 530

        pygame.draw.rect(WIN, GREEN, (dest.get_col_from() * 75 + extra_x, y, 75, 10))

    if len(board.eaten_pieces.get("red")) > 0:
        draw_eaten_pieces(board.eaten_pieces.get("red"), "red")
    elif len(board.eaten_pieces.get("white")) > 0:
        draw_eaten_pieces(board.eaten_pieces.get("white"), "white")
    # pygame.draw.rect(WIN, WHITE, (EATEN_AREA_X, EATEN_AREA_Y, EATEN_AREA_WIDTH, EATEN_AREA_HEIGHT), 1)

    if winner:
        if winner[1] == "red":
            WIN.blit(RED_WINNER_IMG, (WIDTH / 2 - WINNER_IMG_WIDTH / 2, HEIGHT / 2 - 50))
        else:
            WIN.blit(WHITE_WINNER_IMG, (WIDTH / 2 - WINNER_IMG_WIDTH / 2, HEIGHT / 2 - 50))
    pygame.display.update()


def draw_pieces(board, pieces):
    for i in range(2):
        for j in range(len(pieces)):
            try:
                stack_pieces = board[i][j].get_all_stack_elements()
                color = stack_pieces[0].get_color()
                for piece in stack_pieces:
                    row_visual = piece.get_row_visual()
                    col_visual = piece.get_col_visual()
                    if color == "red":
                        WIN.blit(RED_PLAYER, (row_visual, col_visual))
                    else:
                        WIN.blit(WHITE_PLAYER, (row_visual, col_visual))

            except Exception as error:
                continue


def draw_eaten_pieces(eaten_pieces, color):
    piece_img = RED_PLAYER

    if color == "white":
        piece_img = WHITE_PLAYER

    for eaten in eaten_pieces:
        row_visual = eaten.get_row_visual()
        col_visual = eaten.get_col_visual()
        WIN.blit(piece_img, (row_visual, col_visual))


def draw_ai_path(ai_path, board, turn):
    for move in ai_path:
        row_dest = move[0].row_to
        col_dest = move[0].col_to
        eat_piece = move[1]

        if col_dest == -1:
            continue
        try:
            stack_dest = board.board[row_dest][col_dest]
            turn.set_source(move[0])
            turn.set_destination(Move(row_dest, col_dest), eat_piece, False)
            draw(board, turn, False)
            delay(1)
            board.make_move(move[0])
            turn.remove_destination()
            turn.remove_source()
            draw(board, turn, False)
        except IndexError:
            continue


# This function returns the number of cube that clicked, if it clicked
# and if not it returns -1
def clicked_on_cube(click_coordinates):
    x = click_coordinates[0]
    y = click_coordinates[1]

    if CUBE1_X < x < CUBE1_X + CUBE_W and CUBE1_Y < y < CUBE1_Y + CUBE_H:
        return 0
    elif CUBE2_X < x < CUBE2_X + CUBE_W and CUBE2_Y < y < CUBE2_Y + CUBE_H:
        return 1

    return -1


# Delay function
def delay(sec):
    start = timer()
    while timer() - start < sec:
        continue
    end = timer()
    print(end - start)  # Time in seconds, e.g. 5.38091952400282


def main():
    red_player = Player("red", RED_PLACES)  # Red player Object
    white_player = Player("white", WHITE_PLACES)  # White player Object
    board = Board(red_player, white_player)  # Board Object

    run = True
    waiting_for_enter = False  # This variable waits until the player choose an entrance when the enemy player has eaten for him pieces

    game_mode = input("Choose a game mode:\n1 - Human VS Human\n2 - Human VS Computer")

    turn = Turn(game_mode == "2")  # Turn Object
    ai_player = Ai("white", WHITE_PLACES, board, turn)
    if turn.ai_game:
        board.set_player("white", ai_player)

    while run:
        has_winner, winner = board.is_there_winner()
        all_in_home = board.are_all_pieces_in_home_for_player(turn.color)

        if turn.ai_game:
            if turn.ai_turn:
                print("AI is playing...")
                if all_in_home:
                    ai_player.set_all_home(True)
                print(turn.cubes[0], turn.cubes[1])
                ai_path = ai_player.play_ai_moves()
                draw_ai_path(ai_path, board, turn)
                turn.change_turn()
                print("AI Played...")
                continue

        if has_winner:  # If there is a winner
            draw(board, turn, [True, winner])
            start_ticks = pygame.time.get_ticks()  # Start ticking
            while run:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
                seconds = (pygame.time.get_ticks() - start_ticks) / 1000
                if seconds > 5:
                    run = False

        elif board.check_if_blocked(turn.cubes, turn.color, all_in_home):
            start_ticking = pygame.time.get_ticks()
            print("No available moves!!!!!!!!!!!!!!!!!!!!!!!!adsbhdjkabdhjsabdsjhabdhjsabdhjsabdhjasbhj")
            WIN.blit(NO_MOVES_IMG, (WIDTH / 2 - NO_MOVES_IMG_W / 2, HEIGHT / 2 - 50))
            delay(1)
            turn.change_turn()
            continue
        else:  # If there is no winner
            if len(board.eaten_pieces.get(turn.color)) > 0:  # If the enemy player has eaten pieces for the current player
                entrance_details = board.can_piece_entrances_to_column(turn.cubes[0].get_value(), turn.cubes[1].get_value(),
                                                                       turn.color)
                entrance1 = entrance_details[0]
                entrance2 = entrance_details[1]

                if entrance1.get("column") == -1:  # If  cube 1 is not available for entrance
                    turn.set_cube_played(0, True)
                    if turn.double_ind >= 0:  # If the cubes are double and the player cannot enter
                        for i in range(4):
                            turn.set_cube_played(i, True)

                if entrance2.get("column") == -1:  # If  cube 1 is not available for entrance
                    turn.set_cube_played(1, True)

                if turn.has_all_cubes_playes():  # If The player played with all the cubes
                    turn.change_turn()
                    continue
                else:
                    entrance = entrance_details[turn.chosen_cube]
                    turn.set_destination(Move(entrance.get("row"), entrance.get("column")), entrance.get("eat_piece"), False)
                    if len(turn.player_clicks) == 0:
                        waiting_for_enter = True

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                # handle MOUSEBUTTONUP
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    cube = clicked_on_cube(pos)
                    if cube != -1:  # If the player decide to choose cube
                        if turn.double_ind == -1:  # If the current turn is not a "Double Turn"
                            if turn.cubes[cube].get_played():  # If the cube has been played
                                cube = 3 - (2 + cube)
                            turn.set_chosen_cube(cube)
                    else:
                        col = int(pos[0] / 75)
                        row = int(pos[1] / 262)
                        if col > 5:
                            col = col - 1

                        if len(turn.player_clicks) < 1:  # If the player chose the source piece
                            move = Move(row, col)

                            if board.check_if_blocked(turn.cubes, turn.color, all_in_home):  # If the player has not available moves
                                WIN.blit(FONT.render("You have No Option To Move, Wait For The Next Turn!", False, GREEN),
                                         (WIDTH / 2 - 50, HEIGHT / 2))

                                turn.change_turn()
                                continue

                            if waiting_for_enter:  # If the player has eaten pieces, so the program wait for him to choose which entrance he would like to enter
                                temp = turn.destination.get("destination")
                                if temp.get_row_from() == move.get_row_from() and temp.get_col_from() == move.get_col_from():

                                    board.return_eaten_piece_to_game(turn.color, turn.destination)
                                    turn.set_cube_played(turn.chosen_cube, True)
                                    waiting_for_enter = False
                                    turn.set_source(None)
                                    turn.remove_destination()

                                    if turn.double_ind >= 0:
                                        turn.increase_double_index()

                                    if turn.has_all_cubes_playes():  # If the player played with all the cubes
                                        turn.change_turn()
                                        turn.clear_clicks()

                            else:
                                temp = board.get_destination(turn.color, move, turn.get_number_of_steps())
                                move.set_row_col_to(temp.get_row_from(), temp.get_col_from())
                                turn.add_click(move)

                                source_legal, piece_eat = board.is_source_legal(turn.color, move, all_in_home)
                                if source_legal:  # If the source is legal
                                    out_own_piece = False
                                    if move.get_col_to() > 11:
                                        out_own_piece = True
                                        move.set_row_col_to(move.get_row_to(), 12)
                                    turn.set_source(move)
                                    turn.set_destination(Move(move.row_to, move.col_to), piece_eat, out_own_piece)
                                else:
                                    turn.clear_clicks()
                                    turn.set_source(None)
                                    turn.remove_destination()

                        else:   # If the player chose the destination area
                            if board.is_destination_legal(Move(row, col), move):  # If the chosen destination area is the correct one
                                current_cube = turn.chosen_cube

                                if turn.destination.get("out_own_piece"):
                                    board.out_piece(move, turn.color)

                                else:
                                    if turn.destination.get("eat_piece"):
                                        board.eat_piece(board.board[move.get_row_to()][move.get_col_to()].pick())

                                    board.make_move(move)
                                    turn.clear_clicks()

                                if turn.double_ind >= 0:  # If the turn is a "Double Turn"
                                    current_cube = turn.double_ind
                                    turn.increase_double_index()

                                turn.set_source(None)
                                turn.remove_destination()
                                turn.set_cube_played(current_cube, True)

                                if turn.has_all_cubes_playes():  # If the player played with all the cubes
                                    turn.change_turn()
                                    turn.clear_clicks()

                            else:   # If not
                                turn.clear_clicks()
                                turn.set_source(None)
                                turn.remove_destination()

            draw(board, turn, None)
    pygame.quit()
    quit()


if __name__ == "__main__":
    main()



