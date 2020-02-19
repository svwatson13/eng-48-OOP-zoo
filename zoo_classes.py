class Animal():
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.character = []
    def add_character(self, character):
        self.character.append(character)

class Mammal(Animal):
    def __init__(self, name, species):
        super().__init__(name, species)

    def character(self, name, species, character):
        return f'name: {name} \nspecies: {species} \nCharacteristics: {character}'
    def facts(self):
        print (' - Mammals are warm-blooded animals'
               '\n- Mammals are born live'
               '\n- Only two mammals hatch from eggs'
               '\n- Mammals drink milk from their mothers'
               '\n- Bats are the only mammals that can fly'
               '\n- Dolphin and whale babies do not sleep the first month of their life')

class Bird(Animal):
    def __init__(self, name, species):
        super().__init__(name, species)

    def character(self, name, species, character):
        return f'name: {name} \nspecies: {species} \nCharacteristics: {character}'
    def facts(self):
        print (' - Birds have feathers, wings, lay eggs and are warm blooded'
               '\n- The Ostrich is the largest bird in the world. It also lays the largest eggs and has the fastest maximum running speed (97 kph)'
               '\n- Birds have hollow bones which help them fly'
               '\n- Hummingbirds can fly backwards'
               '\n- Scientists believe that birds evolved from theropod dinosaurs'
               '\n- There are around 10000 different species of birds worldwide')

class Reptile(Animal):
    def __init__(self, name, species):
        super().__init__(name, species)

    def character(self, name, species, character):
        return f'name: {name} \nspecies: {species} \nCharacteristics: {character}'
    def facts(self):
        print (' - Nearly all reptiles lay shelled eggs'
               '\n- Nearly all reptiles are cold blooded'
               '\n- The first reptiles are believed to have evolved around 320 million years ago'
               '\n- The size of reptile’s brains relative to their body is much smaller than that of mammals'
               '\n- A snake’s scales are made of keratin, the same substance that makes up our hair and fingernails'
               '\n- Some species of gecko can detach their tails in defense. When a predator grabs the tail, the gecko can detach the tail and make its escape')

class Fish(Animal):
    def __init__(self, name, species):
        super().__init__(name, species)

    def character(self, name, species, character):
        return f'name: {name} \nspecies: {species} \nCharacteristics: {character}'
    def facts(self):
        print (' - There are over 30,000 known species of fish'
               '\n- The amazing Spotted Climbing Perch is able to gulp oxygen from the air and can crawl over land using its strong pectoral fins in search of water'
               '\n- American Lobsters have longer life spans than both cats and dogs, living over 20 years'
               '\n- fish can get sunburn, but it is unusual unless there is something about their environment that does not allow them to seek deeper water or some kind of shelter'
               '\n- Fish are so abundant in the world’s oceans, lakes and rivers that new species are constantly being discovered'
               '\n- The world’s largest fish is the whale shark, which can grow to 12 meters (40 feet) long and weigh an average of 19,000 kilograms (42,000 pounds)')

class Amphibian(Animal):
    def __init__(self, name, species):
        super().__init__(name, species)

    def character(self, name, species, character):
        return f'name: {name} \nspecies: {species} \nCharacteristics: {character}'
    def facts(self):
        print (' - Amphibians are cold-blooded animals that possess backbones and display features that lie between those of fish and reptiles'
               '\n- They are characterized by their ability to exploit both aquatic and terrestrial habitats'
               '\n- The name “amphibian”, derived from the Greek amphibios meaning “living a double life,” reflects this dual life strategy'
               '\n- A small cave salamander, the olm also known as “the human fish,” [photo below] has broken the world’s record for longest-lived amphibian – the salamander has the lifespan of over 100 years'
               '\n- The largest living amphibian is the 1.8 m (5 ft 11 in) Chinese giant salamander (Andrias davidianus) [photo below], but this is dwarfed by the extinct 9 m (30 ft) Prionosuchus from the middle Permian of Brazil.'
               '\n- Amphibians have color vision and depth of focus for clear sight')


