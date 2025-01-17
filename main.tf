

provider "aws" {
  region = "us-west-2"  # Set your preferred AWS region
}

# Define a key pair for SSH access
resource "aws_key_pair" "my_key" {
  key_name   = "my-key-pair"
  public_key = file("~/.ssh/id_rsa.pub")  # Replace with the path to your public key
}

# Define a security group for the instance
resource "aws_security_group" "instance_sg" {
  name        = "instance-security-group"
  description = "Allow SSH and HTTP traffic"

  # Allow SSH access
  ingress {
    from_port   = terraform-orb@1.3.4
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  # Allow HTTP access
  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  # Outbound rules (allow all)
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# Define an EC2 instance
resource "aws_instance" "my_instance" {
  ami           = "ami-0c55b159cbfafe1f0" # Amazon Linux 2 AMI in us-west-2, change as needed
  instance_type = "t2.micro"
  key_name      = aws_key_pair.my_key.key_name
  security_groups = [aws_security_group.instance_sg.name]

  tags = {
    Name = "MyInstance"
  }
}

# Output the public IP of the instance
output "instance_ip" {
  description = "The public IP address of the instance"
  value       = aws_instance.my_instance.public_ip
}