# VM Creation through VirtualBox

## Introduction

This document outlines the steps to create and configure a virtual machine (VM) using VirtualBox, specifically for hosting a dummy website with Nginx on Ubuntu 22.04.

## Features

- Virtual machine setup using VirtualBox.
- Ubuntu 22.04 installation.
- Nginx web server installation and configuration.
- Hosting a dummy website.

## Prerequisites

- VirtualBox shall be installed on your system.
- Ubuntu 22.04 image file from osboxes.org
- Internet access for downloading software and updates.

## Installation

1. **Downloaded and Installed VirtualBox**:
   - Visited the VirtualBox website: [VirtualBox](https://www.virtualbox.org/).
   - Downloaded the VirtualBox version "VirtualBox 7.0.20 platform packages for Windows."
   - Downloaded and installed `.exe` file by following the on-screen instructions.

2. **Download Ubuntu Image**:
   - Visiedt [OSBoxes](https://www.osboxes.org/) and downloaedd the Ubuntu 22.04 image.
   - Unziped the Ubuntu image on my local system.

## Configuration

1. **Created a New VM in VirtualBox**:
   - Opened Oracle VirtualBox.
   - Clicked on `NEW` to create a new virtual machine.
   - Populated the `NAME`, `TYPE`, and `VERSION` fields according to the Ubuntu version downloaded.
   - Adjusted memory allocation, RAM settings, and other configurations for the Linux VM.

2. **Set Up Ubuntu**:
   - Started the VM and logged in using the default username and password.
     - Default credentials can be found on the OSBoxes website.

3. **Configure Nginx and Host a Dummy Website**:
   - Opeedn the terminal in Ubuntu and executed the following commands:
     ```bash
     sudo apt-get update
     sudo apt-get install nginx
     cd /var/www/html
     sudo rm -r *
     sudo nano index.html
     sudo systemctl start nginx
     sudo systemctl status nginx
     sudo apt-get install net-tools
     ifconfig # Copy the IP address and open it in the Ubuntu web browser
     ```

## Testing

1. **Verifed the Website Hosting**:
   - Opened the web browser in Ubuntu and entered the IP address obtained from the `ifconfig` command.
   - Ensured that the dummy website loaded correctly.
  
2. Used NMAP windows version to scan for VMs hosted online
   - Went to the link - https://nmap.org/download.html#windows
   - Downloaded and completed all the steps to install the exe file
   - Opened Zenmap, a GUI for NMAP windows
   - in the target field gave the IP address of the ubuntu which i got by typing in the following command in Ubuntu terminal
     ``` bash
     ifconfig
   - selected "intense scan" in profile section

## Conclusion

Successfully created and configured a virtual machine using VirtualBox. Installed Ubuntu 22.04 and set up Nginx to host a dummy website, validating the setup by accessing the website through the browser.


