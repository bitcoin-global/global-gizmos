# ==========================================================
# This file updates the contents of Helm values file for CI.
# Note: Do not run this script locally!
# ==========================================================
import yaml
import os

# === Helm chart files
fname = "./node/k8s/values.yaml"
chart_name = "./node/k8s/Chart.yaml"
# Open files
stream, chart_stream = open(fname, 'r'), open(chart_name, 'r')
data, chart_data = yaml.load(stream, Loader=yaml.FullLoader), yaml.load(chart_stream, Loader=yaml.FullLoader)

# === Update values.yaml
data['image']['tag'] = os.getenv("BITCOIN_TAG", "v0.19.1")

# === Update Chart.yaml
chart_data['version'] = os.getenv("RELEASE_VERSION", "v0.1.0")

# Save files
with open(fname, 'w') as yaml_file:
    yaml_file.write(yaml.dump(data, default_flow_style=False))

with open(chart_name, 'w') as yaml_file:
    yaml_file.write(yaml.dump(chart_data, default_flow_style=False))