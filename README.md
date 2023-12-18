# image-background-removal-api-end-to-end-pipeline

End to end pipeline real world computer vision project!

[![Watch the video](https://img.youtube.com/vi/xgtujvjKIGs/0.jpg)](https://www.youtube.com/watch?v=xgtujvjKIGs)

## pipeline

We are going to work on this simplified end to end pipeline:

![img](https://github.com/computervisiondeveloper/image-background-removal-api-end-to-end-pipeline/blob/b586baa186478e9f2b8be9ef878a2d6b6daa8b15/simplified_pipeline.png)

### requirements

[This](https://docs.google.com/document/d/1CbJLR0CW8UoJ3ZqIi8rkTQCDcBDnaenN/edit?usp=drive_link&ouid=107960887514237623929&rtpof=true&sd=true).

### planning

![img](https://github.com/computervisiondeveloper/image-background-removal-api-end-to-end-pipeline/blob/14ff384e12a2b964eb6b3bb25a286953e1eb8303/planning.png)

### execution

#### state of the art review

[This](https://docs.google.com/document/d/1okXH0WwAznkjQCDh_ZY9uRtl9u5aocl5/edit?usp=drive_link&ouid=107960887514237623929&rtpof=true&sd=true).

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

#### image background removal served through an API

    git clone https://github.com/computervisiondeveloper/image-background-removal-api-end-to-end-pipeline.git
    
    cd image-background-removal-api-end-to-end-pipeline

Create a virtual environment and install requirements.

    sudo apt install python3-virtualenv

    virtualenv venv --python=python3
    
    source venv/bin/activate

    pip install -r requirements.txt

Launch app.
    
    python3 -m uvicorn main:app


### deliverable

[This](https://docs.google.com/document/d/1zwRmXQDsDvB9vg2lHc3zYwjIxJ4b-YNu/edit?usp=drive_link&ouid=107960887514237623929&rtpof=true&sd=true).
