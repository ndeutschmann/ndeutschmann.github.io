from scholarly import scholarly
import tomlkit

nico = next(scholarly.search_author('Nicolas Deutschmann'))
scholarly.fill(nico, sections=["indices"])
citations = nico["citedby"]
h_index = nico["hindex"]

with open("config.toml", "r") as cf:
    config = tomlkit.load(cf)

config["params"]["footer"]["citation_count"] = citations
config["params"]["footer"]["h_index"] = h_index

with open("config.toml", "w") as cf:
    tomlkit.dump(config, cf)



