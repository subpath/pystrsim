# pystrsim
Python wrapper for Rust's [strsim](https://crates.io/crates/strsim) library

Github repo: https://github.com/subpath/pystrsim

## Installation: 
```bash
pip install pystrsim
```

## Usage:
```python
import pystrsim

print(f"hamming: {pystrsim.hamming('hamming', 'hammers')} should be 3")
print(f"levenshtein: {pystrsim.levenshtein('kitten', 'sitting')} should be 3")
print(
    f"normalized_levenshtein: {pystrsim.normalized_levenshtein('kitten', 'sitting')} should be ~0.571"
)
print(f"osa_distance: {pystrsim.osa_distance('ac', 'cba')} should be 3")
print(f"damerau_levenshtein: {pystrsim.damerau_levenshtein('ac', 'cba')} should be 2")
print(
    f"normalized_damerau_levenshtein: {pystrsim.normalized_damerau_levenshtein('levenshtein', 'löwenbräu')} should be ~0.272"
)
print(
    f"jaro: {pystrsim.jaro('Friedrich Nietzsche', 'Jean-Paul Sartre')} should be ~0.392"
)
print(
    f"jaro_winkler: {pystrsim.jaro_winkler('cheeseburger', 'cheese fries')} should be ~0.911"
)
print(
    f"sorensen_dice: {pystrsim.sorensen_dice('web applications', 'applications of the web')} should be ~0.7878787878787878"
)

```

## Is it blazingly fast?

Well, no : ) 
[Jellyfish](https://github.com/jamesturk/jellyfish) and [Levenshtein](https://github.com/ztane/python-Levenshtein) are faster.

See the [benchmark/benchmark.py](benchmark/benchmark.py) file.

| algorithm                      | library      | function                       |        time |
|--------------------------------|--------------|--------------------------------|-------------|
| DamerauLevenshtein             | jellyfish    | damerau_levenshtein_distance   | 0.00593378  |
| Hamming                        | Levenshtein  | hamming                        | 0.000683438 |
| Hamming                        | jellyfish    | hamming_distance               | 0.00112426  |
| Jaro                           | jellyfish    | jaro_similarity                | 0.00206124  |
| JaroWinkler                    | jellyfish    | jaro_winkler_similarity        | 0.00221943  |
| Levenshtein                    | Levenshtein  | distance                       | 0.00115115  |
| Levenshtein                    | jellyfish    | levenshtein_distance           | 0.00257007  |
| damerau_levenshtein            | **pystrsim** | damerau_levenshtein            | 0.380067    |
| hamming                        | **pystrsim** | hamming                        | 0.0116847   |
| jaro                           | **pystrsim** | jaro                           | 0.0547281   |
| jaro_winkler                   | **pystrsim** | jaro_winkler                   | 0.057244    |
| levenshtein                    | **pystrsim** | levenshtein                    | 0.102525    |
| normalized_damerau_levenshtein | **pystrsim** | normalized_damerau_levenshtein | 0.389092    |
| normalized_levenshtein         | **pystrsim** | normalized_levenshtein         | 0.107314    |
| osa_distance                   | **pystrsim** | osa_distance                   | 0.15746     |
| sorensen_dice                  | **pystrsim** | sorensen_dice                  | 0.0973786   |
