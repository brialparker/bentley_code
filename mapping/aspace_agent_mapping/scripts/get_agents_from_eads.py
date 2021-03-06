import os

from lxml import etree
from tqdm import tqdm

from utilities.ead_utilities.ead_utilities import EADDir


def get_all_agents(input_dir):
    """
    Directs extraction of controlaccess terms from a directory of EADs.

    :param input_dir: filepath to the input director
    :return: a dictionary in the form {"corpname": {"Apple Computer": [authid, naming_source], etc.},
                                       "persname": {"Jane Doe (1900-1911)": [authid, naming_source], etc.},
                                       "famname": {"Adams family": [authid, _naming_source], etc.}}
    """

    agent_types = ["corpname", "persname", "famname"]
    agents = dict(zip(agent_types, [{}, {}, {}]))

    ead_dir = EADDir(input_dir=input_dir)

    for ead in tqdm(ead_dir.ead_files, desc="grabbing all agents from eads"):
        tree = etree.parse(os.path.join(ead_dir.input_dir, ead))
        all_agents = get_agents_from_ead(tree)

        for key, value in all_agents.items():
            agents[key].update(value)

    return agents


def get_agents_from_ead(tree):
    """
    Extracts controlaccess terms from an lxml etree

    :param tree: an lxml etree representation of an EAD
    :return: a dictionary in the form {"corpname": {"Apple Computer": [authid, naming_source], etc.},
                                       "persname": {"Jane Doe (1900-1911)": [authid, naming_source], etc.},
                                       "famname": {"Adams family": [authid, _naming_source], etc.}}
    """

    agent_types = ["corpname", "persname", "famname"]
    results_dict = dict(zip(agent_types, [{}, {}, {}]))

    for agent_type in agent_types:
        tags = tree.xpath("//controlaccess/{}".format(agent_type)) + tree.xpath("//origination/{}".format(agent_type))

        for tag in tags:
            auth = unicode(tag.attrib.get("authfilenumber", ""))
            source = unicode(tag.attrib.get("source"))
            attribs = [auth, source]
            name = unicode(tag.text)

            if name in results_dict[agent_type]:
                if auth and not results_dict[agent_type][name]:
                    results_dict[agent_type][name] = attribs
            else:
                results_dict[agent_type][name] = attribs

    return results_dict


if __name__ == "__main__":
    pass





