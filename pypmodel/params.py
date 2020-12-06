import pkg_resources
import dotmap
import yaml

# TODO - think about being able to load a user preset
# TODO - maybe define here and not in YAML? Probably faster (can convert to
#        numpy and compile).


PARAM_FILE = pkg_resources.resource_filename('pypmodel', 'data/params.yaml')

with open(PARAM_FILE) as param:
    PARAM = dotmap.DotMap(yaml.load(param, Loader=yaml.SafeLoader))
