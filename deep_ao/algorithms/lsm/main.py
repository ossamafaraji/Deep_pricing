import numpy as np
from tqdm import trange

from deep_ao.algorithms.lsm.run import run
from deep_ao.config import (STRIKE, initial_values, number_assets,
                            simulation_params)

number_paths = {
    "n_train": 20000,
    "n_upper": 2000,
    "n_lower": 20000,
}


def main():

    np.random.seed(0)

    result_table = []
    for n_assets in number_assets:
        for initial_value in initial_values:
            print(f"training model for d = {n_assets}, s0 = {initial_value}")

            l = []
            for _ in trange(1):
                out = run(
                    strike=STRIKE,
                    n_assets=n_assets,
                    initial_value=initial_value,
                    number_paths=number_paths,
                    simulation_params=simulation_params,
                )
                l.append(out)

            l = np.array(l)
            result_table.append(l.mean(0))

    return result_table


if __name__ == "__main__":
    results = main()
    print(results)