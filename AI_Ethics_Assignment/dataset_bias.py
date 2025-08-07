from aif360.datasets import CompasDataset  
from aif360.metrics import BinaryLabelDatasetMetric  

# Load data  
compas = CompasDataset()  
privileged_group = [{'race': 1}]    
unprivileged_group = [{'race': 0}]    

# Calculate fairness metrics  
metric = BinaryLabelDatasetMetric(compas,  
                                unprivileged_group=unprivileged_group,  
                                privileged_group=privileged_group)  
print("Disparate Impact:", metric.disparate_impact())  
print("False Positive Rate Difference:", metric.false_positive_rate_difference())  