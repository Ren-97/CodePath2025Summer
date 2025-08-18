# p1 : Most Endangered Species

def most_endangered(species_list):
    lowest_pop = float('inf')
    endangered_species = ''
    for species in species_list:
        if species['population'] < lowest_pop:
            lowest_pop = species['population']
            endangered_species = species['name']
    return endangered_species

species_list = [
    {"name": "Amur Leopard",
     "habitat": "Temperate forests",
     "population": 84
    },
    {"name": "Javan Rhino",
     "habitat": "Tropical forests",
     "population": 72
    },
    {"name": "Vaquita",
     "habitat": "Marine",
     "population": 10
    }
]

#print(most_endangered(species_list))

# p2 : Identifying Endangered Species

def count_endangered_species(endangered_species, observed_species):
    endangered_set = set(endangered_species)
    species_cnt = 0
    for species in observed_species:
        if species in endangered_set:
            species_cnt += 1
    return species_cnt

endangered_species1 = "aA"
observed_species1 = "aAAbbbb"

endangered_species2 = "z"
observed_species2 = "ZZ"

#print(count_endangered_species(endangered_species1, observed_species1)) 
#print(count_endangered_species(endangered_species2, observed_species2))  


# Problem 4: Gallery Subdomain Traffic
def subdomain_visits(cpdomains):
    domains = {}
    for name in cpdomains:
        splitted = name.split()
        views = int(splitted[0])
        alldomains = splitted[1].split('.')
        if len(alldomains) == 2:
            fulldomains = [alldomains[0] + '.' + alldomains[1], alldomains[1]]
        elif len(alldomains) == 3:
            fulldomains = [alldomains[0] + '.' + alldomains[1] + '.' + alldomains[2], 
                           alldomains[1] + '.' + alldomains[2], alldomains[2]]
        for subdomain in fulldomains:
            if subdomain not in domains.keys():
                domains[subdomain] = views
            else:
                domains[subdomain] += views
    cpsubdomains = []
    for domain, view in domains.items():
        cpsubdomains.append(str(view) + ' ' + domain)
    return cpsubdomains

cpdomains1 = ["9001 modern.artmuseum.com"]
cpdomains2 = ["900 abstract.gallery.com", "50 impressionism.com", 
              "1 contemporary.gallery.com", "5 medieval.org"]

print(subdomain_visits(cpdomains1))
print(subdomain_visits(cpdomains2))

