
# IAM Policies
Example of a CloudFormation template that creates an AWS IAM user and attaches three types of policies.

## How to test
To test CF template:
- download template.yml file
- Open AWS Console and go to CloudFormation -> Stacks
<img width="400" alt="Screenshot 2024-08-26 at 10 17 40 PM" src="https://github.com/user-attachments/assets/c4baee3e-fa28-4268-8da9-43a60cd03eb2">

- Create stack -> with new resources (standard)
<img width="600" alt="Screenshot 2024-08-26 at 10 18 19 PM" src="https://github.com/user-attachments/assets/e931cb67-c283-402f-9eb4-7301c325d08d">

- Step 1: Choose 'Upload a template file' and Next.
<img width="600" alt="Screenshot 2024-08-26 at 10 19 12 PM" src="https://github.com/user-attachments/assets/3c6f0028-d319-400b-826d-dc91aab7d35d">

- Step 2: Enter name for the stack, then Next
- Step 3: Next
- Step 4: At the bottom click check mark 'I acknowledge that AWS CloudFormation might create IAM resources with custom names', then Next.

## Clean up 
To clean up, simply delete the stack you created. This will remove all created resources.
