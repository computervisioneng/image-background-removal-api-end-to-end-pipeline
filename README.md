# image-background-removal-api-end-to-end-pipeline

## pipeline

We are going to work on a simplified end to end pipeline.

![img](https://github.com/computervisiondeveloper/image-background-removal-api-end-to-end-pipeline/blob/b586baa186478e9f2b8be9ef878a2d6b6daa8b15/simplified_pipeline.png)

### requirements

[This](https://docs.google.com/document/d/15IcKAXee-lC-KABkP6USPHWp9rVaOUwWg5rA2ZpEqLQ/edit#).

### planning

![img](https://github.com/computervisiondeveloper/image-background-removal-api-end-to-end-pipeline/blob/14ff384e12a2b964eb6b3bb25a286953e1eb8303/planning.png)

### execution

#### state of the art review

[This](https://docs.google.com/document/d/16E6vUTD4_U3mfoygmmEufgJEVG9boW8qcddvZ7-Uluo/edit#).

#### background removal

[This repository](https://github.com/danielgatis/rembg) is selected as our image background removal algorithm.

Implementation is straightforward, the first step is to install it as a Python package.

    pip install rembg
    
Then, this snippet produces an image with its background removed.

    from rembg import remove

    input_path = 'input.png'
    output_path = 'output.png'

    with open(input_path, 'rb') as i:
        with open(output_path, 'wb') as o:
            input = i.read()
            output = remove(input)
            o.write(output)

#### API

The API is deployed into a t2.2xlarge instance from AWS. 

In order to reproduce the process you should follow these steps:

Log into your AWS account and create an EC2 instance, using the latest stable Ubuntu image.

SSH into the instance and run these commands to update the software repository and install the dependencies.

    sudo apt-get update
    sudo apt install -y python3-pip nginx
    
    sudo nano /etc/nginx/sites-enabled/fastapi_nginx
    
    
And put this config into the file (replace the IP address with your EC2 instance's public IP):

    server {
        listen 80;   
        server_name <YOUR_EC2_IP>;    
        location / {        
            proxy_pass http://127.0.0.1:8000;    
        }
    }

Start NGINX.

    sudo service nginx restart
    
Update EC2 security-group settings for your instance to allow HTTP traffic to port 80.

### image background removal served through an API

    git clone https://github.com/computervisiondeveloper/image-background-removal-api-end-to-end-pipeline.git
    
    pip install -r requirements.txt
    
    cd image-background-removal-api-end-to-end-pipeline
    
    python3 -m uvicorn main:app


### deliverable

[This](https://docs.google.com/document/d/1C0K3h5NMzT7LyNXV1Tb-mMpxStjDZxwYO6_JbylVzfM/edit#heading=h.1ii8xb93tsgb).
