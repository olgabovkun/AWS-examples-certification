cd s3/iac/terraform/

terraform init

terraform plan

terraform apply
<!-- 
    will create terrafor.tfstate - it contains metadata about the current state of your infrastructure and maps your Terraform configurations to the actual deployed resources. 
    Don't need to commit this file. 

    Deleting the terraform.tfstate file means Terraform loses track of the resources it manages. If you delete it, Terraform will no longer have information about the deployed infrastructure and may attempt to recreate resources from scratch when you run terraform apply  -->

terraform destroy