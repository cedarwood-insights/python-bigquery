# -*- coding: utf-8 -*-
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Generated code. DO NOT EDIT!
#
# Snippet for ListModels
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-bigquery


# [START bigquery_generated_bigquery_v2_ModelService_ListModels_async]
from google.cloud import bigquery_v2


async def sample_list_models():
    # Create a client
    client = bigquery_v2.ModelServiceAsyncClient()

    # Initialize request argument(s)
    request = bigquery_v2.ListModelsRequest(
        project_id="project_id_value", dataset_id="dataset_id_value",
    )

    # Make the request
    response = await client.list_models(request=request)

    # Handle response
    print(response)


# [END bigquery_generated_bigquery_v2_ModelService_ListModels_async]