import requests

url = "https://www.dnd5eapi.co/graphql"

def demo_query():
    body = """
        query demo {
            races {
                index
                name
                age
                alignment
                language_desc
                size_description
            }
            subraces {
                index
                name
                desc
            }
            classes {
                name
            }
            subclasses {
                index
                name
                desc
            }
            alignments {
                index
                name
                desc
            }
        }
           """
    response = requests.post(url=url, json={"query": body}).json()
    races = [{"index": race['index'], "name": race["name"], "desc": "\n".join([race['age'], race['alignment'], race['language_desc'], race['size_description']])} for race in response['data']['races']]
    subraces = response['data']['subraces']
    classes = response['data']['classes']
    subclasses = response['data']['subclasses']
    alignments = response['data']['alignments']
    return {"races":races, "subraces":subraces, "classes":classes, "subclasses":subclasses, "alignments":alignments}

def vitals_query():
    body = """
        query vitals {
            conditions {
                name
                desc
            } 
        }
           """
    response = requests.post(url=url, json={"query": body}).json()
    response = [{"name": condition["name"], "desc": "\n".join(condition['desc'])} for condition in response['data']['conditions']]
    return response

def spells_query():
    body = """
        query spells {
            spells {
              name
              classes {
                name
              }
              level
              desc
            } 
        }
           """
    response = requests.post(url=url, json={"query": body}).json()
    response = [{"name": spell["name"], "classes":spell["classes"], "desc": "\n".join(spell['desc'])} for spell in response['data']['spells']]
    return response

def spells_query():
    body="""
        query Spells {
            spells {
                name
                index
                level
                desc
            }
        }
    """
    response = requests.post(url=url, json={"query": body}).json()
    response = response['data']['spells']
    spells = [{"name": spell['name'], "index": spell['index'], "level": spell['level'], "desc": "\n".join(spell['desc'])} for spell in response]
    return spells

def proficiency_query():
    body = """
        query proficiency {
            skills {
                name
            }
            proficiencies {
                name
                type
            }
            languages{
                name
            }
            traits{
                name
            }
            features{
                name
            }
        }
           """
    response = requests.post(url=url, json={"query": body}).json()
    skills = [skill for skill in response['data']['skills']]
    weapons = []
    armor = []
    tools = []
    languages = [language for language in response['data']['languages']]
    traits = [trait for trait in response['data']['traits']]
    features = [feature for feature in response['data']['features']]
    for proficiency in response['data']['proficiencies']:
        if proficiency['type'] == 'WEAPONS':
            weapons.append({"name": proficiency['name']})
        if proficiency['type'] == 'ARMOR':
            armor.append({"name":proficiency['name']})
        if proficiency['type'] == ('ARTISANS_TOOLS' or 'MUSICAL_INSTRUMENTS' or 'VEHICLES' or 'GAMING_SETS' or 'OTHER'):
            tools.append({"name":proficiency['name']})
    proficiencies = {'skills':skills, 'weapons':weapons, 'armor':armor, 'tools': tools, 'languages':languages, 'traits':traits, 'features':features}
    
    return proficiencies

def items_query():
    body = """
    query Query {
        equipments{
            name
            equipment_category {
                index
            }
        }
    }
           """
    response = requests.post(url=url, json={"query": body}).json()
    weapons = []
    armor = []
    tools = []
    for item in response['data']['equipments']:
        if item['equipment_category']['index'] == 'weapon':
            weapons.append({"name": item['name']})
        elif item['equipment_category']['index'] == 'armor':
            armor.append({"name": item['name']})
        else:
            tools.append({"name": item['name']})
    items = {'weapons':weapons,'armor':armor, 'tools': tools}
    return items
