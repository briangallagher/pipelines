# Copyright 2018-2022 The Kubeflow Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Namespace link to external kfp-pipeline-spec package.

This module provides access to the external kfp-pipeline-spec package
under the kubeflow.kfp namespace for backward compatibility.
"""

# Import and re-export the external pipeline_spec_pb2 module
try:
    from kfp_pipeline_spec import pipeline_spec_pb2
except ImportError as e:
    raise ImportError(
        "The 'kfp-pipeline-spec' package is required but not installed. "
        "Please install it with: pip install kfp-pipeline-spec==0.8.0"
    ) from e

# Re-export for backward compatibility
__all__ = ['pipeline_spec_pb2'] 