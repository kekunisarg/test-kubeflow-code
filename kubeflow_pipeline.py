import kfp
from kfp import dsl
import kfp.components as comp

@kfp.dsl.component
def run_main_func1():
    component1 = kfp.dsl.ContainerOp(
        name="component11",
        image = 'docker.io/kekunisarg/test-kubeflow-code',
        command=['python','main.py'],
    )
    return component1

@kfp.dsl.component
def run_main_func2():
    component2 = kfp.dsl.ContainerOp(
        name="component22",
        image = 'docker.io/kekunisarg/test-kubeflow-code',
        command=['python','main.py'],
    )
    return component2

@kfp.dsl.pipeline(
    name = "Test-kubeflow-pipeline",
    description="run-Test-kubeflow-pipeline"
)
def run_pipeline():
    run_comp1 = run_main_func1()
    run_comp1.execution_options.caching_strategy.max_cache_stalness = "P0D"
    run_comp2 = run_main_func2().after(run_comp1)
    run_comp2.execution_options.caching_strategy.max_cache_stalness = "P0D"

if __name__ == '__main__':
    from kfp.compiler import Compiler
    Compiler().compile(run_pipeline,"test-kubeflow-pipeline.yaml")
    # # create kfp client with using pipeline endpoint
    # client = kfp.Client("https://11b521f27cd0a187-dot-us-central1.pipelines.googleusercontent.com")
    #
    # # create experiment
    # EXPERIMENT_NAME = 'test-kubeflow1'
    # experiment = client.create_experiment(name=EXPERIMENT_NAME)
    #
    # # deploy pipeline to kubeflow pipeline endpoint
    # run = client.run_pipeline(experiment.id, 'test-kubeflow1_run', 'test-kubeflow-pipeline.yaml')
