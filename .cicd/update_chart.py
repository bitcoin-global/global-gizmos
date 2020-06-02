# ==========================================================
# This file updates the contents of Helm values file for CI.
# Note: Do not run this script locally!
# ==========================================================
import os
import hiyapyco
import pprint
import yaml

# ==========================================================
# ============================ Update valus.yaml
# ==========================================================
valuesFile = "./node/k8s/values.yaml"
valuesFileUpdated = "./node/k8s/values_updated.yaml"
with open(valuesFile) as fp:
    yaml1 = yaml.load(fp, Loader=yaml.FullLoader)
with open(valuesFileUpdated) as fp:
    yaml1_updated = yaml.load(fp, Loader=yaml.FullLoader)

# === Update
merged_yaml = hiyapyco.load(valuesFile, valuesFileUpdated, method=hiyapyco.METHOD_MERGE)

# === Save
with open(valuesFile, 'w') as yaml_file:
    yaml_file.write(hiyapyco.dump(merged_yaml, default_flow_style=False))

# ==========================================================
# ============================ Update Chart.yaml
# ==========================================================
chartFile = "./node/k8s/Chart.yaml"
with open(chartFile) as fp:
    chart_data = yaml.load(fp, Loader=yaml.FullLoader)

# === Update
chart_data['version'] = os.getenv("RELEASE_VERSION")

# === Save
with open(chartFile, 'w') as yaml_file:
    yaml_file.write(yaml.dump(chart_data, default_flow_style=False))
