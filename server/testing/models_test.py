from models import Zookeeper, Enclosure, Animal

class TestZookeeper:
    def test_converts_to_dict(self):
        zk = Zookeeper(name='John', birthday='1990-01-01')
        zk_dict = zk.to_dict()
        assert isinstance(zk_dict, dict)
        assert 'name' in zk_dict
        assert 'birthday' in zk_dict

class TestEnclosure:
    def test_converts_to_dict(self):
        enc = Enclosure(environment='Savannah', open_to_visitors=True)
        enc_dict = enc.to_dict()
        assert isinstance(enc_dict, dict)
        assert 'environment' in enc_dict
        assert 'open_to_visitors' in enc_dict

class TestAnimal:
    def test_converts_to_dict(self):
        zookeeper = Zookeeper(name='John', birthday='1990-01-01')
        enclosure = Enclosure(environment='Savannah', open_to_visitors=True)
        animal = Animal(name='Lion', species='Big Cat', zookeeper=zookeeper, enclosure=enclosure)
        animal_dict = animal.to_dict()
        assert isinstance(animal_dict, dict)
        assert 'name' in animal_dict
        assert 'species' in animal_dict
        assert 'zookeeper' in animal_dict
        assert 'enclosure' in animal_dict
