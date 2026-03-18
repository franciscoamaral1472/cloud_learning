# EC2 Basic Server Lab

## Objective
Deploy a basic web server using AWS EC2.

## Steps
1. Launch EC2 instance
2. Configure security group:
   - Port 22 (SSH)
   - Port 80 (HTTP)
3. Connect via SSH
4. Install Apache

## Commands

```bash
sudo apt update
sudo apt install apache2 -y