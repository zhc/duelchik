from duelchik.server.models import DuelchikResponse


class Message:

    YOUR_TURN = 'YOUR_TURN'
    ENEMY_TURN = 'ENEMY_TURN'
    WAITING_PLAYER = 'WAITING_PLAYER'
    GAME_OVER = 'GAME_OVER'
    ERROR = 'ERROR'

    def __init__(self, player):
        self.player = player

    def response(self):
        state = Message.WAITING_PLAYER
        if self.player.is_active:
            state = Message.YOUR_TURN
        elif self.player.enemy and self.player.enemy.is_active:
            state = Message.ENEMY_TURN
        elif self.player.is_someone_dead():
            state = Message.GAME_OVER
        error_message = ''
        win = 0
        if self.player.enemy and self.player.enemy.is_dead:
            win = 1
        enemy_index = self.player.size - 1
        if self.player.enemy:
            enemy_index = self.player.size - self.player.enemy.position - 1
        return DuelchikResponse(
                state=state,
                error_message=error_message,
                deck=self.player.cards,
                win=win,
                size=self.player.size,
                your_index=self.player.position,
                enemy_index=enemy_index,
                stack_size=23
                )


class ErrorMessage:

    def __init__(self, error_message):
        self.msg = error_message
        print(error_message)

    def response(self):
        return DuelchikResponse(
                state=Message.ERROR,
                error_message=self.msg,
                deck=[],
                win=0,
                size=0,
                your_index=0,
                enemy_index=0,
                stack_size=0
                )
