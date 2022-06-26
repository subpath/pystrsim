# shamelessly borrowed from here: https://github.com/life4/textdistance/blob/master/textdistance/benchmark.pys
from timeit import timeit

from collections import defaultdict, namedtuple
from tabulate import tabulate
from libraries import LIBRARIES_FILE, prototype

pairs_of_strings = [
    ("kfc", "mcd"),
    ("pizza", "pitta"),
    ("fresh green apple", "delicios apple pie"),
    (
        "We cannot solve our problems with the same thinking we used when we created them",
        "The only reason for time is so that everything doesnt happen at once",
    ),
]

ALGORITHMS = [
    "hamming",
    "levenshtein",
    "normalized_levenshtein",
    "osa_distance",
    "damerau_levenshtein",
    "normalized_damerau_levenshtein",
    "jaro",
    "jaro_winkler",
    "sorensen_dice",
]


# STMT = ""
# for (string1, string2) in pairs_of_strings:
#     STMT += f"func('{string1}', '{string2}')\n"

STMT = """
func('text', 'test')
func('qwer', 'asdf')
func('a' * 15, 'b' * 15)
"""

RUNS = 2000
INTERNAL_SETUP = """
from pystrsim import {} as func
"""

EXTERNAL_SETUP = """
from {library} import {function} as func
presets = {presets}
if presets:
    func = func(presets)
"""

Lib = namedtuple("Lib", ["algorithm", "library", "function", "time", "presets"])

libraries = prototype.clone()


class Benchmark:
    @staticmethod
    def get_installed():
        for alg in libraries.get_algorithms():
            for lib in libraries.get_libs(alg):
                # try load function
                if not lib.get_function():
                    continue
                # return library info
                yield Lib(
                    algorithm=alg,
                    library=lib.module_name,
                    function=lib.func_name,
                    time=float("Inf"),
                    presets=lib.presets,
                )

    @staticmethod
    def get_external_benchmark(installed):
        for lib in installed:
            yield lib._replace(
                time=timeit(
                    stmt=STMT,
                    setup=EXTERNAL_SETUP.format(**lib._asdict()),
                    number=RUNS,
                )
            )

    @staticmethod
    def get_internal_benchmark():
        for alg in ALGORITHMS:
            yield Lib(
                algorithm=alg,
                library="**pystrsim**",
                function=alg,
                time=timeit(
                    stmt=STMT,
                    setup=INTERNAL_SETUP.format(alg),
                    number=RUNS,
                ),
                presets=None,
            )

    @staticmethod
    def get_table(data):
        table = tabulate(
            [tuple(i[:-1]) for i in data],
            headers=["algorithm", "library", "function", "time"],
            tablefmt="orgtbl",
        )
        table += "\nTotal: {} libs.\n\n".format(len(data))
        return table

    @classmethod
    def run(cls):
        installed = list(cls.get_installed())
        installed.sort()

        benchmark = list(cls.get_external_benchmark(installed))
        benchmark_internal = list(cls.get_internal_benchmark())
        benchmark += benchmark_internal
        benchmark.sort(key=lambda x: (x.algorithm, x.time))
        print(cls.get_table(benchmark))


if __name__ == "__main__":
    Benchmark.run()
