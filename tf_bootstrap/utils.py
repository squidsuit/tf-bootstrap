import os, yaml

def load_config():
    try:
        with open("./tf_bootstrap/config.yml", "r") as ymlfile:
            cfg = yaml.safe_load(ymlfile)
        # scm_pat = cfg["source_control"]["gitlab"]["pat"]
        # print(scm_pat)
        return cfg
    except Exception as e:
        print(e)
