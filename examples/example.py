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
