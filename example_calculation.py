import numpy as np
import click

@click.command()
@click.option('--n', default=5, help='Number of iterations.')
@click.option('--random_seed', default=123, help='random seed')
def run_calc(n, random_seed,
):
    np.random.seed(random_seed)
    print(np.random.normal(size=(n, )).mean(), f"from {n} random numbers")

if __name__ == "__main__":
    run_calc()