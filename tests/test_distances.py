import pystrsim

assert pystrsim.levenshtein("kitten", "sitting") == 3

assert abs((pystrsim.normalized_levenshtein("kitten", "sitting") - 0.571)) < 0.001

assert pystrsim.osa_distance("ac", "cba") == 3

assert pystrsim.damerau_levenshtein("ac", "cba") == 2

assert (
    abs((pystrsim.normalized_damerau_levenshtein("levenshtein", "löwenbräu") - 0.272))
    < 0.001
)

assert abs((pystrsim.jaro("Friedrich Nietzsche", "Jean-Paul Sartre") - 0.392)) < 0.001

assert abs((pystrsim.jaro_winkler("cheeseburger", "cheese fries") - 0.911)) < 0.001

assert (
    pystrsim.sorensen_dice("web applications", "applications of the web")
    == 0.7878787878787878
)
