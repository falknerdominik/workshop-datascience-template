# %%

# ENSURE these env variables are set in .devcontainers/env-private!
# ENSURE the .env-private file is in .gitignore!
# ENSURE the .env-private file is in docker-compose.yml in the `env_file` key!

# AWS_ENDPOINT_URL="https://publics3storage.risc-software.at/"
# AWS_ACCESS_KEY_ID="<KEY_OBTAINED_FROM_GUI>"
# AWS_SECRET_ACCESS_KEY="<SECRET_OBTAINED_FROM_GUI>"

from cloudpathlib import CloudPath
import pandas as pd
file = CloudPath("s3://<BUCKET_NAME>") / "<FOLDER>" / "<FILE>.parquet"
data = pd.read_parquet(file)