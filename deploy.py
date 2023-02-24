from azureml.core import Workspace, ComputeTarget
from azureml.core.model import Model
from azureml.core import Environment
from azureml.core.model import InferenceConfig
from azureml.core.webservice import AksWebservice
from azureml.core.conda_dependencies import CondaDependencies

ws = Workspace(subscription_id="5a341dea-d53d-438c-914c-5405206db17d",
               resource_group="DefaultResourceGroup-centralindia",
               workspace_name="deploy-model")

model = Model.register(ws, model_name="sentiment_analysis", model_path="./sentiment_analysis_model.pkl")

conda_deps = CondaDependencies.create(conda_packages=['numpy', 'pandas', 'spacy', 'scikit-learn'],
                                      pip_packages=['azureml-defaults', 'inference-schema'])
env = Environment(name='myenv')
env.python.conda_dependencies = conda_deps

inf_config = InferenceConfig(
    environment=env,
    source_directory="./source_dir",
    entry_script="./scoring.py",
)

aks_target = ComputeTarget(workspace=ws, name="my-aks")
deployment_config = AksWebservice.deploy_configuration(cpu_cores=1,memory_gb=1)

service = Model.deploy(
    ws,
    "myservice",
    [model],
    inf_config,
    deployment_config,
    aks_target,
    overwrite=True,
)
service.wait_for_deployment(show_output=True)
print(service.get_logs())
