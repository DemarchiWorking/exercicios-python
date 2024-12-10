import time
import random
import concurrent.futures
import threading
import asyncio

db = {
    92345: ("Benedito", 8.5),
    83456: ("Odair", 7.0),
    74567: ("Adalberto", 9.2),
    65678: ("Carminda", 6.5),
    56789: ("Genoveva", 7.8)
}

lock = threading.Lock()


def get_record_by_id(matricula):
    time.sleep(3)
    with lock:
        record = db.get(matricula, ("Usuario", 0))
    return record


def get_all_records():
    time.sleep(30)
    with lock:
        return db.items()


def consulta_concorrente():
    matriculas = [92345, 83456, 74567, 65678, 56789]
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_record_by_id, m) for m in matriculas]
        resultados = [future.result() for future in concurrent.futures.as_completed(futures)]

    for matricula, (nome, nota) in zip(matriculas, resultados):
        print(f"Matricula= {matricula}, nome= {nome}, nota= {nota}")

    notas = [nota for _, nota in resultados]
    media = sum(notas) / len(notas)
    print(f"Nota media= {media}")


def consulta_assincrona():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_all = executor.submit(get_all_records)
        time.sleep(1)
        resultado = get_record_by_id(92345)
        print(f"Individual - Nome= {resultado[0]}, nota= {resultado[1]}")
        future_all.cancel()


async def generator():
    for _ in range(1000):
        yield random.randint(0, 100)
        await asyncio.sleep(0.01)


async def narrator(generator, players):
    async for number in generator:
        print(f"Numero e {number}")
        for player in players:
            await player.process_number(number)
        if any(player.won for player in players):
            break


class Player:
    def __init__(self, name, card):
        self.name = name
        self.card = set(card)
        self.numbers_found = set()

    @property
    def won(self):
        return self.card == self.numbers_found

    async def process_number(self, number):
        if number in self.card:
            self.numbers_found.add(number)
        print(f"{self.name} {number} {self.card} {len(self.numbers_found)}")
        await asyncio.sleep(0.01)  # Simula tempo de processamento


async def main_bingo():
    players_list = [
        ("player-1", [5, 10, 48, 55]),
        ("player-2", [8, 46, 80, 99]),
        ("player-3", [17, 29, 78, 95])
    ]
    players = [Player(name, card) for name, card in players_list]
    gen = generator()
    await narrator(gen, players)

    for player in players:
        if player.won:
            print(f"{player.name} foi o vencedor ! Winer {player.card} {player.numbers_found}")
            break
    else:
        print("Game is over. Não tivemos ganhadores até o final")


if __name__ == "__main__":
    print("Concorrentes:")
    consulta_concorrente()

    print("Assíncrona:")
    consulta_assincrona()

    print("Jogo de Bingo:")
    asyncio.run(main_bingo())
