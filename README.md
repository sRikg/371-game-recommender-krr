# 371-game-recommender-krr

The ./py/ directory contains the python files pertaining to
* scraping from API([steam_scrapper.py](https://github.com/srikg-msai22/371-game-recommender-krr/blob/main/py/steam_scrapper.py)), 
* extracting the information to python dicts and lists([list_to_clauses_converter.py](https://github.com/srikg-msai22/371-game-recommender-krr/blob/main/py/list_to_clauses_converter.py)), 
* selecting games which have information([game_selector.py](https://github.com/srikg-msai22/371-game-recommender-krr/blob/main/py/game_selector.py)), 
* formatting the krfs into proper predicate format([formatter.py](https://github.com/srikg-msai22/371-game-recommender-krr/blob/main/py/formatter.py)) and
* cleaning and standardizing the attribute values([attribute_formatter.py](https://github.com/srikg-msai22/371-game-recommender-krr/blob/main/py/attribute_formatter.py))

The ./krf/ directory contains the krf flatfiles which contain representations about
* Facts Files ([Facts 1](https://github.com/srikg-msai22/371-game-recommender-krr/blob/main/krfs/game_facts1.krf), [Facts 2](https://github.com/srikg-msai22/371-game-recommender-krr/blob/main/krfs/game_facts2.krf), [Facts 3](https://github.com/srikg-msai22/371-game-recommender-krr/blob/main/krfs/game_facts3.krf), [Facts 4](https://github.com/srikg-msai22/371-game-recommender-krr/blob/main/krfs/game_facts4.krf), [Facts 5](https://github.com/srikg-msai22/371-game-recommender-krr/blob/main/krfs/game_facts5.krf), [Facts 6](https://github.com/srikg-msai22/371-game-recommender-krr/blob/main/krfs/game_facts6.krf), [Facts 7](https://github.com/srikg-msai22/371-game-recommender-krr/blob/main/krfs/game_facts7.krf))
* Ontology files ([Base Predicates](https://github.com/srikg-msai22/371-game-recommender-krr/blob/main/krfs/game_ontology.krf), [Additional Predicates](https://github.com/srikg-msai22/371-game-recommender-krr/blob/main/krfs/game_ontology_additional.krf))
* The Horn Clauses for the Recommender([Rules](https://github.com/srikg-msai22/371-game-recommender-krr/blob/main/krfs/game_rules.krf))

Addtional Information
* The facts files were broken into 7 parts as that facilitated an easier uploading to the NextKB
* Some of the text and file edits were done manually
