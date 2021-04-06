from project.player.player import Player


class BattleField:

    def fight(self, attacker: Player, enemy: Player):

        if attacker.is_dead or enemy.is_dead:
            raise ValueError("Player is dead!")

        if self.is_beginner(attacker):
            attacker.beginner_upgrade()
        if self.is_beginner(enemy):
            enemy.beginner_upgrade()

        attacker.health += sum([card.health_points for card in attacker.card_repository.cards])
        enemy.health += sum([card.health_points for card in enemy.card_repository.cards])

        for c in attacker.card_repository.cards:
            if enemy.is_dead or attacker.is_dead:
                return
            enemy.take_damage(c.damage_points)

        for c in enemy.card_repository.cards:
            if enemy.is_dead or attacker.is_dead:
                return
            attacker.take_damage(c.damage_points)

    @staticmethod
    def is_beginner(player):
        return player.__class__.__name__ == "Beginner"
