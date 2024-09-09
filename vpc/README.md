# Create
In this example we are going to create VPC, IGW and Subnet

## Init
```sh
cd vpc
chmod +x create-vpc
chmod +x delete-vpc
```

## Create VPC, IGW and SUBNET
```sh
./create-vpc
```

## Cleanup
To delete resources, replace <vpc_id>, <igw_id>, and <subnet_id> with the IDs provided in the previous script
```sh
./delete-vpc <vpc_id> <igw_id> <subnet_id>
```