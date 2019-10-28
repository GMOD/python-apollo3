import json
import time

from . import ApolloTestCase, wa


class OrganismTest(ApolloTestCase):

    def test_get_organisms(self):

        orgs = wa.organisms.get_organisms()

        assert len(orgs) >= 3

        first_org = orgs[0]

        assert 'nonDefaultTranslationTable' in first_org
        assert 'annotationCount' in first_org
        assert 'commonName' in first_org
        assert 'obsolete' in first_org
        assert 'id' in first_org
        assert 'publicMode' in first_org
        assert 'valid' in first_org
        assert 'currentOrganism' in first_org
        assert 'sequences' in first_org
        assert 'directory' in first_org
        assert 'blatdb' in first_org
        assert 'genus' in first_org
        assert 'species' in first_org
        assert 'metadata' in first_org

        assert 'apollo_shared_dir/org' in first_org['directory']
        assert first_org['commonName'] in ['test_organism', 'alt_org', 'org3', 'org4']

    def test_get_organism_creator(self):

        orgs = wa.organisms.get_organisms()

        org_id = orgs[0]['id']

        creator = wa.organisms.get_organism_creator(str(org_id))

        assert 'creator' in creator

    def test_show_organism(self):

        orgs = wa.organisms.get_organisms()

        org_id = orgs[0]['id']

        org_info = wa.organisms.show_organism(org_id)

        assert org_info == orgs[0]

    def test_show_organism_cn(self):

        orgs = wa.organisms.get_organisms()

        org_cn = orgs[0]['commonName']

        org_info = wa.organisms.show_organism(org_cn)

        assert org_info == orgs[0]

    def test_get_sequences(self):

        orgs = wa.organisms.get_organisms()

        org_id = orgs[0]['id']

        seqs = wa.organisms.get_sequences(org_id)

        assert 'sequences' in seqs
        assert seqs['sequences'][0]['name'] == 'Merlin'
        assert seqs['sequences'][0]['length'] == 172788
        assert seqs['sequences'][0]['start'] == 0
        assert seqs['sequences'][0]['end'] == 172788

    def test_update_metadata(self):

        orgs = wa.organisms.get_organisms()

        org_id = orgs[0]['id']

        res = wa.organisms.update_metadata(org_id, {'some': 'metadata'})

        assert res == {}

        org_info = wa.organisms.show_organism(org_id)

        assert json.loads(org_info['metadata']) == {'some': 'metadata'}

    def test_delete_organism(self):

        org_info = wa.organisms.show_organism('org4')

        # TODO add a test with commonName too (broken in 2.4.1, should be fixed in 2.4.2)
        wa.organisms.delete_organism(org_info['id'])
        # Returns useless stuff

        time.sleep(2)

        orgs = wa.organisms.get_organisms()

        for org in orgs:
            assert org['commonName'] != 'org4'

    def test_delete_features(self):

        org_info = wa.organisms.show_organism('org3')

        feats_before = wa.annotations.get_features(org_info['id'], 'Merlin')

        assert 'features' in feats_before
        assert len(feats_before['features']) > 0

        # TODO add a test with commonName too (broken in 2.4.1, should be fixed in 2.4.2)
        wa.organisms.delete_features(org_info['id'])

        feats_after = wa.annotations.get_features(org_info['id'], 'Merlin')

        assert 'features' in feats_after
        assert len(feats_after['features']) == 0

    def test_update_organism(self):

        org_info = wa.organisms.show_organism('test_organism')

        # TODO add a test with commonName too (broken in 2.4.1, should be fixed in 2.4.2)
        wa.organisms.update_organism(org_info['id'], 'test_organism', org_info['directory'], species='updatedspecies', genus='updatedgenus', blatdb='/some/where')
        # Returns useless stuff

        time.sleep(2)
        org_info = wa.organisms.show_organism('test_organism')

        assert org_info['species'] == 'updatedspecies'
        assert org_info['genus'] == 'updatedgenus'
        assert org_info['blatdb'] == '/some/where'
